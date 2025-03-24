def is_correct_string(s):

    has_a_or_o = 'a' in s or 'o' in s

    has_no_i_and_e = 'i' not in s and 'e' not in s


    return has_a_or_o and has_no_i_and_e



input_string = input("Введите строку: ")


if is_correct_string(input_string):
    print("True")
else:
    print("False")