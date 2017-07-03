import pandas as pd
import re


def file_parser(file):

    bank = 'Privat'

    PrivatOpenFile = pd.read_excel(file).astype(str)
    PrivatDataFrame = pd.DataFrame(PrivatOpenFile)
    linkText = PrivatDataFrame[PrivatDataFrame.columns[0]].name
    link = re.search('Выписка по счету № (\w+)', linkText).group(1)

    PrivatDataFrame = pd.DataFrame(PrivatOpenFile[['Unnamed: 1', 'Unnamed: 4', 'Unnamed: 3', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 8', 'Unnamed: 7']])[2:-1]

    PrivatList = [list(x) for x in PrivatDataFrame.to_records(index=False)]

    for i in range(len(PrivatList)):
        PrivatList[i].insert(0, bank)
        PrivatList[i].insert(7, link)

    for i in range(len(PrivatList)):
        PrivatList[i][1] = PrivatList[i][1].split()[0]
        for j in range(2, 4):
            if str(PrivatList[i][j]) == 'nan':
                PrivatList[i][j] = '0,00'
            PrivatList[i][j] = str(PrivatList[i][j]).replace('.', ',')

    for i in range(len(PrivatList)):
        for j in range(len(PrivatList[i])):
            if str(PrivatList[i][j]) == 'nan':
                PrivatList[i][j] = ''

    return PrivatList
