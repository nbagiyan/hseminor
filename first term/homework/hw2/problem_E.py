str = input()
if str.find('f') == str.rfind('f') and str.find('f') != -1 :
   print(-1)
elif str.find('f') == -1:
   print(-2)
else:
   for i in range(str.find('f') + 1, str.rfind('f') + 1):
      if str[i] == 'f':
         print(i)
         break
