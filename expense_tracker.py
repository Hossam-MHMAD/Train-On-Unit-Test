class ExpenseTracker:
	def __init__(self):
		self.expensies = {}
		self.user_info = {}

	def get_user_info(self):
		name = input('User Name: ')
		self.user_info['name'] = name

		age = int(input('User Age: '))
		self.user_info['age'] = age

	def add_expense(self):
		pass

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