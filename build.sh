#!/bin/bash

python compile.py build_ext --inplace
mv nisas/core.py nisas/old_core.txt
mv nisas/core.c nisas/old_core_c.txt

pytest

mv nisas/old_core.txt nisas/core.py
mv nisas/old_core_c.txt nisas/core.c
