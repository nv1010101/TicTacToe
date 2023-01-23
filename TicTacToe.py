# блок функций

def victory_check(c_v):
    # проверка ситуации выигрыша на поле , c_v  - cell value
    # проверка по горизонтали
    if a1 == a2 == a3 == c_v or b1 == b2 == b3 == c_v or c1 == c2 == c3 == c_v:
        return True
    # проверка по вертикали
    elif a1 == b1 == c1 == c_v or a2 == b2 == c2 == c_v or a3 == b3 == c3 == c_v:
        return True
    # проверка по диагонали
    elif a1 == b2 == c3 == c_v or c1 == b2 == a3 == c_v:
        return True
    else:
        return False


def draw_check():
    # проверка на ничью, если выигрышной ситуации нет и закончились свободные клетки
    list_of_cell = [a2, a3, b1, b2, b3, c1, c2, c3]
    if "-" in list_of_cell:
        return False
    else:
        return True


def field_rendering():  # отрисовка игрового поля
    print(f" \
 a b c \n\
1 {a1} {a2} {a3}\n\
2 {b1} {b2} {b3}\n\
3 {c1} {c2} {c3}\n")


def field_update(player_input):
    # проверка введенных игроком значений и изменение значения ячейки на поле
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    if player_input == 'a1' and a1 != "0" and a1 != "X":
        a1 = "X"
    elif player_input == 'a2' and a2 != "0" and a2 != "X":
        a2 = "X"
    elif player_input == 'a3' and a3 != "0" and a3 != "X":
        a3 = "X"
    elif player_input == 'b1' and b1 != "0" and b1 != "X":
        b1 = "X"
    elif player_input == 'b2' and b2 != "0" and b2 != "X":
        b2 = "X"
    elif player_input == 'b3' and b3 != "0" and b3 != "X":
        b3 = "X"
    elif player_input == 'c1' and c1 != "0" and c1 != "X":
        c1 = "X"
    elif player_input == 'c2' and c2 != "0" and c2 != "X":
        c2 = "X"
    elif player_input == 'c3' and c3 != "0" and c3 != "X":
        c3 = "X"
    else:
        print("Ошибка! Введите, пожалуйста, верное значение")

    field_rendering()


def ai_first_move():
    # первый ход ai
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, flag_ai_first_move

    random_num_1 = hash("0")  # генерация “случайных” чисел создания для непредсказуемости хода ai, если b2 занято
    random_num_2 = hash("x")

    if b2 == "-":
        b2 = "0"
    else:
        if random_num_1 > 0 and random_num_2 > 0:
            a1 = "0"
        elif random_num_1 > 0 and random_num_2 < 0:
            a3 = "0"
        elif random_num_1 < 0 and random_num_2 > 0:
            c1 = "0"
        elif random_num_1 < 0 and random_num_2 < 0:
            c3 = "0"
    flag_ai_first_move = False  # выключение флага первого хода, чтобы эта функция больше не использовалась


def ai_draw_move():
    # ход ai когда ничья неизбежна и необходимо сделать любой последний ход
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    list_of_cell = [a2, a3, b1, b2, b3, c1, c2, c3]
    counter = 0
    for x in list_of_cell:
        if x == "-":
            counter += 1
    if counter == 2:
        for x in list_of_cell:
            if x == "-":
                x = "0"
                break


def ai_move_win_check(c_v):  # c_v - cell value,
    # проверка ситуации на поле на выигрыш в следующем ходу и ход ai для победы или чтобы помешать
    global a1, a2, a3, b1, b2, b3, c1, c2, c3

    if a1 == "-" and ((a2 == c_v and a3 == c_v) or (b1 == c_v and c1 == c_v) or (b2 == c_v and c3 == c_v)):
        a1 = "0"
        return True
    elif a2 == "-" and ((a1 == c_v and a3 == c_v) or (b2 == c_v and c2 == c_v)):
        a2 = "0"
        return True
    elif a3 == "-" and ((a1 == c_v and a2 == c_v) or (b3 == c_v and c3) or (b2 == c_v and c1 == c_v)):
        a3 = "0"
        return True

    elif b1 == "-" and (((a1 == c_v and c1 == c_v) or (b2 == c_v and b3 == c_v))):
        b1 = "0"
        return True
    elif b2 == "-" and (
            (b1 == c_v and b3 == c_v) or (a2 == c_v and c2) or (a1 == c_v and c3 == c_v) or (c1 == c_v and a3 == c_v)):
        b2 = "0"
        return True
    elif b3 == "-" and ((b1 == c_v and b2 == c_v) or (a3 == c_v and c3 == c_v)):
        b3 = "0"
        return True

    elif c1 == "-" and ((a1 == c_v and b1 == c_v) or (c2 == c_v and c3) or (b2 == c_v and a3 == c_v)):
        c1 = "0"
        return True
    elif c2 == "-" and ((c1 == c_v and c3 == c_v) or (a2 == c_v and b2 == c_v)):
        c2 = "0"
        return True
    elif c3 == "-" and ((a1 == c_v and b2 == c_v) or (a3 == c_v and b3 == c_v)):
        c3 = "0"
        return True


# инициализация переменных
flag_ai_first_move = True

a1, a2, a3 = '-', '-', '-'          # пустые значения игрового поля
b1, b2, b3 = '-', '-', '-'
c1, c2, c3 = '-', '-', '-'


# скрипт
print("Добро пожаловать в игру крестики нолики! Вы играете крестиками ")
field_rendering()

while True:
    player_input = input("Ваш ход! Введите, пожалуйста, имя клетки:  ")
    field_update(player_input)

    if flag_ai_first_move:          #  if True
        ai_first_move()

    if not ai_move_win_check('0'):  # проверка ai своей победы
        ai_move_win_check('X')  # проверка ai победы игрока на след ход и попытка помешать

    field_rendering()

    if victory_check("X"):                 # проверка победы игрока
        print("Поздравляем с победой")
        break
    elif victory_check("0"):               # проверка победы ai
        print("Сожалеем, но Вы проиграли.")
        break
    elif draw_check():                     # проверка ничьи
        print("Увы, но это ничья")
        break
    else:
        continue

print("Game over")
