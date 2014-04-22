# TASK: Random Testing
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion, like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

import array
import random

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

# Write a random tester for the Queue class.
def test():
    N = 1000
    add = 0
    remove = 0
    addFull = 0
    removeEmpty = 0
    q = Queue(N)
    q.checkRep()
    l = []
    # adding bias and testing much bigger queue
    for x in range(20):
        bias = 0.2
        if x%2 == 1:
            bias = - 0.2
        for i in range(10000):
            if(random.random() < 0.5 + bias):
                z = random.randint(0,1000000)
                res = q.enqueue(z)
                q.checkRep()
                if res:
                    l.append(z)
                    add +=1
                else:
                    assert len(l) == N
                    assert q.full()
                    q.checkRep()
                    addFull += 1
            else:
                z= q.dequeue()
                q.checkRep()
                if z is  None:
                    assert len(l) == 0
                    assert q.empty()
                    q.checkRep()
                    removeEmpty += 1
                else:
                    expected_value = l.pop(0)
                    assert z == expected_value
                    remove += 1
    while True:
        res = q.dequeue()
        q.checkRep()
        if res is None:
            break;
        z = l.pop(0)
        assert res == z
    assert len(l) == 0         
    print("number of add: ", add)
    print("number of remove: ", remove)
    print("number of addFull: ", addFull)
    print("number of removeEmpty: ", removeEmpty)
test()

