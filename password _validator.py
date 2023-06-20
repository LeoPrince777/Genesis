pword = input()
#if len(pword) >= 8 and re.match('[a-zA-Z0-9]', pword):
#print('Yes')

if any(char.isalnum() for char in pword) and len(pword) >= 8:
  print("Yes")
if any(char.isalpha() for char in pword) and len(pword) >= 8:
  print("No")
if any(char.isdigit() for char in pword) and len(pword) >= 8:
  print("No")
else:
  print("yes")