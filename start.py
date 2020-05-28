import os
import pickle
import contact_file

try:
	f=open("Contact_Book", "rb")
	f.close()
except FileNotFoundError:
	outfile=open("Contact_Book", "wb")
	data_list = []
	pickle.dump(data_list, outfile)
	outfile.close()

os.system("clear")
contact_file.contact_file()
