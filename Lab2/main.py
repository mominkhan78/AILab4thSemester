# print("    *    ")
# print("   ***   ")
# print("  *****  ")
# print(" ******* ")
# print("*********")
# print(" ******* ")
# print("  *****  ")
# print("   ***   ")
# print("    *    ")

# rows = 5  # Define the number of rows in the star

# # Iterate over each row
# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
    
#     # Print stars
#     for k in range(1, 2 * i):
#         print("*", end="")
    
#     # Move to the next line after each row is printed
#     print()

    
numArray = []
max_num = 0  

# Take input from the user and append it to the list
for i in range(3):
    num = int(input("Enter a number: "))  
    numArray.append(num)  

for i in range(3):
    print(numArray[i])
    if numArray[i] > max_num:
        max_num = numArray[i]

print("Maximum number:", max_num)


# array and list, input outputs
# sorting  of array
# shortcut for array sorting


    