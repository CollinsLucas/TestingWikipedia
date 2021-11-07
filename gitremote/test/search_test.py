import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

@pytest.mark.parametrize("search_term", "wake tech")

def test_wiki_search(search_term):
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 15)

        driver.get('https://en.wikipedia.org')
        driver.find_element(By.NAME, "search").send_keys(search_term + Keys.Return)

        result = wait.until(presence_of_element_located(By.CSS_SELECTOR, 'h1'))
        assert result.get_attribute('textContent') == 'Wake Technical Community College'
