
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


LOCALHOST = 'http://localhost:8000/'


class NewVisitorTest(unittest.TestCase):
    """
    Test for present data on the main page
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_contacts_table(self, row_text):
        "helper function for check rows in table"
        table = self.browser.find_element_by_id('id_contacts_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text, [row.text for row in rows])

    def test_visitor_can_see_the_main_page(self):
        """Hawk goes to check hello homepage"""
        self.browser.get(LOCALHOST)
        self.assertIn('42 Coffee Cups Test Assignment', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('42 Coffee Cups Test Assignment', header_text)

        # He also sees contacts of the applicant
        self.check_for_row_in_contacts_table('Sergey')
        self.check_for_row_in_contacts_table('Miletskiy')
        self.check_for_row_in_contacts_table('s.miletskiy@mockmyid.com')


class VisitorGoesToAdminPageTest(unittest.TestCase):
    """
    Test for admin page with default login and password
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_for_correct_admin_name_and_admin_pass(self):
        """ Hawk check for admin panel"""
        self.browser.get(LOCALHOST+'admin/')

        login = self.browser.find_element_by_id('id_username')
        login.send_keys('admin')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('admin' + Keys.RETURN)

        header_admin = self.browser.find_element_by_id('site-name').text
        self.assertEqual('Django administration', header_admin)


if __name__ == '__main__':
    unittest.main()
