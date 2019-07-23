logins=['jacobs','ultor','vasya']
passwords=['1234','killredfaction','ye blya']



n=(-1)
check=0
answer='no'

#checking your login and password
while check!=1:
    print('Login')
    login = (raw_input()).lower()
    print('Password')
    password = (raw_input()).lower()
    if (login in logins) and (password in passwords):
        print('Welcome ' + str(login))
        check += 1
        break
    else:
        print('')
        print('Error')
    print('')
	
    print('Do you want to try again?')

#Checking if you want to try again
    while check!=1:
		answer=(raw_input()).lower()
		if (answer == 'no'):
			check += 1
		elif (answer == 'yes'):
			print('Ok, let\'s try again')
			print('')
			break
		else:
			print('Could you repeat?')