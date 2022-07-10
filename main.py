"""
On n'est pas arrivé à tout faire mais voici ce que on a fait
"""
from setup import *

def main():
    m= generateMatrix(5, 4, -1, 5)
    for row in m:   
        print(row)
    m= solveMatrix(m)
    print("gain: ", trollOutcome(5, 4, -1, 5))
    
if __name__== '__main__':
    main()