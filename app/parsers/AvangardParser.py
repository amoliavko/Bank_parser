import pandas as pd


def file_parser(file):

    bank = 'Avangard'
    curr = 'RUB'

    AvangardOpenFile = pd.read_excel(file).astype(str)
    AvangardDataFrame = pd.DataFrame(AvangardOpenFile)

    acc = AvangardDataFrame[AvangardDataFrame.columns[12]][0]

    startPos = 0
    for i in AvangardDataFrame[AvangardDataFrame.columns[2]]:
        startPos += 1
        if str(i).startswith('Дата док-та'):
            break

    finishPos = 0
    for i in AvangardDataFrame[AvangardDataFrame.columns[2]]:
        finishPos += 1
        if str(i).startswith('Итого:'):
            finishPos -= 1
            break

    del_list = ['nan', 'Дата док-та']
    AvangardDataFrame = AvangardDataFrame.iloc[startPos:finishPos]
    AvangardDataFrame = pd.DataFrame(AvangardDataFrame[['ПАО АКБ "АВАНГАРД"', 'Unnamed: 26', 'Unnamed: 29', 'Unnamed: 31', 'Unnamed: 21']])
    AvangardDataFrame = AvangardDataFrame[~AvangardDataFrame['ПАО АКБ "АВАНГАРД"'].isin(del_list)]
    AvangardList = [list(x) for x in AvangardDataFrame.to_records(index=False)]

    for i in range(len(AvangardList)):
        AvangardList[i].insert(0, bank)
        AvangardList[i].append(acc)
        AvangardList[i].insert(4, curr)

    for i in range(len(AvangardList)):
        AvangardList[i][1] = AvangardList[i][1].split()[0]
        AvangardList[i][2] = str(AvangardList[i][2]).replace(',', '')
        AvangardList[i][3] = str(AvangardList[i][3]).replace(',', '')
        for j in range(len(AvangardList[i])):
            if str(AvangardList[i][j]) == 'nan':
                AvangardList[i][j] = ''

    for i in range(len(AvangardList)):
        for j in range(2, 4):
            if str(AvangardList[i][j]) == '':
                AvangardList[i][j] = '0,00'
            AvangardList[i][j] = str(AvangardList[i][j]).replace('.', ',')

    return AvangardList
