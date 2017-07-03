import pandas as pd


def file_parser(file):

    bank = 'Centercredit'
    curr = 'KZT'

    CentercreditOpenFile = pd.read_excel(file).astype(str)
    CentercreditDataFrame = pd.DataFrame(CentercreditOpenFile)

    acc_pos = 0
    for i in CentercreditDataFrame[CentercreditDataFrame.columns[0]]:
        acc_pos+=1
        if str(i).startswith('ИИК'):
            acc = i.split()[1]

    startPos = 0
    for i in CentercreditDataFrame[CentercreditDataFrame.columns[0]]:
        startPos += 1
        if str(i).startswith('Реттік'):
            break

    finishPos = 0
    for i in CentercreditDataFrame[CentercreditDataFrame.columns[0]]:
        finishPos += 1
        if str(i).startswith('Жиынтығы'):
            finishPos -= 1
            break

    CentercreditDataFrame = CentercreditDataFrame.iloc[startPos:finishPos]
    CentercreditDataFrame = pd.DataFrame(CentercreditDataFrame[['Unnamed: 1', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 11', 'Unnamed: 5']])
    CentercreditList = [list(x) for x in CentercreditDataFrame.to_records(index=False)]

    for i in range(len(CentercreditList)):
        CentercreditList[i].insert(0,bank)
        CentercreditList[i].append(acc)
        CentercreditList[i].insert(4,curr)

    for i in range(len(CentercreditList)):
        for j in range(2, 4):
            if str(CentercreditList[i][j]) == 'nan':
                CentercreditList[i][j] = '0,00'
            CentercreditList[i][j] = str(CentercreditList[i][j]).replace(',', '')
            CentercreditList[i][j] = str(CentercreditList[i][j]).replace('.', ',')
            CentercreditList[i][j] = str(CentercreditList[i][j]).replace('.', ',')
            
    for i in range(len(CentercreditList)):
        for j in range(len(CentercreditList[i])):
            if str(CentercreditList[i][j]) == 'nan':
                CentercreditList[i][j] = ''

    return CentercreditList
