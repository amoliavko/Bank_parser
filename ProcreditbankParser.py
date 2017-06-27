import pandas as pd

bank = 'ProCredit'

ProCreditFile = 'statics/ПРОКРЕДИТ  БАНК.xlsx'
ProCreditOpenFile = pd.read_excel(ProCreditFile).astype(str)
ProCreditDataFrame = pd.DataFrame(ProCreditOpenFile[['Дата операцiї', 'Дебет', 'Кредит', 'Валюта', 'Призначення платежу', 'Кореспондент', 'Рахунок', 'ЄДРПОУ']])
ProCreditList = [list(x) for x in ProCreditDataFrame.to_records(index=False)]


for i in range(len(ProCreditList)):
    ProCreditList[i][0] = ProCreditList[i][0].split()[0]
    for j in range(len(ProCreditList[i])):
        if str(ProCreditList[i][j]) == 'nan':
            ProCreditList[i][j] = 0.0

for i in ProCreditList:
      print(i)
