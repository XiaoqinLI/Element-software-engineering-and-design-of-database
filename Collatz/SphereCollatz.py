import sys
from math import ceil

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

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")
    
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

def collatz_eval(n1,n2):
    """   
    n1 is the beginning of the range, inclusive
    n2 is the end       of the range, inclusive
    return the max cycle length(max_length) in the range [n1, n2]
    added some asserts to check condition of variables and invariant
    """
    assert(n1 > 0)                      # pre-conditions check
    assert(n2 > 0)
    if n1 > n2:
        n1,n2 = n2,n1
    
    max_length_Index = 0
    max_length = 0
    current_Length = 0
    
    if n1 < (ceil(n2/2)):
        for i in range(int(ceil(n2/2)), n2+1):
            current_Length = cycle_length(i)

            if (current_Length) > max_length:
                max_length_Index = i
                max_length = current_Length
    else:
        for i in range(n1, n2+1):
            current_Length = cycle_length(i)
            if (current_Length) > max_length:
                max_length_Index = i
                max_length = current_Length
    assert (max_length) > 0                # return-value check
    assert(cycle_length(1) == 1)
    assert(cycle_length(10) == 15)
    return max_length 
    
def cycle_length(i):
    """
    Return the cycle length(chainLength) of current number i
    using recursion methods together with an eager cache to optimize calculation
    """
    chainLength = 0;
    
    if (i < len(recEagerCache) and recEagerCache[i] != 0):
        return recEagerCache[i]
    
    if (i % 2 == 0):
        chainLength = 1 + cycle_length(i >> 1)
    else:
        chainLength = 1 + cycle_length((i << 1) + i + 1)

    if (i < len(recEagerCache)):
        recEagerCache[i] = chainLength
    return chainLength

def main():
    """
    this program works for both python 2.7 and python 3.3
    creat a cache for 1 million numbers to save their cycle_length
    call collatz_solve to input pairs, calculate and output the max_cycle_length in in each pair
    """
    global recEagerCache               
    cache_number = 1000000
    recEagerCache = (cache_number+1) * [0]
    recEagerCache[1] = 1
    
    collatz_solve(sys.stdin, sys.stdout)
    
main()
    
