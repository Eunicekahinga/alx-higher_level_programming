#!/usr/bin/python3
'''Solving the N queen puzzle by placing N non-attacking queens on an N×N chessboard'''
import sys

def safety(mq, nq):
    '''determines if a queen can kill'''
