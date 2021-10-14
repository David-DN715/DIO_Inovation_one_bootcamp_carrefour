n = int(input('digite um numero\n'))
m = 1
u = 1
fib_list = []

if (n ==1) or (n ==2):
  fib_list.append(1)
else:
  for i in range(0,n):
    count = m+u
    m = count
    u = (count - u)
    fib_list.append(count)
fib_string = ' '.join(map(str, fib_list))
print(fib_string)
