import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sdk.locators.locators import TrySqlPageLocators
from sdk.pages.base_page import BasePage


class TrySqlPage(BasePage):

    def should_be_sql_statement_input_form(self):
        assert self.is_element_present(*TrySqlPageLocators.TEXT_AREA_CODE_SQL)

    def should_be_execute_sql_button(self):
        assert self.is_element_present(*TrySqlPageLocators.RUN_SQL_BUTTON)

    def should_be_result_form(self):
        assert self.is_element_present(*TrySqlPageLocators.RESULT_AREA)

    def should_be_dml_form(self):
        self.should_be_sql_statement_input_form()
        self.should_be_execute_sql_button()
        self.should_be_result_form()

    def execute_query(self, query):
        allure.attach(query, 'SQL Query', allure.attachment_type.TEXT)

        self.driver.execute_script(f'window.editor.setValue("{query}")')
        self.driver.find_element(*TrySqlPageLocators.RUN_SQL_BUTTON).click()

    def get_result(self):
        result = []

        result_area = self.driver.find_element(*TrySqlPageLocators.RESULT_AREA)

        # All results are in the table. No result - no table.
        table_rows = result_area.find_elements(*TrySqlPageLocators.RESULT_TABLE_ROWS)
        if table_rows:
            table_headers = [col.text for col in table_rows[0].find_elements(*TrySqlPageLocators.RESULT_TABLE_HEADERS)]

            for i in range(1, len(table_rows)):  # Exclude row with column names when iterating over rows.
                table_data = table_rows[i].find_elements(*TrySqlPageLocators.RESULT_TABLE_DATA)

                data = [s.text for s in table_data]
                result.append(dict(zip(table_headers, data)))

        allure.attach(str(result), 'DB rows', allure.attachment_type.TEXT)

        return result

    def should_show_change_result_message(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(TrySqlPageLocators.CHANGE_RESULT_MESSAGE))

    def restore_db(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TrySqlPageLocators.RESTORE_DB_BUTTON)).click()
        self.driver.switch_to.alert.accept()
