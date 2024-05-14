def swap_and_concatenate(str1, str2):
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]

    result = swapped_str1 + ' ' + swapped_str2
    return result

str1 = input("Enter first string:")
str2 = input("Enter second string:")

result = swap_and_concatenate(str1, str2)
print("Result: ", result)
