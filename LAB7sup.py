def edit_distance(string_1, string_2):
    """
    This method takes two strings and computes the minimum number of insertions, deletions, and or/ replacements needed to change
    1 of the words to the other one. this is accomplished by breaking the problem down into smaller problems and saving the solutions
    to those smaller problems in a matrix. For example the value stored at matrix[3][3] will be equal to the number of changes needed to make
    the first 3 characters of each string equal to each other. This is done until the entire matrix is filled then the laste value in the matrix
    is returned. 

    Parameters:
        string_1: word 1 of 2 which is going to be compared 
                  in each of it
        string_2: word 2 of 2 which is going to be compared to the other word
    Returns:
        minimum_needed: The minimun number of insertions, deletions, and/or replacements needed to change 1 word to the other 
    """ 
    # cases where no matrix is needed       
    if string_1 == string_2:
        return 0
    if len(string_1) == 0:
        return len(string_2)
    if len(string_2) == 0:
        return len(string_1)

# creation of the matrix 
    matrix = []
    for i in range(len(string_2)+1):
        row = []
        for j in range(len(string_1)+1):
            row.append(0)
        matrix.append(row)

# population of the 1st row and 1st column
    for i in range(len(matrix)):
        matrix[i][0] = i
    for i in range(len(matrix[0])):
        matrix[0][i] = i



 # comparison of the 2 strings
    for i in range(len(string_2)):
        for j in range(len(string_1)):
            if string_2[i] == string_1[j]:
                matrix[i+1][j+1] = matrix[i][j]
            else:
                matrix[i+1][j+1] = min(matrix[i][j], matrix[i+1][j], matrix[i][j+1])+1
    

    minimum_needed= matrix[len(string_2)][len(string_1)]

    return minimum_needed
