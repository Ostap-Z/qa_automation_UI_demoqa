from random import randint

import allure

from pages.base_page import BasePage
from locators.widgets_locators.slider_locators import SliderLocators


class SliderPage(BasePage):
    locators = SliderLocators()

    @allure.step(
        "Check the 'Slider' value"
    )
    def change_slider_value(self):
        log = self.get_logger()

        with allure.step("Get the 'Slider' value before drag"):
            value_before = \
                self.element_is_visible(
                    self.locators.SLIDER_VALUE).get_attribute(
                    'value')

        log.info(f"Slider value before: {value_before}")
        slider_input = self.element_is_visible(
            self.locators.SLIDER_INPUT)

        with allure.step("Drag the 'Slider' element to random position"):
            self.action_drag_and_drop_by_offset(
                slider_input,
                randint(0, 100),
                0
            )

        with allure.step("Get the 'Slider' value after drag"):
            value_after = self.element_is_visible(
                self.locators.SLIDER_VALUE).get_attribute('value')

        log.info(f"Dragged slider to the value: {value_after}")
        log.info(f"Returned values before, after: "
                 f"{value_before}, "
                 f"{value_after}")
        return value_before, value_after
