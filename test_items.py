

def test_button_add_to_basket_is_displayed(browser):
    button = browser.find_element_by_css_selector(".btn.btn-add-to-basket")
    assert button.is_displayed(), f"Button 'add_to_basket' is not displayed"
    return print(button)


#
# link = "https://www.google.com/"
#
# def test_button(browser):
#     browser.get(link)
#     input1 = browser.find_element_by_css_selector("input.gNO89b")
#     print(f"text = \'{input1}\'")


