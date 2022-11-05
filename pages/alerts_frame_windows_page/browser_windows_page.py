from pages.base_page import BasePage
from locators.alerts_frame_windows_locators.browser_windows_locators import BrowserWindowsLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title
