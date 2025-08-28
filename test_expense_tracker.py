import pytest
from expense_tracker import ExpenseTracker

pytest.MonkeyPatch.setattr()
@pytest.fixture
def Tracker():
	return ExpenseTracker()

def test_init_expense_tracker(Tracker):
	"""Test If Expense Tracker Inizlized Properly"""
	assert len(Tracker.expensies) == 0
	assert Tracker.user_info == {}


def test_get_user_info(Tracker, monkeypatch):
	pytest.monkeypatch.setattr("builtins.input", lambda _: {'name': 'Ahmed', 'age': 20})
	Tracker.get_user_info()
	assert Tracker.user_info == {'name': 'Ahmed', 'age': 20}