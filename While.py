# While
# Just Simple program, i learned it. 
number = 77
running = True
while running:
		guess = int(input('Введите целое число : '))
		if guess == number:
			print('Поздравляю, вы нашли загаданное число!')
			running = False #это останавливает цикл while
		elif guess < number:
			print('Не верно, ваше число меньше загаданного.')
		else:
			print('Не верно, ваше число больше загаданного.')
else:
		print('Cледующее число')
next = 19
running = True
while running:
		guess = int(input('Введите целое число : '))
		if guess == next:
			print('Поздравляю, вы нашли загаданное число!')
			running = False #это останавливает цикл while
		elif guess < next:
			print('Не верно, ваше число меньше загаданного.')
		else:
			print('Не верно, ваше число больше загаданного.')
else:	
    print('Вы угадали', number, 'и', next,'! Вы молодец!')
