from demo import merge_sort,quick_sort,bubble_sort
import random
import time

def randomNums(size,maxVal):
    list1=[]
    for i in range(size):
        list1.append(random.randint(1,maxVal))
    return list1
 
def function_analyzer(fun_name,arr):
    tic=time.time()
    fun_name(l)
    toc=time.time()
    second=toc-tic
    print(f"{fun_name.__name__.capitalize()}\t-> elapsed time:{second:.5f}")

size=int(input("Enter the size for the data:"))
maxVal=int(input("Enter the range:"))
l=randomNums(size,maxVal)
function_analyzer(bubble_sort,l.copy())
function_analyzer(quick_sort,l)
function_analyzer(merge_sort,l)
function_analyzer(sorted,l)
print("_"*40)
