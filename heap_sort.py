#! /usr/bin/python

# -*- coding: utf-8 -*-

class Heap:

    def __init__(self, size):
        self.__heap = list()
        self.__MaxSize = size

    def MaxHeapify(self, i, heapSize):
        largest = self.__heap[i]
        left = 2*i + 1
        right = 2*i + 2
        if left < self.__MaxSize and left < heapSize and self.__heap[left].value > self.__heap[i].value:
            largest = self.__heap[left]
            self.__heap[left] = self.__heap[i]
            self.__heap[i] = largest

        if right < self.__MaxSize and right < heapSize and self.__heap[right].value > self.__heap[i].value:
            largest = self.__heap[right]
            self.__heap[right] = self.__heap[i]
            self.__heap[i] = largest
        else:
            pass
        if left < self.__MaxSize and left < heapSize:
            self.MaxHeapify(left, heapSize)
        if right < self.__MaxSize and right < heapSize:
            self.MaxHeapify(right, heapSize)

    def buildMaxHeap(self, heapSize):
        for i in reversed(xrange(int(heapSize)/2)):
            self.MaxHeapify(i, heapSize)

    def heapSort(self):
        for heapSize in reversed(xrange(2, len(self.__heap)+1)):
            self.buildMaxHeap(heapSize)
            tmp = self.__heap[heapSize-1]
            self.__heap[heapSize-1] = self.__heap[0]
            self.__heap[0] = tmp

    def addNode(self, node):
        if len(self.__heap) <= self.__MaxSize:
            self.__heap.append(node)

    def printHeap(self):
        for i in self.__heap:
            print "%3d"%i.value,


class Node:
    def __init__(self, value):
        self.value = value


def main():
    MaxHeap = Heap(20)
    list = [21, 43, 54, 21, 64, 3, 53, 29, 53, 19, 23, 34, 42, 232, 439]
    for x in list:
        node = Node(x)
        MaxHeap.addNode(node)
    MaxHeap.buildMaxHeap(len(list))
    MaxHeap.printHeap()
    MaxHeap.heapSort()
    print "\n"
    MaxHeap.printHeap()

# The main program #
if __name__ == "__main__":
    main()
