def reverse_words(input_str):
    words = input_str.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

input_str = input("Enter the string to reverse: ")
output_str = reverse_words(input_str)

print("Output →", output_str)
