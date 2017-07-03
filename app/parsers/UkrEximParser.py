import pandas as pd


def file_parser(file):
    bank = 'UkrExim'

    UkrEximOpenFile = pd.read_excel(file).astype(str)
    UkrEximDataFrame = pd.DataFrame(UkrEximOpenFile[['Дата транзакції', 'Дебет', 'Кредит', 'Валюта', 'Призначення платежу', 'Найменування кореспондента', 'Рахунок', 'Код кореспондента']])
    UkrEximList = [list(x) for x in UkrEximDataFrame.to_records(index=False)]

    for i in range(len(UkrEximList)):
        UkrEximList[i].insert(0, bank)

    for i in range(len(UkrEximList)):
        for j in range(2, 4):
            if str(UkrEximList[i][j]) == 'nan':
                UkrEximList[i][j] = '0,00'
            UkrEximList[i][j] = str(UkrEximList[i][j]).replace('.', ',')
                
    for i in range(len(UkrEximList)):
        for j in range(len(UkrEximList[i])):
            if str(UkrEximList[i][j]) == 'nan':
                UkrEximList[i][j] = ''

    return UkrEximList
