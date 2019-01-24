#python2
'''
This code constructs min heap
'''

from __future__ import  print_function


class HeapBuilder:

    def __init__(self):
        self.swap_array = []
        self.heap = []


    def ReadData(self):
        n = int(input())
        self.heap = [int(s) for s in raw_input().split()]
        assert n == len(self.heap)

    def sift_down(self, i):
        c = True
        n = len(self.heap)

        while (c == True):
            l = 2*i + 1
            r = 2*i + 2

            min = i
            c = False

            if l < n and self.heap[l] < self.heap[i]:
                min = l
                c = True

            if r < n and self.heap[r] < self.heap[min]:
                min = r
                c = True

            # Swap H[i] & H[min]

            if (c == True):
                self.swap_array.append(i)
                self.swap_array.append(min)
                x = self.heap[i]
                self.heap[i] = self.heap[min]
                self.heap[min] = x
                i = min


    def min_heap(self):
        n = len(self.heap)

        for i in range(n/2, -1, -1):
            self.sift_down(i)

        print(len(self.swap_array)/2)
        for i in range(0,len(self.swap_array) - 1, 2):
            print(self.swap_array[i], self.swap_array[i+1])


    def operations(self):
        self.ReadData()
        self.min_heap()



if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.operations()
