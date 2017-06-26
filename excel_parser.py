from pandas import DataFrame
from pandas import read_excel, read_html

#lf1 = read_excel("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/excel1.xls")
lf1 = read_excel("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/Ощад.xlsx")
line = ''


start_k = [[x, y] for y in range(len(lf1)) for x in lf1.keys() if ('РЕЄСТР кредитових документів' in str(lf1[x][y]))]
start_d = [[x, y] for y in range(len(lf1)) for x in lf1.keys() if ('РЕЄСТР дебетових документів' in str(lf1[x][y]))]
finish = [[x, y] for y in range(len(lf1)) for x in lf1.keys() if ('Одержано:' in str(lf1[x][y]))]


bank = 'Oshchad'
rahunok = [x for x in lf1['Unnamed: 3'] if ('по рахунку' in str(x))]
invoice = rahunok[0].rsplit()[2]
currency = rahunok[0].rsplit()[3]

print(start_k, start_d, finish, sep='\n')


def find_data(start_pos, finish_pos):
    bank = 'Bank'
    for i in range(int(start_pos[0][1]), int(finish_pos[1])):
        if 'проведено банком:' in str(lf1['Unnamed: 2'][i]):
            date = lf1['Unnamed: 5'][i]
        if 'сума:' in str(lf1['Unnamed: 2'][i]):
            sum = lf1['Unnamed: 5'][i]
        if 'призначення платежу:' in str(lf1['Unnamed: 2'][i]):
            purpose = lf1['Unnamed: 5'][i]
        if 'платник:' in str(lf1['Unnamed: 2'][i]):
            payer = lf1['Unnamed: 5'][i]
    return bank, date, sum, purpose, payer,

out_list = find_data(start_k, finish[0])


wf1 = DataFrame()
# df = DataFrame(columns=('Банк', 'Дата', 'Дебет', 'Кредит'))
df = DataFrame(columns=('Банк', 'Дата', 'Дебет', 'Кредит', 'Валюта', 'Назначение', 'Агент', 'Счет'))
# df.loc[1]=''
# df.loc[2]=''
# df.loc[3]=''
# df['Банк'][1]='tesgft'
# df['Банк'][2]='test'
# df['Банк'][3]='tescdsvt'
# df['Агент'][1]=out_list[3]
# df = df.set_value(2,'Дата', 555)
for i in range(5):
    df.loc[i] = out_list


df.to_excel("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/txt_out.xlsx")
#wf1.to_excel("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/txt_out.xls")
