#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# updated by Xiaoqin LI
# Description: 1002 tests in total, including random (in range of (1,10000))
#                   pairs tests and some corner tests.
#                   Combined collatz_solve and main tegether in SphereCollatz.
# -------------------------------

"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

from SphereCollatz import main 

# ----
main()
# ----


#collatz_solve(sys.stdin, sys.stdout)
