import gspread
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

def service_file(file_path: str) -> gspread.client:
    """
    this function load google service account file
    """
    gc = gspread.service_account(filename=file_path)
    print("service file loaded successfully")

    return gc

def create_spreadsheet(gc: gspread.client, sheet_title: str) -> gspread.spreadsheet:
    """
    this function create a new spreadsheet
    """
    sheet = gc.create(sheet_title)
    print("google sheet created succesfully")

    return sheet

def add_email(sheet: gspread.spreadsheet, user_mail: str) -> None:
    """
    this function add user_email as a writer to the spreadsheet
    """
    sheet.share(user_mail, perm_type='user', role='writer')
    print("email added successfully")

    return None

def create_worksheet(sheet: gspread.spreadsheet, title: str) -> None:
    """
    function creates a worksheet
    """
    worksheet = sheet.add_worksheet(title="first", rows=100, cols=20)
    print("worksheet successfully created")

    return worksheet

def load_file_into_dataframe(link_to_dataset: str) -> pd.DataFrame:
    """
    this function read the dataset with pandas and drop nan values
    """
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    print("files successfully loaded into dataframe")

    return df

def update_worksheet(worksheet: gspread.spreadsheet, df: pd.DataFrame) -> None:
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print("worksheet updated successfully")

    return None

def run(user_email: str, file: str, service_file_path: str, sheet_title: str, worksheet_title: str) -> None:
    """
    this function runs the whole process of loading a dataset into a google spreadsheet
    """
    gc = service_file(service_file_path)
    sheet = create_spreadsheet(gc, sheet_title)
    add_email(sheet, user_email)
    worksheet = create_worksheet(sheet, worksheet_title)
    df = load_file_into_dataframe(file)
    update_worksheet(worksheet, df)

    return None

if __name__=="__main__":
    user_email = "gbotemibolarinwa@gmail.com"
    file = "https://github.com/GbotemiB/MLOps_zoomcamp/raw/main/data/Housing_dataset_train.csv"
    service_file_path = "./service_account.json"
    sheet_title = "housing_dataset"
    worksheet_title = "first"

    run(user_email, file, service_file_path, sheet_title, worksheet_title)

