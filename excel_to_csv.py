import openpyxl
import csv
import xlrd
filename = 'iris_data.xlsx'
# created from: https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set


def csv_from_excel():
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name("Fisher's Iris Data")
    your_csv_file = open('output.csv', 'w')
    wr = csv.writer(your_csv_file, delimiter='\t', quotechar='|')

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    print()
    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()

def test_excel_file():
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name("Fisher's Iris Data")
    for rowOfCellObjects in sheet['A1':'E151']:
        for cellObj in rowOfCellObjects:
            print(cellObj.coordinate, cellObj.value)
        print('---------')

#test_excel_file() #run test to spam data into console