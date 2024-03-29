#!/usr/bin/env python3
#
# This script takes a CSV file with the description of benchmarks
# and sets up a directory to run the experiments in. It also generates
# the necessary scripts to run the experiments.
#
# Jure Kukovec, Igor Konnov, 2019

import argparse
import configparser
import os
import shutil
import stat
import sys
import csv
from os.path import realpath


def os_specific_commands():
    if sys.platform.startswith("linux"):
        cmds = {"time": "/usr/bin/time", "timeout": "/usr/bin/timeout"}
    elif sys.platform == "darwin":
        cmds = {"time": "gtime", "timeout": "gtimeout"}
    else:
        print("Platform %s is not supported" % sys.platform)
        sys.exit(1)

    return cmds


os_cmds = os_specific_commands()


def parse_options():
    parser = argparse.ArgumentParser(
        description="Generate a script to run Apalache tests."
    )
    parser.add_argument(
        "config",
        type=str,
        help="An input CSV that contains the parameters of the experiments",
    )
    # TODO Make this take a docker tag
    parser.add_argument(
        "apalacheDir", type=realpath, help="The APALACHE source code directory."
    )
    parser.add_argument(
        "specDir", type=realpath, help="The directory that contains the benchmarks."
    )
    parser.add_argument(
        "outDir",
        type=realpath,
        help="The directory to write the scripts and outcome of the experiments.",
    )
    parser.add_argument(
        "--memlimit",
        dest="memlimit",
        default=0,
        type=int,
        help="Set memory limits in GB (default: 0)",
    )
    parser.add_argument(
        "--iniFile",
        dest="iniFile",
        default=None,
        type=realpath,
        help="The name of an .ini file that contains configuration parameters",
    )
    args = parser.parse_args()
    return args


def tool_cmd(args, ini_params, exp_dir, tla_filename, csv_row):
    def kv(key):
        return "--%s=%s" % (key, csv_row[key]) if csv_row[key].strip() != "" else ""

    tool = csv_row["tool"]
    apalache_dir = args.apalacheDir
    ctime = "%s -f 'elapsed_sec: %%e maxresident_kb: %%M' -o time.out" % os_cmds["time"]
    ctimeout = "%s --foreground %s" % (os_cmds["timeout"], csv_row["timeout"])
    if tool == "apalache":
        return "%s %s %s/bin/apalache-mc check --profiling=true --run-dir=./out %s %s %s %s %s %s | tee apalache.out" % (
            ctime,
            ctimeout,
            args.apalacheDir,
            kv("init"),
            kv("next"),
            kv("inv"),
            csv_row["args"],
            ini_params.get("more_args", ""),
            tla_filename,
        )
    elif tool == "tlc":
        # TLC needs a configuration file, it should be created by the user
        # figure out how to run tlc
        init, next, inv, user_args = kv("init"), kv("next"), kv("inv"), csv_row["args"]
        mem = "-Xmx%dm" % (1024 * args.memlimit) if args.memlimit > 0 else ""
        return (
            "%s %s java ${JAVA_OPTS} %s -cp %s/3rdparty/tla2tools.jar "
            + " tlc2.TLC %s %s %s | tee tlc.out"
        ) % (
            ctime,
            ctimeout,
            mem,
            apalache_dir,
            user_args,
            ini_params.get("more_args", ""),
            tla_filename,
        )
    else:
        print("Unknown tool: %s" % tool)
        sys.exit(1)


def setup_experiment(args, ini_params, row_num, csv_row):
    exp_dir = os.path.join(args.outDir, "exp", "%03d" % row_num)
    os.makedirs(exp_dir, exist_ok=True)
    print("Populating the directory for the experiment %d:" % row_num)
    # As SANY is only looking for file in the current directory,
    # we have to copy all tla files in the experiment directory.
    # Note that filename may contain a directory name as well, e.g., paxos/Paxos.tla
    tla_full_filename = os.path.join(args.specDir, csv_row["filename"])
    tla_dir, tla_basename = os.path.split(tla_full_filename)
    for f in os.listdir(tla_dir):
        full_path = os.path.join(tla_dir, f)
        if os.path.isfile(full_path) and (
            f.endswith(".tla") or f.endswith(".cfg") or f.endswith(".properties")
        ):
            print("  copied " + f)
            shutil.copy(full_path, exp_dir)

    # create the script to run an individual experiment
    script = os.path.join(exp_dir, "run-one.sh")
    with open(script, "w+") as sf:
        lines = [
            "#!/bin/bash",
            'D=`dirname $0` && D=`cd "$D"; pwd` && cd "$D"',
            tool_cmd(args, ini_params, exp_dir, tla_basename, csv_row),
            'exitcode="$?"',
            'echo "EXITCODE=$exitcode"',
            'exit "$exitcode"',
        ]
        for l in lines:
            sf.write(l)
            sf.write("\n")

    os.chmod(script, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
    print("  created the script " + script)
    return script


def create_master_script(args, all_scripts):
    script = os.path.join(args.outDir, "run-all.sh")
    with open(script, "w+") as sf:
        # otherwise,
        # sf.write("#!/bin/bash\n")
        for s in all_scripts:
            sf.write(s)
            sf.write("\n")

    os.chmod(script, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
    print("Run the master script " + script)
    return script


def create_parallel_script(args, master_script):
    script = os.path.join(args.outDir, "run-parallel.sh")
    with open(script, "w+") as sf:
        sf.write("#!/bin/bash\n")
        # sf.write('trap "kill -s INT 0" EXIT TERM INT\n')
        sf.write('cd "%s"\n' % args.outDir)
        mem = "--memfree %d" % args.memlimit if args.memlimit > 0 else ""
        sf.write(
            "parallel -a %s --delay 3 --results 'out/{#}/' %s \n" % (master_script, mem)
        )

    os.chmod(script, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
    print("Run the parallel script " + script)
    return script


if __name__ == "__main__":
    args = parse_options()
    if not os.path.exists(args.config):
        print("Error: File %s does not exist." % args.config)
        sys.exit(1)

    ini_params = {}
    if args.iniFile:
        if not os.path.exists(args.iniFile):
            print("Error: File %s does not exist." % args.iniFile)
            sys.exit(1)
        else:
            ini = configparser.ConfigParser()
            ini.read(args.iniFile)
            section_name = os.path.basename(args.apalacheDir)
            if section_name in ini:
                ini_params = ini[section_name]

    with open(args.config, "r") as csvfile:
        sample = csvfile.readline()
        sniffer = csv.Sniffer()
        if not sniffer.has_header(sample):
            print("The input CSV file does not have a header")
            sys.exit(1)

        dialect = sniffer.sniff(sample)
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        scripts = []
        for (row_num, row) in enumerate(reader):
            single_script = setup_experiment(args, ini_params, row_num + 1, row)
            scripts.append(single_script)

        print("\nAll experiment directories are populated\n")
        ms_script = create_master_script(args, scripts)
        create_parallel_script(args, ms_script)
