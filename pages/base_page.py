from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def refresh(self):
        self.driver.refresh()

    def anti_overlay_click(self):  # чтобы не падали тесты на Firefox
        action = ActionChains(self.driver)
        action.move_by_offset(250, 0).click().perform()

    def return_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

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
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(expected_element_locator))

    def click_and_wait_for_invisibility(self, locator, check_locator):
        self.click_element(locator)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(check_locator))

    @staticmethod
    def create_locator(locator_template, specification):
        method, locator = locator_template
        locator = locator.format(specification)
        result = (method, locator)
        return result

