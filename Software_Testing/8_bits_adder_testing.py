# SPECIFICATION:
#
# add8 emulates an 8-bit hardware adder.
# it takes 17 bits, representing two 8-bit
# numbers and a carry bit.
#
# TASK:
#
# Write test() such that it achieves 100% 
# statement coverage of the add8 function.

def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)

def split(n):
    return (n&0x1,n&0x2,n&0x4,n&0x8,n&0x10,n&0x20,n&0x40,n&0x80)

def glue(d0,d1,d2,d3,d4,d5,d6,d7,c):
    t=0
    if d0:
        t+=1
    if d1:
        t+=2
    if d2:
        t+=4
    if d3:
        t+=8
    if d4:
        t+=16
    if d5:
        t+=32
    if d6:
        t+=64
    if d7:
        t+=128
    if c:
        t+=256
    return t

def myadd(a,b):
    (a0,a1,a2,a3,a4,a5,a6,a7) = split(a)
    (b0,b1,b2,b3,b4,b5,b6,b7) = split(b)
    (s0,s1,s2,s3,s4,s5,s6,s7,c) = add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,False)
    return glue(s0,s1,s2,s3,s4,s5,s6,s7,c)

def test():
    # Write test cases that achieve 100% 
    # Statement coverage of add8. You 
    # will need to call add8 multiple 
    # times in order to do this.
    # ------exhaustive testing
    for i in range(256):
        for j in range(256):
            res = myadd(i,j)
            assert res == (i+j)
    # ------alternative simpler test:
    #myadd(0,0)
    #myadd(0,1)
    #myadd(255,255)
    
            
test()
    

