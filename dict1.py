dict1 = { 'city': 'Moscow', # Cоздал словарь 
'temperature': 20 
}
print(dict1['city']) # вывел на экран значение key: city
dict1['temperature'] = 5 # Изменил значение key :temperature на 5
print(dict1) # Вывел на экран словарь 
print(dict1.get('country')) # Проверил наличие ключа country
print(dict1.get('country','Россия')) # Вывел значение по умолчанию Россия для country
dict1['date'] = "27.05.2019" # Добавил в словарь ключ data и его значение
print(dict1) # Вывел на зкран 