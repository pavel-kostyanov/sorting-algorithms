# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:15:56 2018

@author: pavel
"""

def radix_sort(lst):
    output_list = lst[:]
    backet_list = [[] for i in range(10)]
    temp_list = []


    for i in output_list:
        last_digit = str(i)[-1]
        backet_number = int(last_digit)
        backet_list[backet_number].append(i)


    for i in range(len(backet_list)):
        if backet_list[i]:
            temp_list.extend(backet_list[i])
        else:
            continue

    backet_list = [[] for i in range(10)]
    for i in temp_list:
        try:
            last_digit = str(i)[-2]
        except IndexError:
            last_digit = 0
        backet_number = int(last_digit)
        backet_list[backet_number].append(i)
    temp_list = []
    for i in range(len(backet_list)):
        if backet_list[i]:
            temp_list.extend(backet_list[i])
        else:
            continue

    backet_list = [[] for i in range(10)]
    for i in temp_list:
        try:
            last_digit = str(i)[-3]
        except IndexError:
            last_digit = 0
        backet_number = int(last_digit)
        backet_list[backet_number].append(i)
    temp_list = []
    for i in range(len(backet_list)):
        if backet_list[i]:
            temp_list.extend(backet_list[i])
        else:
            continue

    backet_list = [[] for i in range(10)]
    for i in temp_list:
        try:
            last_digit = str(i)[-4]
        except IndexError:
            last_digit = 0
        backet_number = int(last_digit)
        backet_list[backet_number].append(i)
    temp_list = []
    for i in range(len(backet_list)):
        if backet_list[i]:
            temp_list.extend(backet_list[i])
        else:
            continue

    print(temp_list)



unsorted = [22, 135, 456, 7, 34, 987, 5674, 5, 16, 24, 1187, 125, 134, 541, 18,69, 47, 84]
radix_sort(unsorted)