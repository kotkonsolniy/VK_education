input_string = input().strip()
lower_string = input_string.lower()

chars_to_replace = {'!', '%', '#', '@'}
replaced_count = 0
result_string = []

for char in lower_string:
    if char in chars_to_replace:
        replaced_count += 1
    else:
        result_string.append(char)

result_string = ''.join(result_string)

print(replaced_count)
print(result_string)