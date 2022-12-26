import pytest

from sdk.pages.try_sql_page import TrySqlPage
from sdk.utils.driver_manager import get_chromedriver


@pytest.fixture(scope='function')
def driver():
    driver = get_chromedriver()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def try_sql_page(driver, endpoint):
    return TrySqlPage(driver, endpoint)


@pytest.fixture(scope='function', autouse=True)
def restore_database(try_sql_page):
    try_sql_page.open()
    try_sql_page.restore_db()
