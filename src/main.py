from db.connectors import test_connection, engine
from models.models import TrueSuitability, FalseSuitability, RawData

test_connection()
table_list = []
raw_data = RawData()
table_list.append(raw_data)
true_suitability = TrueSuitability()
table_list.append(true_suitability)
false_suitability = FalseSuitability()
table_list.append(false_suitability)

key= int(input("Введите значение: 1- создать таблицы, 0- удалить таблицы:"))
if key == 1:
    for i in table_list:
        i.metadata.create_all(bind= engine)
        #i.metadata.drop_all(bind= engine)
elif key == 0:
    for i in table_list:
        #i.metadata.create_all(bind= engine)
        i.metadata.drop_all(bind= engine)
print()
