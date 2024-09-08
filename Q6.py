#This code is interactive and has the answers for the four questions in question 6

person = {'fisrt_name': 'Asabeneh',
          'last_name' : 'Yetayeh',
          'age' : 250,
          'country' : 'Finland',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
              'street' : 'Space street',
              'zipcode' : '02210'
          }
          }

if 'skills' in person:
     x = int(input('Enter 1 for first question & 2 for second: '))
     list = person['skills']
     if x == 1:
         index = len(list)//2
         mid_skill = list[index]
         print(mid_skill)
     elif x == 2:
         if 'Python' in list:
             print("Yes Python is in the skills")
         else:
             print("Python not found")
     elif x == 3: #he has all the skills mentioned BTW 
         if 'React' and 'Node' and 'MongoDB' in list:
             print('He is a fullstack developer')
         elif  'Node' and 'Python' and 'MongoDB' in list:
             print("He is a backend developer")
         elif 'JavaScript' and 'React' in list:
             print("He is a front end developer")    
         else:
             print("unkown title")
     elif x == 4: 
         married = person['is_married']
         country = person['country']
         f_name = person['fisrt_name']
         l_name = person['last_name']
         if married and 'Finland' in country:
             print(f_name + " " + l_name + " lives in Finland. He is married")
     else:
         print('\033[91m'+"Error undefined input" + '\033[0m') #used coloring code from the table (RED)      
else:
    print("not found")