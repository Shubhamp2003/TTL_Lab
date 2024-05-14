def remove_nth(str,n):
    str1 = str[:n]
    str2 = str[n+1:]
    return str1 + str2

str=input("Enter a string: ")
n = int(input("Enter the index where to remove: "))
print(remove_nth(str,n))