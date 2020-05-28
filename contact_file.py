import os
import pickle
import contact
import names

def contact_file():
	print("CONTACT BOOK\n")

	menu = {}
	menu["1"] = "View list of contacts"
	menu["2"] = "Add contact"
	menu["3"] = "Change contact"
	menu["4"] = "Delete contact"
	menu["5"] = "Search for contact"
	menu["6"] = "Delete all contacts"
	menu["7"] = "Add random contacts"
	menu["8"] = "Exit"

	for k,v in menu.items():
		print("{}) {}".format(k,v))

	file_name = "Contact_Book"
	user_input = input()

	if(user_input == "1"):
		os.system("clear")
		print("CONTACT BOOK")
		print("Enter any key to exit\n")
		
		infile = open(file_name, "rb")
		contact_list = pickle.load(infile)
		i=1
		print("----------------------------------------------------------------------------")
		for con in contact_list:
			print("{}    {} {} {} {} {}".format(i, con.first_name, con.last_name, con.phone_number, con.birthday, con.address))
			print("----------------------------------------------------------------------------")
			i += 1

		user_input = input()
		if(user_input == 0):
			os.system("clear")
			contact_file()
		else:
			os.system("clear")
			contact_file()
		
	elif(user_input == "2"):
		os.system("clear")
		print("CREATE NEW CONTACT\n")
		print("Enter '_SKIP' for any field to skip\n")
		print("Enter '_EXIT' to exit\n")

		first_name = input("Enter contact's first name\n")
		last_name = input("Enter contact's last name\n")
		phone_number = input("Enter contact's phone number\n")
		birthday = input("Enter contact's birthday in from off XX/XX/XXX\n")
		address = input("Enter user's address\n")

		new_contact = contact.Contact(first_name, last_name, phone_number, birthday, address)

		infile = open(file_name, "rb")
		contact_list = pickle.load(infile)
		contact_list.append(new_contact)
		infile.close()

		outfile = open(file_name, "wb")
		pickle.dump(contact_list, outfile)
		outfile.close()

		os.system("clear")
		print("Contact successfully added\n")
		contact_file()		
		
	elif(user_input == "3"):
		os.system("clear")
		print("ADD NEW CONTACT\n")
	elif(user_input == "4"):
		os.system("clear")
		print("DELETE CONTACT\n")

	elif(user_input == "5"):
		os.system("clear")
		print("SEARCH FOR CONACT\n")

	elif(user_input == "6"):
		os.system("clear")
		print("DELETE ALL CONTACTS\n")
		#add check that they are sure they want to delete all contacts
		
		print("Are you sure you want to delete all contacts? This cannot be undone.\n")
		print("1) Yes\n")
		print("2) No\n")

		user_input = input()
		if user_input == "1":
			outfile = open(file_name, "wb")
			pickle.dump([], outfile)
			outfile.close()
		elif user_input == "2":
			os.system("clear")
			print(">>>>>Action Cancelled\n")
			contact_file()	
		else:
			os.system("clear")
			print(">>>>>ERROR 492: Invalid Input\n")
			contact_file()		
		
	elif(user_input == "7"):
		os.system("clear")
		print("ADDING RANDOM CONTACTS TO CONTACT BOOK\n")

		user_input = int(input("How many random contacts do you want to add?\n"))
		infile = open(file_name, "rb")
		contact_list = pickle.load(infile)
		infile.close()

		outfile = open(file_name, "wb")		

		for i in range(user_input):
			rand_f_name = names.get_first_name()
			rand_l_name = names.get_last_name()
			rand_p_number = 4448889999
			rand_birthday = "00/11/2222"
			new_contact = contact.Contact(rand_f_name, rand_l_name, rand_p_number, rand_birthday, "NA")
			contact_list.append(new_contact)
		pickle.dump(contact_list, outfile)
		outfile.close()

		os.system("clear")
		print("Successfully added {} contacts".format(user_input))
		contact_file()
			
	elif(user_input == "8"):
		os.system("clear")

	else:
		os.system("clear")
		print(">>>>>ERROR 001: Invalid Input\n")
		contact_file()

