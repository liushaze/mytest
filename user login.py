count = 0
while count <= 2:
    if count <=2:
        user = input('your username:')
        pwd = input("your passwd:")
        if user == 'li' and pwd == "123":
            print('welcome to the room')
            break
        else:
            print('you wrong please do it again.')
            print('you have last',2-count,'chance')
    else:
        print('please try again in 5 min later.')
    count =count +1
