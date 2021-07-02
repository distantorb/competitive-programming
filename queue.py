"""
Similar to a stack, with the difference that elements are added to the end
of the queue (enqueued) and are removed from the front of the queue (dequeued).
A queue is also known as a FIFO queue, whereas a stack is called LIFO.
"""

# Implement queue using two stacks, one stack corresponding to the head
# of the queue for extraction and the other corresponds to the tail for
# insertion. Once the head stack is empty, it is swapped with the tail 
# stack (reversed). The operator __len__ uses len(q) to recover the
# number of elements in the queue q, then "if q" can be used to test if 
# q is non-empty.


class OurQueue:
    def __init__(self):
        self.in_stack = [] # tail
        self.out_stack = [] #head

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self, obj):
        if not self.out_stack: # means head is empty
            # The in_stack is assigned to the out_stack in
            # reverse order. This is because the in_stack stores
            # elements from oldest to newest whereas the out_stack
            # needs to pop elements from newest to oldest

            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()
