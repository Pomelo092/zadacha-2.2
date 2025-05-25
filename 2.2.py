try:
   a = 2
   n = int(input())
   while n != 1:
       if n / a == n // a:
           print(a)
           n = n // a
       else:
           a += 1
except:
   print()
