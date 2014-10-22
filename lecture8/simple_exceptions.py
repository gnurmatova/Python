def get_number():
	while (True):
		try:
			ans=input("Enter a number:")
			return int(ans)
		except:
			print("It appears that you did not enter a number!")

print(get_number())
print(get_number())



