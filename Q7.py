def checker(list):
   ans = False
   x = list[0]
   i = 0
   for item in list:
       if (type(x) == type(item)):
           pass
       else:
           i+=1
   if i == 0:
       ans = True
   print(ans)

my_list = [1, 'ziad', 6, 10, 7, 9] #change 'ziad' to 1 to get true

checker(my_list)