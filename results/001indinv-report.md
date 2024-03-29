# Results of 001indinv-apalache


## 1. Awesome plots

### 1.1. Time (logarithmic scale)

![time-log](001indinv-apalache-time-log.svg "Time Log")

### 1.2. Time (linear)

![time-log](001indinv-apalache-time.svg "Time Log")

### 1.3. Memory (logarithmic scale)

![mem-log](001indinv-apalache-mem-log.svg "Memory Log")

### 1.4. Memory (linear)

![mem](001indinv-apalache-mem.svg "Memory Log")

### 1.5. Number of arena cells (linear)

![ncells](001indinv-apalache-ncells.svg "Number of arena cells")

### 1.6. Number of SMT clauses (linear)

![nclauses](001indinv-apalache-nclauses.svg "Number of SMT clauses")

## 2. Input parameters

no  |  filename                          |  tool      |  timeout  |  init                   |  inv                    |  next  |  args
----|------------------------------------|------------|-----------|-------------------------|-------------------------|--------|--------------------------------
1   |  Bakery-Boulangerie/APABakery.tla  |  apalache  |  1h       |  Init                   |  Inv                    |        |  --length=0
2   |  Bakery-Boulangerie/APABakery.tla  |  apalache  |  1h       |  Inv                    |  Inv                    |        |  --length=1
3   |  ewd840/APAEWD840.tla              |  apalache  |  3h       |                         |  InvAndTypeOK           |        |  --length=0 --cinit=ConstInit10
4   |  ewd840/APAEWD840.tla              |  apalache  |  3h       |  InvAndTypeOK           |  InvAndTypeOK           |        |  --length=1 --cinit=ConstInit10
5   |  bcastByz/APAbcastByz.tla          |  apalache  |  3h       |  InitNoBcast            |  IndInv_Unforg_NoBcast  |        |  --length=0 --cinit=ConstInit4
6   |  bcastByz/APAbcastByz.tla          |  apalache  |  3h       |  IndInv_Unforg_NoBcast  |  IndInv_Unforg_NoBcast  |        |  --length=1 --cinit=ConstInit4
7   |  two-phase/APATwoPhase.tla         |  apalache  |  23h      |                         |  Inv                    |        |  --length=0 --cinit=ConstInit7
8   |  two-phase/APATwoPhase.tla         |  apalache  |  23h      |  InitInv                |  Inv                    |        |  --length=1 --cinit=ConstInit7

## 3. Detailed results: 001indinv-apalache-0.19.2.csv

01:no  |  02:tool   |  03:status  |  04:time_sec  |  05:depth  |  05:mem_kb  |  10:ninit_trans  |  11:ninit_trans  |  12:ncells  |  13:nclauses  |  14:navg_clause_len
-------|------------|-------------|---------------|------------|-------------|------------------|------------------|-------------|---------------|--------------------
1      |  apalache  |  NoError    |  13s          |  0         |  479MB      |  0               |  0               |  549        |  1.0K         |  10
2      |  apalache  |  NoError    |  1m01s        |  0         |  961MB      |  0               |  0               |  14K        |  36K          |  17
3      |  apalache  |  NoError    |  8s           |  0         |  275MB      |  0               |  0               |  805        |  2.0K         |  18
4      |  apalache  |  NoError    |  14s          |  0         |  415MB      |  0               |  0               |  3.0K       |  15K          |  18
5      |  apalache  |  NoError    |  8s           |  0         |  298MB      |  0               |  0               |  150        |  186          |  11
6      |  apalache  |  NoError    |  9s           |  0         |  310MB      |  0               |  0               |  734        |  1.0K         |  19
7      |  apalache  |  NoError    |  8s           |  0         |  275MB      |  0               |  0               |  369        |  2.0K         |  6.0
8      |  apalache  |  NoError    |  14s          |  0         |  414MB      |  0               |  0               |  3.0K       |  9.0K         |  18

## 4. Detailed results: 001indinv-apalache-0.5.2.csv

01:no  |  02:tool   |  03:status  |  04:time_sec  |  05:depth  |  05:mem_kb  |  10:ninit_trans  |  11:ninit_trans  |  12:ncells  |  13:nclauses  |  14:navg_clause_len
-------|------------|-------------|---------------|------------|-------------|------------------|------------------|-------------|---------------|--------------------
1      |  apalache  |  NoError    |  3s           |  0         |  285MB      |  1               |  16              |  712        |  2.0K         |  10
2      |  apalache  |  NoError    |  2m02s        |  1         |  638MB      |  1               |  16              |  25K        |  131K         |  14
3      |  apalache  |  NoError    |  4s           |  0         |  261MB      |  1               |  4               |  1.0K       |  6.0K         |  11
4      |  apalache  |  NoError    |  8s           |  1         |  329MB      |  1               |  4               |  5.0K       |  36K          |  12
5      |  apalache  |  NoError    |  3s           |  0         |  215MB      |  1               |  5               |  126        |  198          |  8.0
6      |  apalache  |  NoError    |  5s           |  1         |  297MB      |  1               |  5               |  1.0K       |  10K          |  14
7      |  apalache  |  NoError    |  3s           |  0         |  224MB      |  1               |  7               |  260        |  1.0K         |  5.0
8      |  apalache  |  NoError    |  6s           |  1         |  311MB      |  1               |  7               |  4.0K       |  23K          |  13

## 5. Detailed results: 001indinv-apalache-0.7.0.csv

01:no  |  02:tool   |  03:status  |  04:time_sec  |  05:depth  |  05:mem_kb  |  10:ninit_trans  |  11:ninit_trans  |  12:ncells  |  13:nclauses  |  14:navg_clause_len
-------|------------|-------------|---------------|------------|-------------|------------------|------------------|-------------|---------------|--------------------
1      |  apalache  |  NoError    |  4s           |  0         |  305MB      |  0               |  0               |  585        |  1.0K         |  9.0
2      |  apalache  |  NoError    |  46s          |  1         |  673MB      |  0               |  0               |  21K        |  99K          |  13
3      |  apalache  |  NoError    |  4s           |  0         |  297MB      |  0               |  0               |  1.0K       |  5.0K         |  12
4      |  apalache  |  NoError    |  9s           |  1         |  356MB      |  0               |  0               |  5.0K       |  34K          |  12
5      |  apalache  |  NoError    |  4s           |  0         |  288MB      |  0               |  0               |  141        |  296          |  9.0
6      |  apalache  |  Error      |  4s           |  0         |  284MB      |  0               |  0               |  26         |  48           |  7.0
7      |  apalache  |  NoError    |  4s           |  0         |  299MB      |  0               |  0               |  364        |  2.0K         |  6.0
8      |  apalache  |  NoError    |  7s           |  1         |  329MB      |  0               |  0               |  4.0K       |  23K          |  13

## 6. Detailed results: 001indinv-apalache-0.16.0.csv

01:no  |  02:tool   |  03:status  |  04:time_sec  |  05:depth  |  05:mem_kb  |  10:ninit_trans  |  11:ninit_trans  |  12:ncells  |  13:nclauses  |  14:navg_clause_len
-------|------------|-------------|---------------|------------|-------------|------------------|------------------|-------------|---------------|--------------------
1      |  apalache  |  NoError    |  13s          |  0         |  512MB      |  0               |  0               |  549        |  1.0K         |  10
2      |  apalache  |  NoError    |  41s          |  0         |  772MB      |  0               |  0               |  14K        |  37K          |  17
3      |  apalache  |  NoError    |  7s           |  0         |  283MB      |  0               |  0               |  805        |  2.0K         |  17
4      |  apalache  |  NoError    |  10s          |  0         |  332MB      |  0               |  0               |  3.0K       |  15K          |  18
5      |  apalache  |  NoError    |  8s           |  0         |  270MB      |  0               |  0               |  138        |  184          |  11
6      |  apalache  |  NoError    |  8s           |  0         |  306MB      |  0               |  0               |  614        |  1.0K         |  16
7      |  apalache  |  NoError    |  7s           |  0         |  301MB      |  0               |  0               |  369        |  2.0K         |  6.0
8      |  apalache  |  NoError    |  10s          |  0         |  422MB      |  0               |  0               |  3.0K       |  10K          |  18

## 7. Detailed results: 001indinv-apalache-0.6.0.csv

01:no  |  02:tool   |  03:status  |  04:time_sec  |  05:depth  |  05:mem_kb  |  10:ninit_trans  |  11:ninit_trans  |  12:ncells  |  13:nclauses  |  14:navg_clause_len
-------|------------|-------------|---------------|------------|-------------|------------------|------------------|-------------|---------------|--------------------
1      |  apalache  |  NoError    |  4s           |  0         |  312MB      |  0               |  0               |  585        |  1.0K         |  8.0
2      |  apalache  |  NoError    |  46s          |  1         |  607MB      |  0               |  0               |  21K        |  99K          |  13
3      |  apalache  |  NoError    |  4s           |  0         |  310MB      |  0               |  0               |  842        |  3.0K         |  10
4      |  apalache  |  NoError    |  7s           |  1         |  314MB      |  0               |  0               |  3.0K       |  21K          |  12
5      |  apalache  |  NoError    |  4s           |  0         |  278MB      |  0               |  0               |  141        |  296          |  8.0
6      |  apalache  |  NoError    |  4s           |  1         |  290MB      |  0               |  0               |  657        |  2.0K         |  13
7      |  apalache  |  NoError    |  4s           |  0         |  296MB      |  0               |  0               |  364        |  2.0K         |  6.0
8      |  apalache  |  NoError    |  7s           |  1         |  327MB      |  0               |  0               |  4.0K       |  23K          |  13

## 8. Detailed results: 001indinv-apalache-0.9.0.csv

01:no  |  02:tool   |  03:status  |  04:time_sec  |  05:depth  |  05:mem_kb  |  10:ninit_trans  |  11:ninit_trans  |  12:ncells  |  13:nclauses  |  14:navg_clause_len
-------|------------|-------------|---------------|------------|-------------|------------------|------------------|-------------|---------------|--------------------
1      |  apalache  |  NoError    |  6s           |  0         |  283MB      |  0               |  0               |  56         |  38           |  7.0
2      |  apalache  |  NoError    |  1m01s        |  0         |  507MB      |  0               |  0               |  18K        |  47K          |  17
3      |  apalache  |  NoError    |  8s           |  0         |  264MB      |  0               |  0               |  213        |  297          |  12
4      |  apalache  |  NoError    |  9s           |  0         |  287MB      |  0               |  0               |  3.0K       |  13K          |  18
5      |  apalache  |  NoError    |  6s           |  0         |  221MB      |  0               |  0               |  72         |  88           |  10
6      |  apalache  |  NoError    |  7s           |  0         |  237MB      |  0               |  0               |  729        |  1.0K         |  16
7      |  apalache  |  NoError    |  6s           |  0         |  218MB      |  0               |  0               |  27         |  74           |  4.0
8      |  apalache  |  NoError    |  9s           |  0         |  301MB      |  0               |  0               |  3.0K       |  9.0K         |  18
