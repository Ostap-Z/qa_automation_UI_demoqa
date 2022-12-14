from random import randint

import allure
import pytest

from pages.elements_page.web_table_page import WebTablePage


@allure.suite("Elements suite")
@allure.feature("Web Table page")
class TestWebTable:

    @allure.title(
        "Verify that the user has an opportunity "
        "to add a new person to the table"
    )
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(
            driver,
            "https://demoqa.com/webtables"
        )
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result, \
            "\nActual result:" \
            f"\n\t{new_person} not in the {table_result}" \
            "\nExpected result:" \
            f"\n\t{new_person} should be in the {table_result}"

    @allure.title(
        "Verify that the user has an opportunity to "
        "find a person in the table by key word"
    )
    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(
            driver,
            "https://demoqa.com/webtables"
        )
        web_table_page.open()
        key_word = web_table_page.add_new_person()[randint(0, 5)]
        web_table_page.search_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, \
            "\nActual result:" \
            f"\n\t{key_word} not in the table {table_result}" \
            "\nExpected result:" \
            f"\n\t{key_word} should be in the table {table_result}"

    @allure.title(
        "Verify that the user has an opportunity to "
        "update a person info"
    )
    def test_web_table_edit_person(self, driver):
        web_table_page = WebTablePage(
            driver,
            "https://demoqa.com/webtables"
        )
        web_table_page.open()
        last_name = web_table_page.add_new_person()[1]
        web_table_page.search_person(last_name)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, \
            "\nActual result:" \
            f"\n\t{age} is not present in the {row}" \
            "\nExpected result:" \
            f"\n\t{age} should be present in the {row}"

    @allure.title(
        "Verify that the user has an opportunity to "
        "delete a person from the table"
    )
    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(
            driver,
            "https://demoqa.com/webtables"
        )
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_person(email)
        web_table_page.delete_person()
        deleted_text = web_table_page.check_deleted_person()
        assert deleted_text == "No rows found"

    @allure.title(
        "Verify that the user has an opportunity to "
        "set different amount of table rows: "
        "[5, 10, 20, 25, 50, 100]"
    )
    @pytest.mark.xfail(
        reason="Expected failed due to there is a bug - "
               "the user can't see count_rows dropdown "
               "when more than 20 rows are opened"
    )
    def test_web_table_change_row_count(self, driver):
        web_table_page = WebTablePage(
            driver,
            "https://demoqa.com/webtables"
        )
        web_table_page.open()
        count = web_table_page.select_up_to_rows()
        assert count == [5, 10, 20, 25, 50, 100], \
            "The number of rows in the table " \
            "hasn't been changed or changed incorrect "
