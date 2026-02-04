#Write a function that takes two arguments, 145 and 'o'and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.

def format_number(num, rep):
    return format(num, rep)

# Call the function
result = format_number(145, 'o')

# Print the result
print(result)