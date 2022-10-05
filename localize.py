# Copyright 2022 by Cheonsong
# All rights reserved.
# and is released under the "MIT License Agreement". Please see the LICENSE

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import csv
import os
import re

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# JSON Key File Path
JSON_KEY_PATH = "../../Scripts/diary-364506-154725c9cb23.json"
# CSV File Path
CSV_FILE_PATH = "../../Scripts/localize.csv"
# language.lproj directory path
LPROJ_PATH = "../../Diary/App/Resources/"
# Google Spread Sheet Key
SPREADSHEET_KEY = "1m-OJOgLcWXkFNugPWcYUMVxosskWbgtt7Or1CJTtEwI"

# Google Auth Check
credential = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_PATH, scope)
gc = gspread.authorize(credential)

# Open Spread Sheet with Key
doc = gc.open_by_key(SPREADSHEET_KEY)

# Select Sheet
sheet = doc.worksheet("Strings")

# Get all values in the sheet into lists
sheetData = sheet.get_all_values()
if sheetData:
    print("*** GoogleSpreadSheet data extraction completed ***")

# Convert to csv file
with open(CSV_FILE_PATH, 'w', newline='') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    #write.writerow(fields)
    write.writerows(sheetData)
    print("*** Convert GoogleSpreadSheet to .csv completed ***")
    f.close()

# Read csv file
csvFile = open(CSV_FILE_PATH, 'r')
reader = csv.reader(csvFile)

languageList = []
codes = []

# Get language codes
for i in reader:
    codes = i[2:]
    print(codes)
    break

for i in codes:
    languageList.append(re.findall('[a-z_]{2}', i)[0])

# Make directories with language code
for i in languageList:
    os.makedirs(LPROJ_PATH + i + '.lproj', exist_ok=True)
csvFile.close()

# Write Localizable.strings
for code in languageList:
    # Open csv file only read
    csvFile = open(CSV_FILE_PATH, 'r')
    reader = csv.reader(csvFile)

    # Open Localizable.strings only write
    stringFile = open(LPROJ_PATH + code + '.lproj/Localizable.strings', 'w')

    # Check index
    index = languageList.index(code)

    # Write a Localizable.strings file by reading a line from a CSV file
    for line in reader:
        if line[0] != "" :
            stringFile.write("//" + line[0] + "\n")
        stringFile.write("\"" + line[1] + "\" = \"" + line[2+index] + "\";\n" )
    # Close files
    csvFile.close()
    stringFile.close()

