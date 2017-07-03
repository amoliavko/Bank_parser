import pandas as pd

def file_parser(file):

    bank = 'Oshchad'
    curr = 'UAH'
    paymantList = []
    OshchadList = []
    OutOshchadList = []
    readFile = pd.read_excel(file)
    df = pd.DataFrame(readFile)



    oshadDf = df[df.columns[2:6]].astype(str)
    oshadDf = oshadDf.drop(oshadDf.columns[1:3], axis=1)
    oshadDf = oshadDf[oshadDf[oshadDf.columns[0]].isin(oshadDf[oshadDf.columns[0]].dropna())]

    TempOshchadList = [list(x) for x in oshadDf.to_records(index=False)]

    # print(oshadDf[oshadDf[oshadDf.columns[0]]].str.contains('рахунок:'))

    count = accCond = 0
    acc = ''

    for i in TempOshchadList:

        if i[0].startswith('РЕЄСТР кредитових'):
            count = 1
            accCond = 0
        elif i[0].startswith('рахунок:') and count == 1 and accCond ==0:
            acc = i[1]
            accCond = 1
        elif i[0].startswith('платник:') and count == 1:
            paymantList.append(acc)
            paymantList.append(i[1])
        elif i[0].startswith('проведено банком:') and count == 1:
            paymantList.append(i[1].split()[0])
        elif i[0].startswith('сума:') and count == 1:
            paymantList.append('0.00')
            paymantList.append(i[1].replace(u'\xa0', u'').replace(',', '.'))
        elif i[0].startswith('призначення платежу:') and count == 1:
            paymantList.append(i[1])
            OshchadList.append(paymantList)
            paymantList = []

        if i[0].startswith('РЕЄСТР дебетових'):
            count = 2
            accCond = 0
        elif i[0].startswith('рахунок:') and count == 2 and accCond == 0:
            acc = i[1]
            accCond = 1
        elif i[0].startswith('одержувач:') and count == 2:
            paymantList.append(acc)
            paymantList.append(i[1])
        elif i[0].startswith('проведено банком:') and count == 2:
            paymantList.append(i[1].split()[0])
        elif i[0].startswith('сума:') and count == 2:
            paymantList.append(i[1].replace(u'\xa0', u'').replace(',', '.'))
            paymantList.append('0.00')
        elif i[0].startswith('призначення платежу:') and count == 2:
            paymantList.append(i[1])
            OshchadList.append(paymantList)
            paymantList = []

    TempList = []
    for i in OshchadList:
        TempList.append(bank)
        TempList.append(i[2])
        TempList.append(i[3])
        TempList.append(i[4])
        TempList.append(curr)
        TempList.append(i[5])
        TempList.append(i[1])
        TempList.append(i[0])
        OutOshchadList.append(TempList)
        TempList = []
    
    for i in range(len(OutOshchadList)):
        for j in range(len(OutOshchadList[i])):
            if str(OutOshchadList[i][j]) == 'nan':
                OutOshchadList[i][j] = ''

    for i in range(len(OutOshchadList)):
        for j in range(2, 4):
            OutOshchadList[i][j] = str(OutOshchadList[i][j]).replace('.', ',')

    return OutOshchadList
