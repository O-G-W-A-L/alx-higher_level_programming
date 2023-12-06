#!/usr/bin/python3

def weight_average(my_list=[]):
    average = 0
    tweight = 0
    tscore = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        tweight += weight
        tscore += score * weight
    return tscore / tweight
