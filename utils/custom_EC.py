class length_of_the_element_text_not_null(object):
    """Ожидание что длинна текста элемента больше нуля."""
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element_text = driver.find_element(*self.locator).text
        if len(element_text) > 0:
            return True
        else:
            return False

class element_has_new_text(object):
    """Ожидание смены текста элемента"""
    def __init__(self, locator, old_text):
        self.locator = locator
        self.old_text = old_text

    def __call__(self, driver):
        new_text = driver.find_element(*self.locator).text
        if new_text != self.old_text:
            return True
        else:
            return False

class pay_button_is_red(object):
    """Ожидание что кнопка Продолжить красного цвета"""
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.value_of_css_property('background-color') == 'rgba(239, 61, 33, 1)':
            return True
        else:
            return False
