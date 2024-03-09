import math

def solution(brown, yellow):
    return [round(((brown/2-2) + math.sqrt((-1*(brown/2-2))**2 -4*yellow))/2 + 2),
            round(((brown/2-2) - math.sqrt((-1*(brown/2-2))**2 -4*yellow))/2 + 2)]