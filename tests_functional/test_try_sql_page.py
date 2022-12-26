import allure

CONTACT_NAME = 'Giovanni Rovelli'


class TestTrySqlPage:

    @allure.title('Getting a record from Customers table')
    def test_customer_should_have_correct_address(self, try_sql_page):
        with allure.step('Given the page is ready to execute queries'):
            try_sql_page.open()
            try_sql_page.should_be_dml_form()

        with allure.step('When getting a record from the database'):
            query = f"SELECT * FROM Customers WHERE ContactName='{CONTACT_NAME}'"
            try_sql_page.execute_query(query)

        with allure.step('Then correct data returned'):
            result = try_sql_page.get_result()

            assert len(result) == 1
            assert result[0].get('Address') == 'Via Ludovico il Moro 22'

    @allure.title('Getting all records from London city from Customers table')
    def test_customers_number_from_london_should_equal_six(self, try_sql_page):
        with allure.step('Given the page is ready to execute queries'):
            try_sql_page.open()
            try_sql_page.should_be_dml_form()

        with allure.step('When getting records with condition from the database'):
            query = "SELECT * FROM Customers WHERE city='London'"
            try_sql_page.execute_query(query)

        with allure.step('Then correct data returned'):
            result = try_sql_page.get_result()
            assert len(result) == 6

    @allure.title('Adding a record in Customers table and check the changes in DB')
    def test_add_new_customer_should_add_new_entry(self, try_sql_page):
        with allure.step('Given the page is ready to execute queries'):
            try_sql_page.open()
            try_sql_page.should_be_dml_form()

        with allure.step('When adding a record in the database'):
            new_customer = {
                'CustomerName': 'Cardinal',
                'ContactName': 'Tom B. Erichsen',
                'Address': 'Skagen 21',
                'City': 'Stavanger',
                'PostalCode': '4006',
                'Country': 'Norway'
            }
            query = f"INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) \
                    VALUES ('{new_customer.get('CustomerName')}', '{new_customer.get('ContactName')}', " \
                    f"'{new_customer.get('Address')}', '{new_customer.get('City')}', '{new_customer.get('PostalCode')}'," \
                    f"'{new_customer.get('Country')}')"
            try_sql_page.execute_query(query)

        with allure.step('Then correct result message is shown'):
            try_sql_page.should_show_change_result_message()

        with allure.step('When getting the record from the database'):
            query = f"SELECT * FROM Customers WHERE ContactName='{new_customer.get('ContactName')}'"
            try_sql_page.execute_query(query)

        with allure.step('Then correct data returned'):
            result = try_sql_page.get_result()
            assert len(result) == 1

            result[0].pop('CustomerID', None)  # Exclude CustomerId from comparing.
            assert new_customer == result[0]

    @allure.title('Update all fields for a record in Customers table and check the changes in DB')
    def test_update_customer_should_update_entry(self, try_sql_page):
        with allure.step('Given the page is ready to execute queries'):
            try_sql_page.open()
            try_sql_page.should_be_dml_form()

        with allure.step('When adding the record in the database'):
            customer_id = 1
            updated_customer = {
                'CustomerName': 'Updated Magazzini Alimentari Riuniti',
                'ContactName': 'Updated Giovanni Rovelli',
                'Address': 'Updated Via Ludovico il Moro 22',
                'City': 'Updated Bergamo',
                'PostalCode': 'Updated 24100',
                'Country': 'Updated Italy'
            }

            query = f"UPDATE Customers SET CustomerName='{updated_customer.get('CustomerName')}', " \
                    f"ContactName='{updated_customer.get('ContactName')}', Address='{updated_customer.get('Address')}'," \
                    f"City='{updated_customer.get('City')}', PostalCode='{updated_customer.get('PostalCode')}'," \
                    f"Country='{updated_customer.get('Country')}'" \
                    f"WHERE CustomerId={customer_id}"

            try_sql_page.execute_query(query)

        with allure.step('Then correct result message is shown'):
            try_sql_page.should_show_change_result_message()

        with allure.step('When getting a record from the database'):
            query = f"SELECT * FROM Customers WHERE CustomerId='{customer_id}'"
            try_sql_page.execute_query(query)

        with allure.step('Then correct data returned'):
            result = try_sql_page.get_result()
            assert len(result) == 1

            result[0].pop('CustomerID', None)  # Exclude CustomerId from comparing.
            assert updated_customer == result[0]

    @allure.title('Deleting a record in Customers table and check the changes in DB')
    def test_deleting_customer_should_delete_entry(self, try_sql_page):
        with allure.step('Given the page is ready to execute queries'):
            try_sql_page.open()
            try_sql_page.should_be_dml_form()

        with allure.step('When deleting the record from the database'):
            query = f"DELETE FROM Customers WHERE ContactName='{CONTACT_NAME}'"
            try_sql_page.execute_query(query)

        with allure.step('Then correct result message is shown'):
            try_sql_page.should_show_change_result_message()

        with allure.step('When getting the record from the database'):
            query = f"SELECT * FROM Customers WHERE ContactName='{CONTACT_NAME}'"
            try_sql_page.execute_query(query)

        with allure.step('Then correct data returned'):
            result = try_sql_page.get_result()
            assert not result
