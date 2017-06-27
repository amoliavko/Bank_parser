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

    AvangardDataFrame = AvangardDataFrame.iloc[startPos:finishPos]
    AvangardDataFrame = pd.DataFrame(AvangardDataFrame[['ПАО АКБ "АВАНГАРД"', 'Unnamed: 26', 'Unnamed: 29', 'Unnamed: 31', 'Unnamed: 21']])
    AvangardList = [list(x) for x in AvangardDataFrame.to_records(index=False)]

    for i in range(len(AvangardList)):
        AvangardList[i].insert(0,bank)
        AvangardList[i].append(acc)
        AvangardList[i].insert(4,curr)



    for i in range(len(AvangardList)):
        AvangardList[i][1] = AvangardList[i][1].split()[0]
        for j in range(len(AvangardList[i])):
            if str(AvangardList[i][j]) == 'nan':
                AvangardList[i][j] = 0.0
            AvangardList[i][j] = str(AvangardList[i][j]).replace(',','')

    return AvangardList
