import allure
import requests

from pages.base_page import BasePage
from locators.elements_locators.links_locators import LinksPageLocators


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step(
        "Check a simple new tab"
    )
    def check_new_tab_simple_link(self):
        log = self.get_logger()
        simple_link = \
            self.element_is_visible(self.locators.SIMPLE_LINK)

        with allure.step("Get the 'href' attribute"):
            link_href = simple_link.get_attribute("href")

        with allure.step("Do get request for the 'Simple Link': "
                         f"{link_href}"):
            request = requests.get(link_href)

        with allure.step("Check if status code is 200"):
            if request.status_code == 200:

                with allure.step("Clicks on the 'Simple Link'"):
                    simple_link.click()
                log.info("Clicked on the simple link")

                with allure.step("Switch to the new tab"):
                    self.driver.switch_to.window(
                        self.driver.window_handles[1])

                with allure.step("Get an url of the new opened tab"):
                    url = self.driver.current_url
                log.info(f"Current url: {url}")
                log.info(f"Link href: {link_href}")
                return link_href, url

            else:
                log.info(f"Link href: {link_href}")
                log.info(f"Status code: {request.status_code}")
                return link_href, request.status_code

    @allure.step(
        "Check broken link"
    )
    def check_broken_link(self, url):
        log = self.get_logger()

        with allure.step("Do get request for the "
                         f"'Broken Link': {url}"):
            request = requests.get(url)

        with allure.step("Check if status code is 200"):
            if request.status_code == 200:

                with allure.step("Clicks on the 'Broken Link'"):
                    self.element_is_present(
                        self.locators.BAD_REQUEST_LINK).click()
                    log.info("Clicked on the bad request link")
                    log.info(f"Status code: {request.status_code}")

            else:
                log.info(f"Status code: {request.status_code}")
                return request.status_code
