import openpyxl
import csv
import xlrd
filename = 'iris_data.xlsx'
# created from: https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set


def csv_from_excel():
    wb = xlrd.open_workbook(filename)

    # retrieves the sheet to be worked on
    sh = wb.sheet_by_name("Fisher's Iris Data")

    # creates csv-file with write-permission
    csv_file = open('output.csv', 'w')

    # creates writer-object
    wr = csv.writer(csv_file, delimiter='\t', quotechar='|')

    # nrows is the number of rows
    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    print("excel to csv has been completed for " + filename)
    csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()

#run test to spam data into console
def test_excel_file():
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name("Fisher's Iris Data")
    for rowOfCellObjects in sheet['A1':'E151']:
        for cellObj in rowOfCellObjects:
            print(cellObj.coordinate, cellObj.value)
        print('---------')

# run test_excel_file() 