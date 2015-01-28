from app import app
import unittest


class FlaskTestCase(unittest.TestCase):


	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)
	#ensure that the login page loads correctly
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Please login' in response.data)
	#ensure login behaves correctly given correct credentials
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login', 
			data=dict(username="admin", password="admin"), 
			follow_redirects = True
		)
		self.assertIn(b'You were just logged in!', response.data)
	#ensure login behaves correctly given incorrect credentials
	#ensure logout


if __name__ == '__main__':
	unittest.main()