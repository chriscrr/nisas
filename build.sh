#!/bin/bash

rm -rf _tmp
mkdir _tmp
cp -r * _tmp/
cd _tmp

python compile.py build_ext --inplace > compile.log
rm nisas/core.py
rm nisas/core.c
rm tests/integration/test_nisas_core.py
rm tests/integration/test_nisas_core.c

pytest -vv > test_results.txt
