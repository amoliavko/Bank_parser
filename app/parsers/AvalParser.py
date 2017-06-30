import pandas as pd


def file_parser(file):

    bank = 'Aval'
    AvalOpenFile = pd.read_excel(file).astype(str)
    AvalDataFrame = pd.DataFrame(AvalOpenFile[['Дата операцiї', 'Дебет', 'Кредит', 'Валюта', 'Призначення платежу', 'Кореспондент', 'Рахунок', 'ЄДРПОУ кореспондента']])
    AvalDict = AvalDataFrame.to_dict()

    AvalList = [list(x) for x in AvalDataFrame.to_records(index=False)]


    for i in range(len(AvalList)):
        AvalList[i].insert(0,bank)


    for i in range(len(AvalList)):
        AvalList[i][1] = AvalList[i][1].split()[0]
        AvalList[i][2] = str(AvalList[i][2]).replace('.', ',')

        for j in range(len(AvalList[i])):
            if str(AvalList[i][j]) == 'nan':
                AvalList[i][j] = '0,0'

    return AvalList
