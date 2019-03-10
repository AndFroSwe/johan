def user_name(name,surname):
	#outname =  surname+", "+ name 
	outname = "Lord " + name+ " of "+ surname
	return outname

def main():		
	name = input("give name: ")
	surname = input("give surname: ")
	fullname = user_name(name,surname)
	print(fullname)



main()


