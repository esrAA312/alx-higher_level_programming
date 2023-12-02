#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    olist = my_list[:]
    for y, i in enumerate(my_list):
        if i % 2 == 0:
            olist[y] = True
        else:
            olist[y] = False
    return (olist)
