#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# updated by Xiaoqin LI
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import io
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# ----------------------
# TestCollatz
# 23 unit tests in total
# ----------------------

class TestCollatz (unittest.TestCase) :
    # ---------------------------------------
    # collatz_read fuction test, 4 in total
    # ---------------------------------------

    def test_read_1 (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_2 (self) :
        r = io.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  100)
        self.assertTrue(j == 200)

    def test_read_3 (self) :
        r = io.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  900)
        self.assertTrue(j == 1000)
        
    def test_read_4 (self) :
        r = io.StringIO("1000 900\n")   
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1000)
        self.assertTrue(j == 900)

    # ---------------------------------------
    # collatz_eval fuction test, 7 in total
    # ---------------------------------------

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)
      
    def test_eval_5(self):
        v = collatz_eval(1, 1000000)     #full range    
        self.assertTrue(v == 525)
       	
    def test_eval_6(self):
        v = collatz_eval(1000, 900)      #reverse order
        self.assertTrue(v == 174)
     
    def test_eval_7(self):
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1)          #same number


    # --------------------------------------
    # collatz_print fuction test, 7 in total
    # --------------------------------------

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 100, 200, 125)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 900, 1000, 174)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "900 1000 174\n")
        
    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 5000, 6000, 236)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "5000 6000 236\n")

    def test_print_5 (self) :  # corner test
        w = io.StringIO()
        collatz_print(w, 1, 1, 1)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "1 1 1\n")

    def test_print_6 (self) :  # corner test
        w = io.StringIO()
        collatz_print(w, 1, 1000000, 525)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "1 1000000 525\n")

    def test_print_7 (self) :  # reverse order
        w = io.StringIO()
        collatz_print(w, 1000, 900, 174)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "1000 900 174\n")
    

    # ---------------------------------------
    # collatz_solve fuction test, 5 in total
    # ---------------------------------------

    def test_solve_1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2(self) :
        r = io.StringIO("200 300\n300 400\n400 500\n500 600\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "200 300 128\n300 400 144\n400 500 142\n500 600 137\n")

    def test_sovle_3(self) :
        r = io.StringIO("1000 2000\n2000 3000\n3000 4000\n4000 5000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1000 2000 182\n2000 3000 217\n3000 4000 238\n4000 5000 215\n")
    def test_sovle_4(self) :
        r = io.StringIO("1000 2000\n2000 3000\n3000 4000\n4000 5000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1000 2000 182\n2000 3000 217\n3000 4000 238\n4000 5000 215\n")
    def test_sovle_5(self) :
        r = io.StringIO("2000 1000\n3000 2000\n4000 3000\n5000 4000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "2000 1000 182\n3000 2000 217\n4000 3000 238\n5000 4000 215\n")
        print("Done.")

# ----
# main
# ----

print("TestCollatz.py")
print()
unittest.main()


