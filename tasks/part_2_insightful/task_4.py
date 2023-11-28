
user_line = input().lower()
line1 = user_line.title()

s1 = 'camel' + (''.join(line1.split()))
s2 = 'Pascal' + (''.join(line1.split()))
s3 = 'snake' + '_' + ('_'.join(user_line.split()))

print(s1)
print(s2)
print(s3)
