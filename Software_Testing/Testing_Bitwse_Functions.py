# TASK: Testing Bitwise Functions.
import random
def high_common_bits(a,b):
    mask = 0x8000000000000000
    output = 0
    for i in reversed(range(64)):
        if (a&mask) == (b&mask):
            output |= a&mask
        else:
            output |= mask
            return output
        mask >>= 1
    return output

def low_common_bits(a,b):
    mask = 1
    output = 0
    for i in range(64):
        if (a&mask) == (b&mask):
            output |= a&mask
        else:
            output |= mask
            return output
        mask <<= 1
    return output

##def test(a,b):
##    print("a= "+str(a)+" b= "+str(b))
##    print(high_common_bits(a,b))
##    print(low_common_bits(a,b))
##    test()
for i in range(100000):
    a = random.getrandbits(64)
    b = random.getrandbits(64)
    print(high_common_bits(a,b)+low_common_bits(a,b))




