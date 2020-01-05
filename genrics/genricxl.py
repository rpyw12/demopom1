import pandas as pd

def getXl(filepath, sheetname):
    xl = pd.read_excel(filepath, sheet_name=sheetname)
    return xl

def readData(filepath, sheetname, row_number, clo_name):
    xl=getXl(filepath,sheetname)
    value = xl.loc[row_number, clo_name]
    return value

def writeData(filepath, sheetname, row_number, clo_name, value):
    xl = getXl(filepath, sheetname)
    xl.loc[row_number, clo_name] = value
    writer = pd.ExcelWriter(filepath)
    xl.to_excel(writer, sheetname)
    writer.save()
