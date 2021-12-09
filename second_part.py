import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv")
list_name = df['CARGO'].unique()
price = []
weight = []
quantity = []
for i in list_name:
    price.append(sum(df[df['CARGO'] == i]['PRICE'].tolist()))
    weight.append(sum(df[df['CARGO'] == i]['WEIGHT'].tolist()))
    quantity.append(len(df[df['CARGO'] == i]['CARGO'].tolist()))
dict_price = {}
for i in range(0, len(list_name)):
    dict_price[list_name[i]] = price[i]
dict_weight = {}
for i in range(0, len(list_name)):
    dict_weight[list_name[i]] = weight[i]
dict_quantity = {}
for i in range(0, len(list_name)):
    dict_quantity[list_name[i]] = quantity[i]

# первый график
bar_numbers = range(len(dict_price))
labels = list(dict_price.keys())
values = list(dict_price.values())
fig, ax = plt.subplots()
ax.set_title('Полная стоимость')
ax.bar(bar_numbers, values)
ax.set_xticks(bar_numbers)
ax.set_xticklabels(labels)
plt.show()

# второй график
bar_numbers = range(len(dict_weight))
labels = list(dict_weight.keys())
values = list(dict_weight.values())
fig, ax = plt.subplots()
ax.set_title('Полная масса перевезённых грузов')
ax.bar(bar_numbers, values)
ax.set_xticks(bar_numbers)
ax.set_xticklabels(labels)
plt.show()

# третий график
bar_numbers = range(len(dict_quantity))
labels = list(dict_quantity.keys())
values = list(dict_quantity.values())
fig, ax = plt.subplots()
ax.set_title('Количесиво рейсов')
ax.bar(bar_numbers, values)
ax.set_xticks(bar_numbers)
ax.set_xticklabels(labels)
plt.show()