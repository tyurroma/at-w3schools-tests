from selenium.webdriver.common.by import By

from constants import Constants


class TrySqlPageLocators:
    TEXT_AREA_CODE_SQL = (By.ID, 'textareaCodeSQL')
    RUN_SQL_BUTTON = (By.XPATH, f'//button[text()="{Constants.RUN_SQL_TEXT}"]')

    RESTORE_DB_BUTTON = (By.ID, 'restoreDBBtn')

    RESULT_AREA = (By.ID, 'divResultSQL')
    RESULT_TABLE_ROWS = (By.TAG_NAME, 'tr')
    RESULT_TABLE_HEADERS = (By.TAG_NAME, 'th')
    RESULT_TABLE_DATA = (By.TAG_NAME, 'td')

    CHANGE_RESULT_MESSAGE = (By.XPATH, f'//*[contains(text(),"{Constants.CHANGE_RESULT_MESSAGE_TEXT}")]')
