import os
from push_data import *
import pandas as pd
import gspread
from dotenv import load_dotenv
import json
from unittest.mock import MagicMock

def test_service_file_path():
    """
    This test the service file path declared in .env if it contains neccessary keys
    """
    load_dotenv()
    path = os.getenv("service_file_path")
    with open(path) as jsonFile:
        data = json.load(jsonFile)
        keys = data.keys()

        assert 'private_key_id' in keys
        assert 'project_id' in keys
        assert 'client_id' in keys
        assert 'token_uri' in keys
        assert 'auth_uri' in keys

def test_create_spreadsheet():
    """
    tests the create spreadsheet function
    """

    load_dotenv()
    service = os.getenv("service_file_path")
    title = os.getenv("title")
    gc = gspread.service_account(service)

    assert gc
    assert create_spreadsheet(gc, title)
    assert type(gc) == gspread.client.Client    

def test_load_file_into_dataframe():
    """
    tests the load dataframe function
    """

    file = "gspread-project/data/Housing_dataset_train.csv"
    df = load_file_into_dataframe(file)

    assert type(df) == pd.DataFrame
    assert df.isna().sum().max() == 0

def test_add_email():
    """
    tests the add email function
    """

    #using magicmock to mock gspread.spreadsheet
    spreadsheet = MagicMock(return_value=gspread.spreadsheet)
    email = "test@gmail.com"
    assert add_email(spreadsheet, email) is None
    
def test_create_worksheet():
    """
    tests create worksheet function
    """

    # using magicmock to mock gpread.spreadsheets
    sheet = MagicMock(return_value=gspread.spreadsheet)
    worksheet = create_worksheet(sheet, title="title")
    assert worksheet
    