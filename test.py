import pandas as pd

table = pd.read_html('https://books.toscrape.com/catalogue/the-requiem-red_995/index.html')
new_table = []
table = str(table[0]).split('  ')

new_table = [elem for elem in table if len(str(elem)) > 0]
# for elem in table:
#     if len(str(elem)) > 0:
#         new_table.append(elem)
del new_table[0]
del new_table[0]
upc = new_table[1][:-2]
price_ex_taxe = new_table[5][:-2]
price_with_taxe = new_table[7][:-2]
nb_stock = new_table[11][:-2]
print(upc)
print(price_ex_taxe)
print(price_with_taxe)
print(nb_stock)