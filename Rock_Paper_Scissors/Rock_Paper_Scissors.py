import rps_func

print("Здравствуйте. Это игра - Камень, ножницы, бумага.\n")

question = print("Известны ли Вам правила игры? " + "Да/Нет\n")
answer = input("Ответ: ")

while answer != "Да" or "Нет":
	if answer == "Да":
		print("\nОтлично. Тогда можно начинать игру.\n")
		break
	elif answer == "Нет":
		rps_func.rules()
		break
	else:
		print("Только Да/Нет")
		answer = input("Ответ: ")

rps_func.logics()




