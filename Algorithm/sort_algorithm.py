#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Chenfeng Zhu
#

import math
import random


def generate_array(size = 10, start = 1, end = 10):
    arr = []
    for x in range(0, size):
        arr.append(random.randint(start, end))
    return arr


# Insertion Sort:
# - Best:  n
# - Avg:   n^2
# - Worst: n^2
# - Memory: 1
# - Stable: yes
def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i
        while j > 0 and tmp < arr[j-1]:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = tmp


# Shell Sort:
# - Best:  n*log(n)
# - Avg:   depends on gap sequence
# - Worst: depends on gap sequence
# - Memory: 1
# - Stable: no
def shell_sort(arr):
    gap = int(len(arr) / 2)
    while gap > 0:
        for i in range(gap, len(arr)):
            tmp = arr[i]
            j = i
            while j >= gap and tmp < arr[j-gap]:
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = tmp
        gap = int(gap / 2)


# Heapsort
# - Best:  n*log(n)
# - Avg:   n*log(n)
# - Worst: n*log(n)
# - Memory: 1
# - Stable: no
def heapify(arr, idx, size):
    tmp = arr[idx]
    while 2 * idx + 1 < size:
        child = 2 * idx + 1
        if child != size - 1 and arr[child] < arr[child+1]:
            child = child + 1
        if tmp < arr[child]:
            arr[idx] = arr[child]
        else:
            break
        idx = child
    arr[idx] = tmp


def heap_sort(arr):
    n = len(arr)
    for i in range(int(n/2), -1, -1):
        heapify(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)


# Mergesort
# - Best:  n*log(n)
# - Avg:   n*log(n)
# - Worst: n*log(n)
# - Memory: n
# - Stable: yes
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        array_left = arr[:mid]
        array_right = arr[mid:]

        merge_sort(array_left)
        merge_sort(array_right)

        i, j, k = 0, 0, 0

        while i < len(array_left) and j < len(array_right):
            if array_left[i] < array_right[j]:
                arr[k] = array_left[i]
                i = i + 1
            else:
                arr[k] = array_right[j]
                j = j + 1
            k = k + 1

        while i < len(array_left):
            arr[k] = array_left[i]
            i = i + 1
            k = k + 1

        while j < len(array_right):
            arr[k] = array_right[j]
            j = j + 1
            k = k + 1


# Mergesort
# - Best:  n*log(n)
# - Avg:   n*log(n)
# - Worst: n^2
# - Memory: log(n)
# - Stable: both no and yes
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


# Bucket sort
# - Best:  n + m
# - Avg:   n + m
# - Worst: n^2
# - Memory: n + m
# - Stable: yes
def bucket_sort(arr):
    min = arr[0]
    max = arr[0]
    bucket_size = 20
    temp_arr = []

    # Find the low and high bound:
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]

    bucket_num = math.floor((max - min) / bucket_size) + 1
    buckets = []
    for i in range(0, bucket_num):
        buckets.append([])

    for i in range(0, len(arr)):
        idx = math.floor((arr[i] - min) / bucket_size)
        buckets[idx].append(arr[i])

    for i in range(0, len(buckets)):
        insertion_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            temp_arr.append(buckets[i][j])

    return temp_arr


# Bubble sort
# - Best:  n
# - Avg:   n^2
# - Worst: n^2
# - Memory: 1
# - Stable: yes
def bubble_sort(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Selection sort
# - Best:  n^2
# - Avg:   n^2
# - Worst: n^2
# - Memory: 1
# - Stable: No
def selection_sort(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def run_generate():
    pass
    # print(generate_array())
    # print(generate_array(10, 1, 100))
    # print(generate_array(size = 5))


def run_sort():
    test_array = generate_array(10, 1, 100)
    print("Original array:", test_array)

    array_insertion = test_array.copy()
    insertion_sort(array_insertion)
    print("Insertion sort:", array_insertion)

    array_shell = test_array.copy()
    shell_sort(array_shell)
    print("Shell sort    :", array_shell)

    array_heap = test_array.copy()
    heap_sort(array_heap)
    print("Heap sort     :", array_heap)

    array_merge = test_array.copy()
    merge_sort(array_merge)
    print("Merge sort    :", array_merge)

    array_quick = test_array.copy()
    quick_sort(array_quick, 0, len(array_quick)-1)
    print("Quick sort    :", array_quick)

    array_bucket = bucket_sort(test_array.copy())
    print("Bucket sort   :", array_bucket)

    array_bubble = test_array.copy()
    bubble_sort(array_bubble)
    print("Bubble sort   :", array_bubble)

    array_selection = test_array.copy()
    selection_sort(array_selection)
    print("Selection sort:", array_selection)


if __name__ == '__main__':
    run_sort()
