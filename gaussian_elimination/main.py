import numpy as np

def gaussian_elimination(a_matrix, b_matrix):
    if (a_matrix.shape[1] != b_matrix.shape[0]):
        print("Error: rows in A is not equate column in B.")
    elif (b_matrix.shape[1] != 1) or (b_matrix.shape[0] != a_matrix.shape[0]):
        print("Error: number of columns in B does not equate to one, or A is not squared.")
    else:
        print("Accepted.")


    #creating thre augmented matrix
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis= 1)
    print("The initial augmented matrix is:\n")
    print(augmented_matrix)

    n = len(b) #num of rows
    i = 0
    k = 0

    for i in range( n - 1 ):
        if augmented_matrix[i][i] == 0:
            print("ERROR: null pivot number ",i)
            break
        else:
            for j in range(i + 1, n):
                if augmented_matrix[j][i] != 0 :
                    scalability_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                    for k in range(n+1):
                        print(augmented_matrix[j][k], augmented_matrix[i][k], scalability_factor)
                        augmented_matrix[j][k] = augmented_matrix[j][k] - augmented_matrix[i][k]*scalability_factor
                        print(augmented_matrix)


                #scalability_factor = a_matrix[j][i] / a_matrix[i][i]
                #augmented_matrix[j] = augmented_matrix[j] - (scalability_factor * augmented_matrix[i])
                #print(augmented_matrix)
                #j = j + 1




    print("Final matrix: \n")
    print(augmented_matrix)



a = np.array([[1, -1, 1],
              [2, 3, -1],
              [3, -2, -9]
              ])
b = np.array([[8],
              [-2],
              [9]
              ])

gaussian_elimination(a, b)