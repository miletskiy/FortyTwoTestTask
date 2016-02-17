
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.core.urlresolvers import reverse


LOCALHOST = 'http://localhost:8000'


class NewVisitorTest(unittest.TestCase):
    """
    Test for present data on the main page
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_visitor_can_see_the_main_page(self):
        """Hawk goes to check hello homepage"""
        self.browser.get(LOCALHOST)
        self.assertIn('Contacts 42 Coffee Cups Test Assignment',
                      self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('42 Coffee Cups Test Assignment', header_text)

        # He also sees contacts of the applicant
        first_name = self.browser.find_element_by_css_selector(
            '.list2 li:nth-child(1)').text
        last_name = self.browser.find_element_by_css_selector(
            '.list2 li:nth-child(2)').text
        email = self.browser.find_element_by_css_selector(
            '.list4 li:nth-child(1)').text
        self.assertEqual('Sergey', first_name)
        self.assertEqual('Miletskiy', last_name)
        self.assertEqual('s.miletskiy@mockmyid.com', email)

    def test_hawk_can_sees_new_link_requests(self):
        """
        Hawk goes to check hello homepage and sees new link requests
        """
        self.browser.get(LOCALHOST)
        self.browser.find_element_by_link_text('requests')
        requests = self.browser.find_element_by_id('id_requests').text

        self.assertEqual('requests', requests)


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
        self.browser.get(LOCALHOST+reverse('admin:index'))

        login = self.browser.find_element_by_id('id_username')
        login.send_keys('admin')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('admin' + Keys.RETURN)

        header_admin = self.browser.find_element_by_id('site-name').text
        self.assertEqual('Django administration', header_admin)


class VisitorGoesToRequestsPageTest(unittest.TestCase):
    """
    Test for admin page with default login and password
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def check_for_headers_of_requests_table(self, row_text):
        """
        Helper function for check headers in the table
        """
        table = self.browser.find_element_by_id('id_requests_table')
        rows = table.find_elements_by_tag_name('th')
        self.assertIn(row_text, [row.text for row in rows])

    def test_requests_page_title_and_subheader(self):
        """
        Hawk goes to requests page from main page
        """
        self.browser.get(LOCALHOST)
        requests = self.browser.find_element_by_link_text('requests')
        requests.click()

        # He sees the page title,
        self.assertIn('Requests 42 Coffee Cups Test Assignment',
                      self.browser.title)
        # header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('42 Coffee Cups Test Assignment', header_text)
        # and subheader
        sub_header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Requests', sub_header_text)

    def test_table_for_requests_presents_on_the_page(self):
        """
        Hawk sees table for requests with headers
        """
        self.browser.get(LOCALHOST+reverse('hello:requests'))

        self.check_for_headers_of_requests_table('Id')
        self.check_for_headers_of_requests_table('Title')
        self.check_for_headers_of_requests_table('Emergence')
        self.check_for_headers_of_requests_table('Path')
        self.check_for_headers_of_requests_table('Method')
        self.check_for_headers_of_requests_table('User')

if __name__ == '__main__':
    unittest.main()
