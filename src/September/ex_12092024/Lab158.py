from Browser_Package.openBrowser import start_Browser
from Browser_Package.close_browser import close_browser


def test_case():
    start_Browser()
    print("Iam executing testcase 1")
    close_browser()



test_case()