thislist = ["apple", "banana", "cherry"]
print('write a number')
n = input()
while n>2 or n<0:
	print('incorrect information')
	print('Please, write number between 0 and 2')
	n=input()

print(thislist[n])


print('Do you want to change it?')
answer = (raw_input()).lower()
if answer=='yes':
	print('Ok, let\'s do it')
	print('write a new list member')
	thislist[n]=raw_input()
elif answer=='no':
	print('Ok')
	
print(thislist)