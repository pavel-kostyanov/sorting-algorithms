# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:15:56 2018

@author: pavel
"""
#Codecademy version of radix sort

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0


      digit = int(digit)

      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

print(radix_sort(unsorted_list))

"""
#******************My own version***************
def radix_sort(lst):
    sorted_list = lst[:]
    backet_list = [[] for i in range(10)]
    last_digit_counter = -1
    max_digit_len = len(str(max(sorted_list)))

    while last_digit_counter != - max_digit_len + 1:
        for i in sorted_list:
            try:
                last_digit = str(i)[last_digit_counter]
            except IndexError:
                last_digit = 0
            backet_number = int(last_digit)
            backet_list[backet_number].append(i)
        sorted_list = []
        for i in range(len(backet_list)):
            if backet_list[i]:
                sorted_list.extend(backet_list[i])
            else:
                continue

        last_digit_counter += -1
        backet_list = [[] for i in range(10)]

    print(sorted_list)



unsorted = [22, 135, 456, 7, 780945, 34, 987, 5674, 5, 16, 95478, 24, 1187, 125, 134, 541, 18,69, 47, 84]
radix_sort(unsorted)


************* 1st ver.**********************

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

"""
