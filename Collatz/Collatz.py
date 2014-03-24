#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (n1, n2) :
    """
    n1 is the beginning of the range, inclusive
    n2 is the end       of the range, inclusive
    return the max cycle length(max_step_counter) in the range [n1, n2]
    using a cache to optimize  calculation
    added some asserts to check condition of variables and invariant
    """
    # <your code>
    assert(n1 > 0)                      # pre-conditions check
    assert(n2 > 0)
    
    if n1 > n2:                         # switching if n1 is greater than n2
        n1,n2 = n2,n1
        
    assert(n1 <= n2)                    # pre-conditions check
        
    cache_number = 1000000              # creat a cache for 1 million numbers to save their max_cycle_length
    cache = (cache_number+1) * [-1]     # the default value of each is -1.
    max_step_counter = 0
    cache[1] = 1                        # cycle_length of 1 is 1

    for i in range(2, n2+1):            # calculate cycle length for numbers from 2 to n2
        individual_step_counter = 0     
        current_number = i              # current number in calculation
        while current_number != 1 and current_number >= i:           # if the cycle length of this number has not been calculated yet, continue the calculation
                individual_step_counter += 1                         # cycle length + 1
                if current_number%2 != 0:
                    current_number = 3*current_number + 1                    
                else: 
                    current_number = current_number//2      
        cache[i] = individual_step_counter + cache[current_number]   # save cycle length of current number
        
    assert(cache[1] == 1)               # post-conditions check
    
    max_step_counter = max(cache[n1:n2+1])
    
    assert (max_step_counter) > 0                # return-value check
    return max_step_counter

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
