#!/bin/bash

rm -rf _tmp
mkdir _tmp
cp -r * _tmp/
cd _tmp

python compile.py build_ext --inplace
rm nisas/core.py
rm nisas/core.c
# rm tests/integration/test_nisas.py
# rm tests/integration/test_nisas.c

pytest > test_results.txt
