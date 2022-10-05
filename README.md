# LocalizeScript
Localizing script written in Python for iOS

## Version
- python3.10
- pip3

## Module
```shell
pip install oauth2client
pip install gspread
```

## Get Started
### Setting
```python
# JSON Key File Path
# You need to get it from Google
JSON_KEY_PATH = "../../Scripts/diary-364506-154725c9cb23.json"
# CSV File Path
CSV_FILE_PATH = "../../Scripts/localize.csv"
# language.lproj directory path
LPROJ_PATH = "../../Diary/App/Resources/"
# Google Spread Sheet Key
# You can get it from Google Spreadsheet url.
SPREADSHEET_KEY = "1m-OJOgLcWXkFNugPWcYUMVxosskWbgtt7Or1CJTtEwI"
# Select worksheet
sheet = doc.worksheet("Strings")
```

### Google Spread Sheet Form
![image](https://user-images.githubusercontent.com/59193640/194016082-f698fd23-30ab-4b3a-8026-1233a95166b0.png)

### Usage
```shell
python localize.py
```
You can get the csv file and strings files.


### XCode RunScript Pre Build
AppTarget - Build Phases - Add - New Run Script Phase - insert python localize.py (path)
