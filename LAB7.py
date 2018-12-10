"""
CS 2302
Emilio Ramirez
Lab 7 B
Diego Aguirre,  Manoj Saha
Last Date Modified: December 9th, 2018
Purpose:  Implement Dynamic programing algortithm for Edit Distance
"""
from LAB7sup import edit_distance

def main():
    print(" Testing edit distance method on words, \"miners\" and \"money \" ")
    print(" The minimun number of changes needed for the words to match is", edit_distance("miners","money"))

main()