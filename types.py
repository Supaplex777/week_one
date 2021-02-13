a = 2
b = 0.5
print(a + b) # Задача первая

name = input('Привет как тебя зовут?\n') # Задача вторая
print(f'Привет, {name}!')

number = int(input('Привет напиши число:\n')) # Задача третья 
message = number + 10 
print(message)

name1 = input('Привет напиши свое имя друг?\n') # Задача четвертая
name2 = name.lower()
print(f'Привет {name2}. Как дела?')

print(float('1')) #Задача номер пять
#print(int('2.5')) сделать нельзя ошибка в лекции,есть иное решение:
a = float('2.5')
print(int(a))
print(bool(''))
print(bool(0))
print(bool(None))