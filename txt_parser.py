from pandas import read_table, DataFrame

rf1 = read_table("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/txt.txt", encoding='CP1251')


#print(rf1)

##wf1 = rf1.to_csv("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/txt_out", sep='\t', encoding='utf-8')

#rf1.to_csv("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/txt_out")

country = [u'Украина',u'РФ',u'Беларусь',u'РФ',u'РФ']

wf1 = DataFrame()
wf1.insert(0,'count',country)


wf1.to_csv("/media/a_m/Wdisk/Python/Projects/Bank_parser/example/txt_out")


print(type(rf1),'\n', type(wf1))