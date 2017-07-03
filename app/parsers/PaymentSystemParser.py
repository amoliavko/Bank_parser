import re
import datetime as date


def file_parser(file):

    bank = 'PaymentSystem'
    curr = 'UAH'

    count=0
    paymentList = []
    PaySystemList = []
    openFile = open(file, 'r')

    for i in openFile:
        account = re.search('Р/с пред.:\s+(\d+)', i)
        line = re.search('\A\s+(\d\.){2}\d+', i)
        end = re.search('Итого:', i)

        if account:
            acc = account.group(1)

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
        PaySystemList[i].insert(4, curr)

    openFile.close()

    for i in range(len(PaySystemList)):
        for j in range(2, 4):
            PaySystemList[i][j] = str(PaySystemList[i][j]).replace('.', ',')
        for j in range(len(PaySystemList[i])):
            PaySystemList[i][j] = re.sub('\s+', ' ', PaySystemList[i][j])

    for i in range(len(PaySystemList)):
        for j in range(len(PaySystemList[i])):
            if str(PaySystemList[i][j]) == 'nan':
                PaySystemList[i][j] = '0,00'

    for i in range(len(PaySystemList)):
        PaySystemList[i][5], PaySystemList[i][6] = PaySystemList[i][6], PaySystemList[i][5]

    return PaySystemList

if __name__== '__main__':
    file = '/home/user/Playground/Projects/BankParser/Bank_parser/app/static/Платежные сисетмы.txt'
    PaySystemList = file_parser(file)
    for i in PaySystemList:
        print(i)


