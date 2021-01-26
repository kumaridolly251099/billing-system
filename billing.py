import datetime
sum =0
while (True):
    user_input = input('enter the price of item: \n')
    user_input1 = input('enter the name of item:\n')
    print(f"{user_input}:{user_input1}")
    if user_input!='q':
        sum = sum + int(user_input)
        print(f"order total so far:{sum}")
    else: 
        print(f"your tptal bill is {sum}. thank you for visiting us")
        break
x = datetime.datetime.now()
print(x)


