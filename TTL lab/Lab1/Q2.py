def is_rotated_by(str1,str2):
    clockwise_rotate = str1[2:]+str1[:2]
    anticlockwise_rotate = str1[-2:]+str1[:-2]
    if clockwise_rotate == str2 or anticlockwise_rotate == str2:
       return True
    else:
        return False
in_str1 = input("Enter first string:")
in_str2 = input("Enter second string:")
result = is_rotated_by(in_str1,in_str2)
print("Output ->", result)