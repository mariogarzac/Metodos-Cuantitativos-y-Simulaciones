#!/usr/bin/python3

# Mario Garza Chapa
# Juan Pablo González
# Michel Antoine Dionne

import chi 
import rachas
import LCG

def main():

    LCG.runTests()
    chi.chiSquaredTest()
    rachas.runsTest()

if __name__ == "__main__":
    main()