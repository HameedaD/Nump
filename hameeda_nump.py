# -*- coding: utf-8 -*-
"""Hameeda_nump.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s8LcPWpRgqMprtCog2dt8XLQBQxYRfLA

11/09/2023
Hameeda

**20221BCA0314**
"""

!python --version

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

x = 3
print(x, type(x))

x = 'c'
print(x, type(x))