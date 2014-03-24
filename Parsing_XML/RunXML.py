#!/usr/bin/env python3

# ------------------------------
# project 2/XML/RunXML.py
# Author: Xiaoqin LI Roberto Salinas
# Description: 1000 lines of accecptance tests in total, including random tests and some corner tests.
# -------------------------------

"""
To run the program
    % python3 RunXML.py < anc2275-RunXML.in > anc2275.out
    % python3 RunXML.py < hkt984-RunXML.in > hkt984.out
    % python3 RunXML.py < kenon-RunXML.in > kenon.out
    % python3 RunXML.py < yj2946-RunXML.in > yj2946.out
    % python3 RunXML.py < yj2946-RunXML.in > wigu.out
    % chmod ugo+x RunCollatz.py
    % python3 RunXML.py < RunXML.in > RunXML.out

To document the program
    % pydoc -w XML
"""

# -------
# imports
# -------

import sys
import XML 

#--------Main fuction---------
def main():
    XML.xmlSolve(sys.stdin, sys.stdout)
#-----------------------------
    
main()


