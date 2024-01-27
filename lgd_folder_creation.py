import pandas as pd
import os

# Read the Excel sheet
df = pd.read_excel('D:/VILLAGE_BOUNDARY_TASK_AND_SCRIPTS/LGD.xlsx')

# Set the folder path
base_folder = 'D:/output_folder/new1'

# Replace missing codes with relevant names
for index, column in df.iterrows():
    district_code = str(column['LGD District Code']).strip()
    taluk_code = str(column['LGD Taluk Code']).strip()
    village_code = str(column['LGD Village Code']).strip()
    village_name = str(column['Village Name'])
    district_name = str(column['District Name'])
    taluk_name = str(column['Taluk Name'])

    if not district_name:
        district_name = district_code
    if not taluk_name:
        taluk_name = taluk_code
    if not village_name:
        village_name = village_code

    district_folder = os.path.join(base_folder, 'districts', district_name)
    #taluk_folder = os.path.join(district_folder, taluk_name)
    #village_folder = os.path.join(taluk_folder, village_name)

    # Create district folder if it doesn't exist
    if district_name and not os.path.exists(district_folder):
        os.makedirs(district_folder)

    # Create taluk folder if it doesn't exist
    #if taluk_name and not os.path.exists(taluk_folder):
        #os.makedirs(taluk_folder)

    # Create village folder if it doesn't exist
    #if village_name and not os.path.exists(village_folder):
       # os.makedirs(village_folder)
