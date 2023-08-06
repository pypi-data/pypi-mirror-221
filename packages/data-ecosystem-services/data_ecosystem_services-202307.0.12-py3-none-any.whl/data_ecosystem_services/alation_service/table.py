from .manifest import Manifest
from .column import Column
from pandas import json_normalize
from bs4 import BeautifulSoup

import json
from jsonschema import validate
import sys
import os
import pandas as pd
import requests


from data_ecosystem_services.cdc_admin_service import (
    environment_tracing as pade_env_tracing,
    environment_logging as pade_env_logging
)

import data_ecosystem_services.cdc_tech_environment_service.environment_file as pade_env_file
import data_ecosystem_services.alation_service.tokenendpoint as alation_token_endpoint

# Get the currently running file name
NAMESPACE_NAME = os.path.basename(os.path.dirname(__file__))
# Get the parent folder name of the running file
SERVICE_NAME = os.path.basename(__file__)

ENVIRONMENT = "dev"

# Get the absolute path of the current script
current_script_path = os.path.abspath(__file__)

# Get the project root directory by going up one or more levels
project_root = os.path.dirname(os.path.dirname(current_script_path))


class Table:
    """
    Represents a table object.

    """

    def __init__(self, table_json, schema_file_path):
        """
        Initializes a Table object using the provided table JSON.

        Args:
            table_json (dict): The JSON data representing the table.

        Raises:
            Exception: If an error occurs during initialization.

        """

        logger_singleton = pade_env_logging.LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        logger = logger_singleton.get_logger()
        tracer_singleton = pade_env_tracing.TracerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        tracer = tracer_singleton.get_tracer()

        with tracer.start_as_current_span("__init__"):

            try:

                self.schema_file_path = schema_file_path

                if table_json is None:
                    return

                manifest = Manifest(schema_file_path)

                # get the expected fields from the manifest
                schema_fields, expected_table_fields, expected_column_fields, required_table_fields = manifest.get_manifest_expected_fields()

                msg = "Schema fields length: " + str(len(schema_fields))
                logger.info(msg)
                msg = "Expected table fields length: " + \
                    str(len(expected_column_fields))
                logger.info(msg)

                # add specified tables fields to the table object and update if necessary
                for key in expected_table_fields:
                    if key in table_json:
                        setattr(self, key, table_json[key])

                missing_keys = [
                    key for key in required_table_fields if not hasattr(self, key)]

                if missing_keys:
                    logger.error(f"Missing keys: {missing_keys}")

                # get the extra description fields from the table JSON
                self.extra_description_fields = self.get_table_extra_description_fields(
                    table_json)

                self.name = table_json['name']
                self.title = table_json['title']
                self.description = self.format_description(table_json)

                tags = table_json.get('tags')
                if tags is not None:
                    self.tags = tags
                else:
                    self.tags = []
                columns_json = table_json.get('columns')

                if columns_json is not None:
                    # self.columns = list(
                    #     map(lambda c: Column(c, schema_file_path), columns_json))
                    self.columns = {column.name: column for column in map(
                        lambda c: Column(c, self.schema_file_path), columns_json)}

                else:
                    self.columns = None
            except Exception as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                logger_singleton.error_with_exception(error_msg, exc_info)
                raise

    def get_alation_data(self):
        """
        Retrieves the title and description from the instance.

        This function checks the 'title' and 'description' attributes of the instance and returns a dictionary that includes 
        'title' and 'description' keys, each with their respective values, only if the values are not None. 
        It includes keys whose values are empty strings.

        Returns:
            dict: A dictionary with 'title' and 'description' keys. The dictionary will not include keys whose values are None.
            If both 'title' and 'description' are None, an empty dictionary is returned.
        """
        return {k: v for k, v in {
            'title': self.title,
            'description': self.description
        }.items() if v is not None}

    def get_valueset_for_tables_sql_xlsx(self, valueset_name):
        logger_singleton = pade_env_logging.LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        logger = logger_singleton.get_logger()
        tracer_singleton = pade_env_tracing.TracerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        tracer = tracer_singleton.get_tracer()

        with tracer.start_as_current_span("get_valueset_for_tables_sql_xlsx"):

            # Change the current working directory to the project root directory
            os.chdir(project_root)
            # Get the file utility object
            obj_file = pade_env_file.EnvironmentFile()

            # Get the manifest file
            schema_file = self.schema_file_path
            directory = os.path.dirname(schema_file) + "/"
            directory = obj_file.convert_to_current_os_dir(directory)
            schema_file_valuesets = directory + "excel_manifest_schema_valuesets.xlsx"
            file_exists = obj_file.file_exists(
                True, schema_file_valuesets, None)
            logger.info(f"file_exists: {file_exists}")
            df_fields_excel_table = pd.read_excel(
                schema_file_valuesets, valueset_name)
            return df_fields_excel_table, schema_file

    def get_schema_for_tables_sql_xlsx(self):
        """
        Reads an Excel file containing a schema for SQL tables from a specific location in the file system.

        The function first changes the current working directory to the project root directory, and then creates 
        an instance of the EnvironmentFile class. It constructs a path to the file location based on the current 
        environment and checks whether the file exists. The function reads the Excel file into a pandas DataFrame 
        and returns the DataFrame and the file path.

        The function raises an AssertionError if the file does not exist.

        Returns:
            tuple: A tuple containing a pandas DataFrame representing the content of the Excel file and the path 
            to the file.
        """

        logger_singleton = pade_env_logging.LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        logger = logger_singleton.get_logger()
        tracer_singleton = pade_env_tracing.TracerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        tracer = tracer_singleton.get_tracer()

        with tracer.start_as_current_span("get_schema_for_tables_sql_xlsx"):

            # Change the current working directory to the project root directory
            os.chdir(project_root)
            # Get the file utility object
            obj_file = pade_env_file.EnvironmentFile()

            # Get the manifest file
            schema_file = self.schema_file_path
            file_exists = obj_file.file_exists(True, schema_file, None)
            logger.info(f"file_exists: {file_exists}")
            df_fields_excel_table = pd.read_excel(schema_file)
            return df_fields_excel_table, schema_file

    def get_tables_for_schema_for_excel(self, config, alation_datasource_id, alation_schema_id):
        """
        This function fetches tables for a specified schema from Alation for excel processing.
        The function first gets an API token from the config using the token_endpoint helper. 
        It then constructs the necessary parameters for a GET request to the Alation API, 
        where it fetches the tables for the given schema. The function then processes the 
        API response to expand the JSON, transform it into a dataframe and match column 
        names with a predefined schema from an Excel source. After this, the data is sorted 
        by the order defined in the Excel schema.

        Args:
            config (dict): A configuration dictionary containing necessary API information.
            alation_datasource_id (int): The Alation id of the datasource to fetch tables from.
            alation_schema_id (int): The Alation id of the schema to fetch tables from.

        Returns:
            None. The function prints out the sorted dataframe containing the tables.
            For future use, this function could be modified to return the dataframe.

        Raises:
            AssertionError: An error occurred if the status code from the token endpoint is not 200.
        """

        logger_singleton = pade_env_logging.LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        logger = logger_singleton.get_logger()
        tracer_singleton = pade_env_tracing.TracerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        tracer = tracer_singleton.get_tracer()

        with tracer.start_as_current_span("get_tables_for_schema_for_excel"):

            # Change the current working directory to the project root directory
            os.chdir(project_root)

            edc_alation_base_url = config.get("edc_alation_base_url")
            token_endpoint = alation_token_endpoint.TokenEndpoint(
                edc_alation_base_url)
            status_code, edc_alation_api_token, api_refresh_token = token_endpoint.get_api_token_from_config(
                config)

            print(
                f"edc_alation_api_access_token_length: {str(len(edc_alation_api_token))}")
            print(f"api_refresh_token_length: {str(len(api_refresh_token))}")
            assert status_code == 200

            # setting the base_url so that all we need to do is swap API endpoints
            base_url = edc_alation_base_url
            # api access key
            api_key = edc_alation_api_token
            # setting up this access key to be in the headers
            headers = {"token": api_key}
            # api for tables
            api = "/integration/v2/table/"

            limit = 500
            skip = 0

            # Create a dictionary to hold the parameters
            params = {}
            params['limit'] = limit
            params['skip'] = skip
            params['schema_id'] = alation_schema_id
            params['ds_id'] = alation_datasource_id

            # make the API call
            tables_result = requests.get(
                base_url + api, headers=headers, params=params)
            # convert the response to a python dict.
            tables_result_json = tables_result.json()

            # Process the data
            expanded_json = []
            for item in tables_result_json:
                new_item = item.copy()  # start with existing fields
                for field in item['custom_fields']:
                    # add custom fields
                    new_item[field['field_name']] = field['value']
                expanded_json.append(new_item)

            # Convert to dataframe
            df_tables = json_normalize(expanded_json)

            # Get expected columns
            df_fields_excel_schema, schema_file = self.get_schema_for_tables_sql_xlsx()

            # html columns
            df_html_fields_excel_schema = df_fields_excel_schema[
                df_fields_excel_schema['field_type_alation'] == 'RICH_TEXT']

            html_columns = df_html_fields_excel_schema['field_name'].tolist()

            # Get a list of columns that exist in both df_tables and l
            table_column_names = df_tables.columns.tolist()
            valid_html_columns = [
                col for col in html_columns if col in table_column_names]

            if "description" not in valid_html_columns:
                valid_html_columns.append("description")

            # convert html
            for column in valid_html_columns:
                # for each row in the column
                for idx in df_tables.index:
                    # Get the value at the current cell
                    cell_value = df_tables.loc[idx, column]
                    try:
                        # Try to parse it as HTML
                        if cell_value is None:
                            cell_value = ''

                        if pd.isna(cell_value):
                            cell_value = ''

                        soup = BeautifulSoup(cell_value, 'html.parser')

                        # Check if 'html' and 'body' tags exist
                        if not soup.html:
                            soup = BeautifulSoup(
                                '<html><body>' + str(soup) + '</body></html>', 'html.parser')

                        # Extract text from the HTML document
                        text = soup.get_text()

                        # Replace the cell value with the parsed HTML
                        # This assumes that you want the first table, as pd.read_html returns a list of tables
                        df_tables.loc[idx, column] = text
                    except ValueError:
                        # pd.read_html throws a ValueError if it can't parse the input as HTML
                        # If this happens, we'll just leave the cell value as it is
                        pass

            # required columns
            df_fields_excel_schema = df_fields_excel_schema[
                df_fields_excel_schema['excel_column_order'] > 0]

            # Create a list of column names from df_fields_excel_schema in the order specified by excel_column_order
            ordered_columns = df_fields_excel_schema.sort_values('excel_column_order')[
                'field_name'].tolist()

            # Get a list of columns that exist in both df_tables and ordered_columns
            table_column_names = df_tables.columns.tolist()
            valid_columns = [
                col for col in ordered_columns if col in table_column_names]

            # Reorder the columns in df_tables
            df_tables = df_tables[valid_columns]

            # Create a list of columns to drop from df_tables
            columns_to_drop = [
                col for col in df_tables.columns.tolist() if col not in valid_columns]

            # Drop the columns from df_tables
            df_tables = df_tables.drop(columns=columns_to_drop)

            # Set the option to display all columns
            pd.set_option('display.max_columns', None)
            df_tables = df_tables.fillna('')

            print(df_tables)

            return df_tables

    def get_table_extra_description_fields(self, table_json):
        """
            Retrieves extra description fields from the table JSON.

            Args:
                table_json (dict): The JSON data representing the table.

            Returns:
                dict: A dictionary containing the extra description fields.

            Raises:
                Exception: If an error occurs while retrieving the extra description fields.

        """

        logger_singleton = pade_env_logging.LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        logger = logger_singleton.get_logger()
        tracer_singleton = pade_env_tracing.TracerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        tracer = tracer_singleton.get_tracer()

        with tracer.start_as_current_span("get_table_extra_description_fields"):

            try:

                extra_description_fields = {}
                if "extraDescriptionFields" in table_json:
                    optional_description_fields = table_json['extraDescriptionFields']
                    msg = "Extra description fields: %s", optional_description_fields
                    logger.info(msg)
                    for key in optional_description_fields:
                        extra_description_fields[key] = optional_description_fields[key]
                return extra_description_fields
            except Exception as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                logger_singleton.error_with_exception(error_msg, exc_info)
                raise

    def format_description(self, table_json):
        """
        Formats the description for the table.

        Args:
            table_json (dict): The JSON data representing the table.

        Returns:
            str: The formatted description string.

        Raises:
            Exception: If an error occurs while formatting the description.

        """

        logger_singleton = pade_env_logging.LoggerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        logger = logger_singleton.get_logger()
        tracer_singleton = pade_env_tracing.TracerSingleton.instance(
            NAMESPACE_NAME, SERVICE_NAME)
        tracer = tracer_singleton.get_tracer()

        with tracer.start_as_current_span("format_description"):

            try:

                description = table_json['description']
                if self.extra_description_fields:
                    description += '<br><table><tr><th>Field</th><th>Value</th></tr>'
                    for key in self.extra_description_fields:
                        description += '<tr><td>' + key + '</td><td>' + \
                            self.extra_description_fields[key] + '</td></tr>'
                    description += '</table>'
                return description
            except Exception as ex:
                error_msg = "Error: %s", ex
                exc_info = sys.exc_info()
                logger_singleton.error_with_exception(error_msg, exc_info)
                raise
