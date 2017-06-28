import re
import datetime as date

# def file_parser(file):
def file_parser():

    bank = 'PaymentSystem'
    curr = 'UAH'

    count=0
    paymentList = []
    PaySystemList = []
    openFile = open('/home/user/Playground/Projects/BankParser/Bank_parser/app/static/Ощад.xlsx', 'r', encoding = 'cp1251')

    for i in openFile:
        account = re.search('Р/с пред.:\s+(\d+)', i)
        line = re.search('\A\s+(\d\.){2}\d+', i)
        end = re.search('Итого:', i)

        if account:
            acc = account.group(1)
            print(acc)
        if end:
            PaySystemList.append(paymentList)
            break

        elif not line and count>0:
            paymentList[3]+=i[23:38]
            paymentList[4]+=i[38:92]

        elif line and count>0:
            PaySystemList.append(paymentList)
            paymentList = []
            count=0

        if count == 0 and line:
            count += 1
            paymentList.append(i[17:22]+ '.'+ str(date.datetime.now().year))
            paymentList.append(i[103:111])
            paymentList.append(i[93:103])
            paymentList.append(i[23:38])
            paymentList.append(i[38:92])

    for i in range(len(PaySystemList)):
        PaySystemList[i].insert(0,bank)
        PaySystemList[i].append(acc)
        PaySystemList[i].insert(4,curr)

    for i in range(len(PaySystemList)):
            PaySystemList[i][2] = str(PaySystemList[i][2]).replace(',','.')
            PaySystemList[i][3] = str(PaySystemList[i][3]).replace(',','.')

    return PaySystemList



if __name__== '__main__':
    file = '/home/user/Playground/Projects/BankParser/Bank_parser/app/static/Ощад.xlsx'
    list = file_parser()
    for i in list:
        print(i)