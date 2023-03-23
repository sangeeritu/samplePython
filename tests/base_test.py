import unittest

import os

from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

class BaseTest(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "sangeethanarayan_A7hYOz"
        BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "Gv1pqh9rLAykDsiY6pft"
        URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

        bstack_options = {
            "os": "OS X",
            "osVersion": "Monterey",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack single python",
            "userName": BROWSERSTACK_USERNAME,
            "accessKey": BROWSERSTACK_ACCESS_KEY
        }
        bstack_options["source"] = "python:sample-main:v1.0"
        options = ChromeOptions()
        options.set_capability('bstack:options', bstack_options)
        self.driver = webdriver.Remote(command_executor=URL, options=options)
        self.driver.get("http://www.amazon.com")

    def tearDown(self):
        self.driver.close()


class TestPages:
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)
