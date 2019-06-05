#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# readCensusExcel.py - tabulates population and number of census tracts for
# each country.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('/users/cruz/p3p/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# TODO: Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
	# each row in the spreadsheet has data for one census tract.
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

#TODO: Open a new text file and write thje contents of countyData to it.
print(countyData)

