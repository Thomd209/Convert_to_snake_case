def convert_to_snake_case(s):
    snake_case = ''
    for i in range(len(s)):
        if i == len(s) - 1:
            snake_case += s[i]
            continue

        if s[i + 1].isupper() and s[i + 1].isalpha():
            snake_case += s[i] + '_'
        else:
            snake_case += s[i]

    snake_case = snake_case.lower()

    return snake_case


camel_case = input()
result = convert_to_snake_case(camel_case)
print(result)
