import string
import random
from random import randint, choices, sample, shuffle


class PasswordManager:

	def __init__(self, name, master_pw, filename = None):
		self.passwords = {}
		self.__name = name 
		self.__master_pw = master_pw 

	def add_password(self, site, username, criteria = None):
		self.user_name = username
		if self.__password_gen(criteria):
			if site not in self.user_name:
				password = self.__password_gen(criteria)
				self.passwords[site] = [self.user_name, password]
		else:
			print('Invalid Specifications')


	def __password_specs(self, length = 14, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
		num_sc = randint(min_spec, min((length - min_num - min_upper), max_spec))
		num_num = randint(min_num, length - num_sc  - min_upper)
		num_upper = randint(min_upper, length - num_sc - num_num)
		num_lower = length - (num_sc + num_num + num_upper)
		return [num_sc, num_num, num_upper, num_lower]


	def __password_gen(self, criteria = None,length = 14, spec_char = '@!&', repeat = True, min_spec = 0, max_spec = 0, min_num = 0, min_upper = 0):
		if criteria != None:
			for spec, item in criteria.items():
				if spec == 'length':
					length = item
				elif spec =='spec_char':
					spec_char = item
				elif spec == 'repeat':
					repeat = item
				elif spec == 'min_spec':
					min_spec = item
				elif spec == 'max_spec':
					max_spec = item
				elif spec == 'min_num':
					min_num = item
				elif spec == 'min_upper':
					min_upper = item
		if(max_spec < min_spec):
			max_spec = min_spec
		required = sum([min_spec, min_num, min_upper])
		if required <= length and (repeat or len(spec_char)>=min_spec):
			specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
			if(repeat):
				password = random.choices(string.ascii_lowercase, k=specs[3]) + random.choices(string.ascii_uppercase, k=specs[2]) + random.choices(string.digits, k=specs[1]) + random.choices(spec_char, k=specs[0])
			else:
				if specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase) or specs[3] > len(string.ascii_lowercase):
					specs = self.__password_specs(length, min_spec, max_spec, min_num, min_upper)
					password = random.sample(string.ascii_lowercase, k=specs[3]) + random.sample(string.ascii_uppercase, k=specs[2]) + random.sample(string.digits, k=specs[1]) + random.sample(spec_char, k=specs[0])
			shuffle(password)
			return ''.join(password)

	def validate(self, mp):
		if self.__master_pw ==  mp:
			return True
		else:
			return False

	def change_password(self, site, master_pass, new_pass = None, criteria = None):
		if self.validate(master_pass)== True:
			if site in self.passwords:
				if new_pass != None:
					self.passwords[site] = [self.user_name,new_pass]
				else:
					self.__password_gen(criteria)
			else:
				print('Site does not exist')
				return False
		else:
			print('Incorrect master password')
			return False
	
	def remove_site(self, site):
		if site in self.passwords:
			del self.passwords[site]

	def get_site_info(self, site):
		for site in self.passwords:
			value = self.passwords.get(site)
		return value

	def get_name(self):
		return self.__name

	def get_site_list(self):
		site_list = list(self.passwords.keys())
		return site_list

	def __str__(self):
		result = 'Sites stored for ' + str(self.__name) + ':\n'
		for sites in self.passwords:
			result += str(sites) + '\n'
		return result
