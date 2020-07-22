def test_button_add_to_basket_is_displayed(browser):
    button = browser.find_element_by_css_selector(".btn.btn-add-to-basket")

    assert button.is_displayed(), "Button is not displayed"

    elements = browser.find_elements_by_css_selector(".btn.btn-add-to-basket")
    assert len(elements) > 0, "Button is not displayed"

    # element = None
    # try:
    #     element = browser.find_elements_by_css_selector(".btn.btn-add-to-basket")
    # except NoSuchElementException:
    #     print("Button is not displayed")



