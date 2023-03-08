#!/usr/bin/env bash
set -euo pipefail

# This script downloads the apalache package of the given version
# and puts it in the _apalache directory for execution

VERSION=${VERSION:-''}

# The directory of this file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ROOT="$DIR"/..

if [ -z "$VERSION" ]
then
    echo "error: must supply a version, e.g., VERSION=0.0.0 ./use-apalache.sh"
    exit 1
fi

tmp_dir=$(mktemp -d -t "apalache-${VERSION}-XXXXXXXXXX")
trap 'rm -rf -- "$tmp_dir"' EXIT


if [[ "$VERSION" =~ unreleased ]]
then
    # Build from source
    cd "$tmp_dir"
    git clone https://github.com/informalsystems/apalache.git
    cd apalache
    make package
    mkdir -p "${ROOT}/_apalache"
    version=$(./script/get-version.sh)
    mv "target/universal/apalache-${version}" "${ROOT}/_apalache/apalache-${version}"

    # Save the version for use in CI
    echo "${version}" > "${ROOT}/_VERSION"
else
    # Install the release
    dst_dir="${ROOT}/_apalache/apalache-${VERSION}"
    zip_name="apalache-v${VERSION}.zip"

    cd "$tmp_dir"
    wget "https://github.com/informalsystems/apalache/releases/download/v${VERSION}/${zip_name}"
    mkdir -p "${ROOT}/_apalache"
    unzip "${zip_name}" -d "${dst_dir}"

    # Save the version for use in CI
    echo "${VERSION}" > "${ROOT}/_VERSION"
fi
