import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_see_backet_link(browser):
    browser.get(link)
    y = len(browser.find_elements_by_id("add_to_basket_form"))
    assert y > 0, 'Cелектор кнопки не найден'
    
    
    
    # Для запуска теста pytest -s -v --language=es test_items.py
    #не забудьте добавить time.sleep(30)
    