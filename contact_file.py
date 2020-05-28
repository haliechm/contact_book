import os
import pickle
import contact
import names

from random import randint

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
		phone_number = input("Enter contact's phone number in form of (XXX)XXX-XXXX\n")
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
		print("CHANGE CONTACT\n")

		infile = open(file_name, "rb")
		contact_list = pickle.load(infile)
		infile.close()


		print("Choose contact to change or enter '_EXIT' to exit\n")
		
		i=1
		for cont in contact_list:
			print("{}) {} {} {} {} {}".format(i, cont.first_name, cont.last_name, cont.phone_number, cont.birthday, cont.address))
			i += 1

		user_input = input()


		try:
			if(int(user_input) >= 1 or int(user_input) <= len(contact_list)):
				changing_contact = contact_list[int(user_input)-1]
				os.system("clear")
				print("Updating contact\n")
				lil_menu = {}
				lil_menu["1"] = "Update first name"
				lil_menu["2"] = "Update last name"
				lil_menu["3"] = "Update phone number"
				lil_menu["4"] = "Update DOB"
				lil_menu["5"] = "Update address"
				lil_menu["6"] = "Cancel"
				for k,v in lil_menu.items():
					print("{}) {}".format(k, v))
				user_input2 = input()
				update_contact(changing_contact, user_input2) 
			else:
				os.system("clear")
				print("ERROR 583: Invalid input\n")


		except ValueError:
			if(user_input == "_EXIT"):
				os.system("clear")
				print(">>>>>Cancelled action\n")
				contact_file()
			else:
				os.system("clear")
				print("ERROR 493: Invalid input\n")
				contact_file()

		outfile = open(file_name, "wb")
		pickle.dump(contact_list, outfile)
		outfile.close()

		os.system("clear")
		print(">>>>>Contact updated\n")
		contact_file()
	elif(user_input == "4"):
		os.system("clear")
		print("DELETE CONTACT")
		print("Choose contact to change or enter '_EXIT' to exit\n")

		infile = open(file_name, "rb")
		contact_list = pickle.load(infile)
		infile.close()

		i = 1
		for cont in contact_list:
			print("{} {} {} {} {} {}".format(i, cont.first_name, cont.last_name, cont.phone_number, cont.birthday, cont.address))
			i += 1
		user_input = input()
		try:

			if int(user_input) >= 1 and int(user_input) <= len(contact_list):
                                del contact_list[int(user_input)-1]

                                outfile = open(file_name, "wb")
                                pickle.dump(contact_list, outfile)
                                outfile.close()

                                os.system("clear")
                                print(">>>>>Contact deleted\n")
                                contact_file()
			else:                
                        	os.system("clear")
                        	print(">>>>>ERROR 593: Invalid input\n")
                        	contact_file()

		except ValueError:
			os.system("clear")
			print("Action cancelled\n") if user_input == "_EXIT" else print("ERROR 309: Invalid input\n")
			contact_file()
	elif(user_input == "5"):
		os.system("clear")
		print("SEARCH FOR CONACT")
		print("Would you like to search for name by first name, last name, phone number, DOB, or address?\n")

		lil_menu = {}
		lil_menu["1"] = "First Name"
		lil_menu["2"] = "Last Name"
		lil_menu["3"] = "Phone Number"
		lil_menu["4"] = "Date of Birth"
		lil_menu["5"] = "Address"
		lil_menu["6"] = "Exit"

		for k,v in lil_menu.items():	
			print("{} {}".format(k, v))

		infile = open(file_name, "rb")
		contact_list = pickle.load(infile)                
		infile.close()
		user_input = input()
		matching_list = []
		matching_contacts = []

		if(user_input == "1"):
			# returns a list
			matching_contacts = sift_through(matching_list, contact_list, "first_name", input("Enter first name:\t"))
		elif(user_input == "2"):
			matching_contacts = sift_through(matching_list, contact_list, "last_name", input("Enter last name:\t"))
		elif(user_input == "3"):
			matching_contacts = sift_through(matching_list, contact_list, "phone_number", input("Enter phone number in form of (XXX)XXX-XXXX:\t"))
		elif(user_input == "4"):
			matching_contacts = sift_through(matching_list, contact_list, "birthday", input("Enter DOB in form of XX/XX/XXX:\t"))
		elif(user_input == "5"):
			matching_contacts = sift_through(matching_list, contact_list, "address", input("Enter address:\t"))
		elif(user_input == "6"):
			os.system("clear")
			contact_file()

		else:
			os.system.clear()
			print("ERROR 207: Invalid input\n")
			contact_file()	
		print("-------------------------------------------------------\n")
		for cont in matching_contacts:
			print("{} {} {} {} {}\n".format(cont.first_name, cont.last_name, cont.phone_number, cont.birthday, cont.address))

		user_input = input("\nEnter any key to exit\n")
		os.system("clear")
		contact_file()
		
		

	elif(user_input == "6"):
		os.system("clear")
		print("DELETE ALL CONTACTS\n")
		
		print("Are you sure you want to delete all contacts? This cannot be undone.\n")
		print("1) Yes\n")
		print("2) No\n")

		user_input = input()
		if user_input == "1":
			outfile = open(file_name, "wb")
			pickle.dump([], outfile)
			outfile.close()
			os.system("clear")
			print(">>>>>All contacts deleted\n")
			contact_file()
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
			rand_p_number = "({}){}-{}".format(randint(100,999), randint(100,999), randint(1000,9999))
			rand_birthday = "{}/{}/{}".format(randint(1,13), randint(1,31), randint(1900,2021))
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

def sift_through(matching_list, contact_list, key_word, search_word):
	for cont in contact_list:

		if(key_word == "first_name"):
			if cont.first_name == search_word:
				matching_list.append(cont)
		elif(key_word == "last_name"):
			if cont.last_name == search_word:
				matching_list.append(cont)
		elif(key_word == "phone_number"):
			if cont.phone_number == search_word:
				matching_list.append(cont)
		elif(key_word == "birthday"):
			if cont.birthday == search_word:
				matching_list.append(cont)
		elif(key_word == "address"):
				matching_list.append(cont)

	return matching_list

def update_contact(changing_contact, user_input2):
	if (user_input2 == "1"):
		new_name = input("Change first name to:\t")
		changing_contact.first_name = new_name
	elif(user_input2 == "2"):
		new_name = input("Change last name to:\t")
		changing_contact.last_name = new_name
	elif(user_input2 == "3"):
		new_number = input("Change phone number to (XXX)XXX-XXXX:\t")
		changing_contact.phone_number = new_number
	elif(user_input2 == "4"):
		new_birthday = input("Change DOB to (XX/XX/XXXX):\t")
		changing_contact.birthday = new_birthday
	elif(user_input2 == "5"):
		new_address = input("Change address to:\t")
		changing_contact.address = new_address
	elif(user_input2 == "6"):
		os.system("clear")
		contact_file()

	else:
		os.system("clear")
		print(">>>>>ERROR 109: Invalid input")
		contact_file() 

	return
