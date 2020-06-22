from selenium.webdriver.common.by import By

def test_user_should_see_the_site_on_pref_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket.is_displayed(), "There is no 'Add to basket' button."
