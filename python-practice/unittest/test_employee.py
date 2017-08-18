import unittest
from employee import Employee

class Test_Employee(unittest.TestCase):

	def setUp(self):
		self.emp_1 = Employee('Corey', 'Shafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)

	def reatDown():
		pass

	def test_email(self):
		

		self.assertEqual(self.emp_1.email, 'Corey.Shafer@email.com')
		self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

		self.emp_1.first = 'John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.email, 'John.Shafer@email.com')
		self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

	# def test_fullname(self):
	# 	self.emp_1 = Employee('Corey', )


if __name__ == '__main__':
	unittest.main()