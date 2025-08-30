from datetime import datetime

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
			while 0 >= user_num or user_num > 6:
				user_num = int(input('Choose Number From 1 To 6: '))
		except:
			raise ValueError
		
		return user_num

	def check_expense(self, expense_amount) -> bool:
		if expense_amount <= 0:
			return False
		return True

	def manage_expense_inputs_and_validation(self) -> bool:
		expense_name = input('Expense Name: ')
		expense_amount = float(input('Expense Amount: '))
		valid_expense = self.check_expense(expense_amount)
		if not valid_expense:
			print('         ---------------- Please Enter A Valid Expense ----------------')
		else:
			self.expensies[datetime.now().date()] = {'expense_name': expense_name, 'expense_amount': expense_amount}

	def get_expensies(self):
		print("---------------------------- All Expensies ----------------------------")
		for i, expense in enumerate(self.expensies, 1):
			print(f"{i}) {expense} -> (Expense Name: {self.expensies[expense]["expense_name"]}, Expense Amount: ${self.expensies[expense]["expense_amount"]})")
		print("-----------------------------------------------------------------------")

	def remove_expense(self, expense_number):
		
		print(list(self.expensies.keys))

	def remove_expense_inputs(self):
		self.get_expensies()
		expense_num = int(input('Enter Expense Number You Want To Remove: '))
		self.remove_expense(expense_num)

		# okay from here i quit because i knew how to test okay! 😬😤😤


	def remove_all_expensies(self):
		pass

	def get_total_expensies(self):
		pass

	def set_monthly_limit_expensies(self):
		pass

	def run(self):
		pass