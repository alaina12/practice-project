def reverse(name):
    n = ''
    for char in name:
        n = char + n
    return n
name = input(str("Enter your name: "))

if __name__ == "__main__":
    print(reverse(name))

#  def reverse(name):
#     n1 = ''
#     for char in name:
#         n1 = char + n1  # appending chars in reverse order
#     return n1

# input_str = input(str("Enter your name: "))

# if __name__ == "__main__":
    # print('Reverse String using for loop =', reverse(input_str))