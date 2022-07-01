per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
dict = per_cent
money = input("Введите сумму:")
deposit = []
for value in dict: deposit.append (dict[value] * float(money) / 100)
print (deposit)
print ("Максимальная сумма которую вы можете заработать: [%d]" % max(deposit))
