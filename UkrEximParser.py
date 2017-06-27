import pandas as pd

bank = 'UkrExim'

UkrEximFile = 'statics/УКРЭКСИМ.xlsx'
UkrEximOpenFile = pd.read_excel(UkrEximFile).astype(str)
UkrEximDataFrame = pd.DataFrame(UkrEximOpenFile[['Дата транзакції', 'Дебет', 'Кредит', 'Валюта', 'Призначення платежу', 'Найменування кореспондента', 'Рахунок']])
UkrEximList = [list(x) for x in UkrEximDataFrame.to_records(index=False)]


for i in range(len(UkrEximList)):
    for j in range(len(UkrEximList[i])):
        if str(UkrEximList[i][j]) == 'nan':
            UkrEximList[i][j] = 0.0

for i in UkrEximList:
      print(i)
