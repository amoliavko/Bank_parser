import pandas as pd


def file_parser(file):
    bank = 'ProCredit'

    ProCreditOpenFile = pd.read_excel(file).astype(str)
    ProCreditDataFrame = pd.DataFrame(ProCreditOpenFile[['Дата операцiї', 'Дебет', 'Кредит', 'Валюта', 'Призначення платежу', 'Кореспондент', 'Рахунок', 'ЄДРПОУ']])
    ProCreditList = [list(x) for x in ProCreditDataFrame.to_records(index=False)]


    for i in range(len(ProCreditList)):
        ProCreditList[i].insert(0, bank)

    for i in range(len(ProCreditList)):
        ProCreditList[i][1] = ProCreditList[i][1].split()[0]
        for j in range(2, 4):
            if str(ProCreditList[i][j]) == 'nan':
                ProCreditList[i][j] = '0,00'
            ProCreditList[i][j] = str(ProCreditList[i][j]).replace('.', ',')
            ProCreditList[i][j] = str(ProCreditList[i][j]).replace('.', ',')

    for i in range(len(ProCreditList)):
        for j in range(len(ProCreditList[i])):
            if str(ProCreditList[i][j]) == 'nan':
                ProCreditList[i][j] = ''

    return ProCreditList
