import pandas as pd


def file_parser(file):
    bank = 'VTB'

    VtbOpenFile = pd.read_excel(file).astype(str)
    VtbDataFrame = pd.DataFrame(VtbOpenFile)
    VtbFrameLan = len(VtbDataFrame[VtbDataFrame["БИК Банка получателя"].map(lambda x: 'nan'not in x)])
    acc = VtbDataFrame['Тип'][VtbFrameLan+1]
    VtbDataFrame = pd.DataFrame(VtbOpenFile[['Дата', 'Сумма', 'Валюта', 'Основание платежа', 'Наименование Получателя']])[:VtbFrameLan]
    VtbList = [list(x) for x in VtbDataFrame.to_records(index=False)]

    for i in range(len(VtbList)):
        VtbList[i].append(acc)
        VtbList[i].insert(0, bank)
        VtbList[i].insert(2, 0.00)

    for i in range(len(VtbList)):
        VtbList[i][1] = VtbList[i][1].split()[0]
        for j in range(len(VtbList[i])):
            if str(VtbList[i][j]) == 'nan':
                VtbList[i][j] = 0.0

    return VtbList
