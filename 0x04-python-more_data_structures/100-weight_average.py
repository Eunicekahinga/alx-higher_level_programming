#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    t_score = t_weight = 0

    for score, weight in my_list:
        t_score += score * weight
        t_weight += weight

    if t_weight == 0:
        return 0

    average = t_score / t_weight

    return average
