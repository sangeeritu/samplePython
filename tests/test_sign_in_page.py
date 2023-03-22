import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


class TestSignInPage(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_search_item(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        search_result = page.search_item("iPhone")
        self.assertIn("iPhone", search_result)

