filename = 'pi_digit.txt'
try:
    with open(filename) as file_object:
        lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()

except FileNotFoundError:
    print("File not found")

else:
    print(pi_string)
    print(len(pi_string))

