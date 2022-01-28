def func(line):##создание функции
  count = 0 ##счётчик
  for i in line:
    if i == '':
      count += 1 ##подсчёт символов
  print("Amount of in your line is ", count, ".") ##вывод
  line = line.replace("", " ") ##заменяем на пробелы
  print("Yout final result is " +line) ##вывод итога

line = input("Input your string")
func(line)