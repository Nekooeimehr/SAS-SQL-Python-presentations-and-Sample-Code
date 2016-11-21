
# Linear search 
def linear_search(Wholelist, Target):
    for (i,w) in enumerate(Wholelist):
        if Target == w:
            return i
    return -1

X = ['red', 'blue', 'yellow', 'black']
print(linear_search(X, 'blue'))
print(linear_search(X, 'brown'))


vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()

# Vocab check
def vocab_check(Vocab, Book):
    Notfind = []
    for w in Book:
        if linear_search(Vocab, w) < 0:
            Notfind.append(w)
    return (Notfind)

print(vocab_check(vocab, book_words))

# Quicksort with in-place framework
import random

def QuickSort(List, fst, lst):
    if (fst >= lst):
        return 
    pivot = List[random.randint(fst, lst)]
    i = fst
    j = lst
    while i <= j:
        while List[i] < pivot: i+=1
        while List[j] > pivot: j-=1
        if i <= j:
            List[i], List[j] = List[j], List[i]
            i = i + 1
            j = j - 1
    QuickSort(List, fst, j)
    QuickSort(List, i, lst)
    return List

List = [2,3,4,2,3,4,7,6,4,5,6,5,4,7,7,6,5,12,1,0,25]
NewList = QuickSort(List, 0, len(List)-1)

import math
# check if a number is prime or not
def isprime(A):
    if A == 2 or A==3:
        return True
    if A%2 == 0:
        return False
    if A%3 == 0:
        return False
    S = int(math.sqrt(A)) + 1
    i = 5
    w = 2
    while i < S:
        if A%i == 0:
            return False

        i+=w
        w = 6-w
    return True

print(isprime(35))


# Hash Tables
class HashTable:
    def __init__(self):
        self.arraysize = 11
        self.arrayhash = self.arraysize * [None]
    def hashcalculator(self, keys):
        sum_alphabet = 0
        for i in str(keys):
            sum_alphabet += ord(i)
        return sum_alphabet%self.arraysize
    def put(self, key, value):
        hashkey = self.hashcalculator(key)
        keyvalue = [key, value]
        if self.arrayhash[hashkey] == None:
            self.arrayhash[hashkey] = list([keyvalue])
            return True
        else:
            for pair in self.arrayhash[hashkey]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.arrayhash[hashkey].append(keyvalue)
            return True
    def get(self, key):
        hashkey = self.hashcalculator(key)
        if self.arrayhash[hashkey] is not None:
            for pair in self.arrayhash[hashkey]:
                if pair[0] == key:
                    return pair[1]
        return None

HashObj = HashTable()
HashObj.put('Nahid', 78776)
HashObj.put('Iman', 2333)
HashObj.put('ehsan', 6677)
HashObj.put('mehdi', 3343)
HashObj.put('hello', 2231)
HashObj.arrayhash
HashObj.put('yoo', 5554)
HashObj.put('fgg', 5554)
HashObj.put('come', 5554)
HashObj.put('Nahid', 5544)
HashObj.get('Iman')

# Heap Data Structure
class HeapArray:
    def __init__(self):
        self.heaparray = [0]
    def swap(self, i, j):
        self.heaparray[i], self.heaparray[j] = self.heaparray[j], self.heaparray[i]
    def Add(self, value):
        self.heaparray.append(value)
        NewArray = self.Moveup()
        return NewArray
    def Moveup(self):
        i = len(self.heaparray) - 1
        flag = 0
        while i > 1:
            if self.heaparray[i] < self.heaparray [i//2]:
                self.swap(i, i//2)
            i = i//2
        return self.heaparray
    def delete(self):
        end = len(self.heaparray) - 1
        self.heaparray[1] = self.heaparray[-1]
        del self.heaparray[-1]
        Indx = 1
        NewArray = self.movedown(Indx, end)
        return NewArray
    def movedown(self, Indx, end):
        while (Indx*2) <= end: 
            if self.heaparray[Indx] > self.heaparray [self.MinChild(Indx, end)]:
                self.swap(Indx, self.MinChild(Indx, end))
            Indx = self.MinChild(Indx, end)
    def MinChild(self, Indx, end):
        if (Indx * 2 + 1) > end:
            return Indx * 2
        else:
            if self.heaparray[Indx*2] <= self.heaparray[Indx*2+1]:
                return Indx*2
            else:
                return (Indx*2 + 1)
    def build(self, Vector):
        self.heaparray = [0] + Vector
        end = len(self.heaparray) - 1
        i = end//2
        while(i > 0):
            self.movedown(i, end)
            i -= 1
        return self.heaparray
    def sortheap(self, Vector):
        self.heaparray = self.build(Vector)
        end = len(self.heaparray) - 1 
        for i in (end, 1, -1):
            self.swap(1,i)
            self.movedown(1,i)

Heap = HeapArray()            
Heap.build([23,16,15,34,24,122,20,54,14])
#Heap.sortheap([23,18,-3,34,-15,122,56,-4,0])
        
# Dijkstra algorithm for shortest path:
# Initialization:
def Dijkstra(Graph, StartNode):
    Visited = []
    NumNodes = len(Graph)
    DList = NumNodes*[200]
    Dlist[StartNode] = 0
    Unvisited = list(set(range(NumNodes)) ^ set(Visited))
    Dlist

# DP for 0-1 Knapsack
Inputs = {1:[4,12], 2:[2,1], 3:[6,4], 4:[1,1], 5:[2,2]}
Cap = 11
def DPKnapsack(Inputs, Cap):
    DPMatrix = [[0 for i in range(Cap + 1)] for j in range(len(Inputs) + 1)]
    for i in range(1,len(Inputs)+1):
        for j in range(Cap + 1):
            if Inputs[i][0] > j:
                DPMatrix[i][j] = DPMatrix[i-1][j]
            else:
                DPMatrix[i][j] = max(DPMatrix[i-1][j], Inputs[i][1] + DPMatrix[i-1][j - Inputs[i][0]])
    MaxValue = DPMatrix[i][j]
    Sel_Items = []
    j = Cap
    for i in range(len(Inputs), 0, -1):
        
        if DPMatrix [i][j]!= DPMatrix [i-1][j]:
            Sel_Items.append(i)
            j -= Inputs[i][0]
    return(Sel_Items, MaxValue)

[Items, MaxValue]= DPKnapsack(Inputs, Cap)
print(Items, MaxValue)
                

# Prim's algorithm for finding minimum spanning tree
# Creating a random symmetric adjucency matrix
Size = 5
Adj = [[100 for i in range(Size)]for j in range(Size)]
or i in range(Size):
	for j in range(i+1,Size):
		Adj[i][j] = Adj [j][i] = random.randint(1,10)
def Prims(AdjMtx):
    Visited = []

# Merge Sort
List = [5,3,5,6,7,5,-4,6,5,8,-3]
def MergeSort(List):
    if(len(List)>1):
        Lower = List[:len(List)//2]
        Upper = List[len(List)//2:]
        MergeSort(Lower)
        MergeSort(Upper)
        i = 0
        j = 0
        l = 0 
        while j < len(Lower) and i < len(Upper):
            if Lower[j] < Upper[i]:
                List[l] = Lower[j]
                j +=1
            else:
                List[l] = Upper[i]
                i +=1
            l +=1
        while j < len(Lower):
            List[l] = Lower[j]
            j +=1
            l +=1
        while i < len(Upper):
            List[l] = Upper[i]
            i +=1
            l +=1

MergeSort(List)
        
        
# binary search
SortedList = [15,18,27,35,42,50,65]
def binarysearch(a, SortedList, start, stop):    
    if stop < start:
        return False
    else:
        mid = start + ((stop - start)//2)
        if a < SortedList[mid]:
            return binarysearch(a, SortedList, start, mid - 1)
        elif a > SortedList[mid]:
            return binarysearch(a, SortedList, mid + 1, stop)
        else:
            return mid

print(binarysearch(27, SortedList, 0, 6))


    

    




    
    
        
    










