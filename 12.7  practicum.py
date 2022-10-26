money=float(input("Введите сумму для депозита: "))
deposit=[]
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
liststavok=per_cent.values()
#print(liststavok)
for i in liststavok:
    #print(i*money)
    deposit.append(int(i*money/100))
    
print("Возможные суммы для дохода:", deposit)
print("Максимальная сумма, которую вы можете заработать - " , max(deposit))
