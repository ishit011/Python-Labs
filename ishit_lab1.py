# Check Palindrome
def check_palindrome(checklist):
    temp_check=[]
    list_length=len(checklist)
    for i in range(list_length - 1 , -1 , -1 ):
        temp_check.append(checklist[i])
    if(temp_check==checklist):
        print(True)
    else:
       print(False)
test_list = [[0,2,3,5,7,7,0],["Red", "Blue", "Green"],[1,0,0,1,0,0,1],
             ["Red", "Yellow", "Green", "Yellow", "Red"]]

for i in test_list:
    check_palindrome(i)


# Matrix Multiplication 
def  multi_matrix(matrix1 , matrix2):
    n=len(matrix2)
    final_output=[]
    for i in range(n):
        firstlist = matrix1[i]
        secondlist = matrix2[i]
        output_list = []
        for j in range(len(secondlist)):
            product = firstlist[j] * secondlist[j]
            output_list.append(product)
        final_output.append(output_list)
    return final_output
   
print(multi_matrix(
    [[1, 2, 3, 5, 7, -7, 0], [112, 43, 17, 6, 2, 118, 11], [1024, 512, 256, 128, 64, 32, 16]], 
    [[9, 81, 75, 42, 5, -113, -1], [11, 2, -3, 0, 7, 0, 9], [8, 4, 2, 1, 0, -1, -2]]))

#Find Scalar Multiplication
def list_multiplication(n):
    value=1
    for i in n:
        value=value*i
    return value
#Test Code
print(list_multiplication([1024, 512, 256, 128, 64, 32, 16]))