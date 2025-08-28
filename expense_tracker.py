class ExpenseTracker:
	def __init__(self):
		self.expensies = {}
		self.user_info = {}

	def get_user_info(self):
		name = input('User Name: ')
		self.user_info['name'] = name

		age = int(input('User Age: '))
		self.user_info['age'] = age

	def main_screen(self):
		print(f'----- Welcome -----')
		print('1) add_expense')
		print('2) Get All Expensies')
		print('3) Remove Expense')
		print('4) Remove All Expensies')
		print('5) Get Total Expensies')
		print('6) Set Monthly Limit')

		try:
			user_num = int(input('Choose Number From 1 To 6: '))
		except:
			raise ValueError
		
		return user_num

	def add_expense(self):
		print('Expense Name: ')
		expense_name = input('Expense Name: ')

	def get_expensies(self):
		pass

	def remove_expense(self):
		pass

	def remove_all_expensies(self):
		pass

	def get_total_expensies(self):
		pass

	def set_monthly_limit_expensies(self):
		pass

	def run(self):
		pass