def lexicographically(str_in):
    words = str_in.split()
    words.sort()
    str_out = ""
    for word in words:
        str_out = str_out + word + " "
    return str_out.strip()

input_from_user = input("Enter any string: ")
print(lexicographically(input_from_user))