import time
import pytest
from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_present(browser):
    browser.get(url)
    add_to_cart_button = browser.find_elements(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert len(add_to_cart_button) != 0, f'Seems that "Add to cart" button not found'


if __name__ == '__main__':
    pytest.main()
