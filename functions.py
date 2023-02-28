import matplotlib.pyplot as plt
import numpy as np
import scipy
import math


def lin(x):
    return x


def quartic(x):
    return x**4


def quart_prime(x):
    return 4 * (x **3)


def factorial(x):
    return scipy.special.factorial(x)


def r_factorial(x):
    x_list = x.tolist()
    x_copy = x_list.copy()
    idx = 0
    for num in x_list:
        x_copy[idx] = rfac_help(x_list[idx])
        idx += 1
    
    return x_copy

        
def rfac_help(num):
    if num < 1:
        return 1
    return num * rfac_help(num-1)


def r_factorial_prime(x):
    x_list = x.tolist()
    x_copy = x_list.copy()
    idx = 0
    for num in x_list:
        x_copy[idx] = rfac_prime_help(x_list[idx])
        idx += 1
    
    return x_copy


def rfac_prime_help(num):
    if num <= 1:
        return 1
    
    whole = int(num // 1)
    
    list_a = []
    for i in range(whole):
        list_a.append(num-i)
    
    broken_list_a = two_split(list_a) #appending the lists in this list together makes list_a
    
    derivative_terms = []
    
    for small_list in broken_list_a:
        assert len(small_list) == 1 or len(small_list) == 2
        term = "q"
        if len(small_list) == 1:
            term = rfac_help(num) / small_list[0]
            
        if len(small_list) == 2:
            term = rfac_help(num) * (small_list[0] + small_list[1]) / (small_list[0] * small_list[1])
        
        derivative_terms.append(term)
    
    derivative_sum = 0
    for term in derivative_terms:
        derivative_sum += term

    return derivative_sum


def two_split(list_a):
    num = len(list_a)
    if num <= 2:
        list_of_lists = []
        list_of_lists.append(list_a)
        return(list_of_lists)
        print(list_of_lists)
    half_idx = int(num / 2)
    half1, half2 = list_a[:half_idx], list_a[half_idx:]
    return two_split(half1) + two_split(half2)


def num_derivative(x_list, y_list):
    y_prime = np.diff(y_list)/np.diff(x_list)
    x_prime = []
    for i in range(len(y_prime)):
        temp = (x_list[i+1] + x_list[i])/2
        x_prime = np.append(x_prime, temp)
    return x_prime, y_prime
