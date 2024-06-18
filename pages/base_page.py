from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(locator))

    def return_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def check_element_visible(self, locator):
        self.wait_for_element(locator)
        if expected_conditions.visibility_of_element_located(locator) is not None:
            return True

    def check_element_invisible(self, locator):
        self.wait_for_invisibility(locator)
        if expected_conditions.invisibility_of_element_located(locator) is not None:
            return True

    def scroll_to_element(self, locator):
        element = self.return_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def scroll_and_return(self, locator):
        self.scroll_to_element(locator)
        return self.return_element(locator)

    def get_text(self, locator):
        element = self.return_element(locator)
        return element.text

    def fill_field(self, locator, text):
        element = self.return_element(locator)
        element.send_keys(text)

    def click_element(self, locator):
        element = self.return_element(locator)
        element.click()

    def click_and_wait_for(self, locator, expected_element_locator):
        self.click_element(locator)
        self.wait_for_element(expected_element_locator)

    def click_and_wait_for_invisibility(self, locator, check_locator):
        self.click_element(locator)
        self.wait_for_invisibility(check_locator)

    @staticmethod
    def create_locator(locator_template, specification):
        method, locator = locator_template
        locator = locator.format(specification)
        result = (method, locator)
        return result

    def action(self):
        return ActionChains(self.driver)

    def anti_overlay_click(self):  # чтобы не падали тесты на Firefox
        self.action().move_by_offset(250, 0).click().perform()

    def drag_and_drop(self, dragged, target):
        self.action().drag_and_drop(dragged, target).pause(1).perform()
