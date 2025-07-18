str1=str(input('Enter the String = '))
output = ''
for i in str1:
    if ord(i) > 96:
        output+= i.upper()

    else:
        output+= i.lower()

print(output)
print(output.isalnum())