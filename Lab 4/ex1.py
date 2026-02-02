# string manipulation examples 

# 1 concantation operator 

first = input("Enter your first name: ")
middleIn = input("Enter your middle initial: ")
last = input("Enter your last name: ")

fullName = first + " " + middleIn + ". " + last
print("Your full name is:", fullName)

# 2 f string 

print(f"Your full name is: {first} {middleIn}. {last}")

# 3 operator 
fullName = "%s %s. %s" % (first, middleIn, last)
print("Your full name is:", fullName)

# 4 format
fullName = "{} {}. {}".format(first, middleIn, last)
print("Your full name is", fullName)

# 5 join()
name_list = [first, middleIn + ".", last]
fullName = " ".join(name_list)
print("Your full name is:", fullName)

# 6 format () but unpacking the list
fullName = "{0} {1} {2}".format(*name_list)
print("Your full name is:", fullName)
