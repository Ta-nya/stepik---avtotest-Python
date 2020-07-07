def test_button_add_to_basket_is_displayed(browser):
    button = browser.find_element_by_css_selector(".btn.btn-add-to-basket")
    assert button.is_displayed(), "Button is not displayed"




