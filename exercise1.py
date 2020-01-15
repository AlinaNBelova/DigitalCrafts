# #1
# name = input('What is your name?  ')
# print(f'Hello{name}')

# #2
# name = input ('WHAT IS YOUR NAME?')
# name_caps = name.upper()
# print (f'HELLO , {name_caps}')
# print (f'YOUR NAME HAS {len(name)} LETTERS IN IT! AWESOME!')


# #3 
# name = input('What is your name?')
# subject = input('What is subject?')
# print( f'{name}\'s favorite subject in school is {subject}')

# #4
# day = int(input('Day (0-6)? '))
# if day ==0:
#     print("Sunday")
# if day ==1:
#     print("Monday")
# if day ==2:
#     print("Tuesday")
# if day ==3:
#     print("Wednesday")
# if day ==4:
#     print("Thursday")
# if day ==5:
#     print("Friday")
# if day ==6:
#     print("Saturday")

# #5
# day = int (input("day(0-6)?"))
# if  day >0 and day <= 5 :
#     print('Go to work')
# else:
#     print('Sleep in')

# #6
# C = int(input('Temperature in C? '))
# F = C*1,8 +32
# print(f'{F} F')

# #7
# bill = float(input('Total bill amount? $ '))
# service = input('Level of service: good/bad/fair? ')
# if service =='bad':
#     tip_size= 0.1
# if service =='fair':
#     tip_size = 0.15
# if service =='good':
#     tip_size= 0.2
# tip = bill*tip_size
# total = bill+tip
# print(f'tip amount: ${tip:.2f} \ntotal amount: ${total:.2f}')

# #8
# bill = float(input('Total bill amount? $ '))
# service = input('Level of service: good/bad/fair? ')
# if service =='bad':
#     tip_size= 0.1
# if service =='fair':
#     tip_size = 0.15
# if service =='good':
#     tip_size= 0.2
# tip = bill*tip_size
# total = bill+tip
# number_of_person= int(input('Split how many ways? '))
# amount_per_person = total/number_of_person
# print(f'tip amount: ${tip:.2f} \ntotal amount: ${total:.2f}\namount per person: ${amount_per_person:.2f}')

# #9
# count =0
# while count<10:
#     count +=1
#     print (count)

#10
coins =0
print (f'You have {coins} coins')
want_coin ='yes'
while want_coin =='yes':
    coins +=1
    want_coin = input('Want coin? yes/no.')
    print (f'You have {coins}  coins.')
print('bye')
