import pytest
from expense_tracker import ExpenseTracker

@pytest.fixture
def Tracker():
	return ExpenseTracker()

def test_init_expense_tracker(Tracker):
	"""Test If Expense Tracker Inizlized Properly"""
	assert len(Tracker.expensies) == 0
	assert Tracker.user_info == {}


def test_get_user_info(Tracker, monkeypatch):
	inputs = iter(["Ahmed", "20"])  
	monkeypatch.setattr("builtins.input", lambda _: next(inputs))

	Tracker.get_user_info()
	assert Tracker.user_info == {'name': 'Ahmed', 'age': 20}

def test_main_screen(Tracker, monkeypatch):
	"""using monkeypatch technique"""
	monkeypatch.setattr("builtins.input", lambda _: 'ge')
	with pytest.raises(ValueError):
		Tracker.main_screen()

# def test_expense_validation(Tracker):
# 	assert Tracker.check_expense(0) == False
# 	assert Tracker.check_expense(-33) == False
# 	assert Tracker.check_expense(4) == True


@pytest.mark.parametrize(
	"expense_amount,expected", 
	[
		(20, True),
		(30, True),
		(20.2, True),
		(.3, True),
		(0, False),
		(-34, False),
		(-2.3, False)
	])
def test_expense_function(Tracker, expense_amount, expected):
	assert Tracker.check_expense(expense_amount) == expected