class Contact():
	num_of_contacts = 0

	def __init__(self, first_name, last_name, phone_number, birthday, address):
		self.first_name = "NA" if first_name == "_SKIP" else first_name
		self.last_name = last_name 
		self.phone_number = phone_number
		self.birthday = birthday
		self.address = address

	def get_first_name():
		return self.first_name
