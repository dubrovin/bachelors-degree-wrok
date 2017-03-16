# coding=utf-8
import time


class container:

    def __init__(self, i_index, j_index):
        self.i = i_index
        self.j = j_index


def my_print(arr):
    for i in arr:
        print i

# поиск минимального элемента в строке
# возвращает список минимальных э-ов каждой строки


def find_min_in_row(arr):
    min = []
    for i in range(len(arr)):
        min.append(arr[i][0])
        for j in range(len(arr[i])):
            if a[i][j] < min[i]:
                min[i] = a[i][j]
    return min

# поиск минимального элемента в столбце
# возвращает список минимальных э-ов каждого столбца


def find_min_in_colum(arr):
    min = []
    for i in range(len(arr)):
        min.append(arr[0][i])
        for j in range(len(arr[i])):
            if a[j][i] < min[i]:
                min[i] = a[j][i]
    return min

# вычитает из каждого элемента строки минимальный э-т строки
# edit - массив минимальных элементов


def rows_edit(arr, edit):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] -= edit[i]
    return arr

# вычитает из каждого элемента столбца минимальный э-т столбца
# edit - массив минимальных элементов

def colums_edit(arr, edit):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[j][i] -= edit[i]
    return arr

# формируем список нулей со звездочкой


def check_nulls(arr, stars):
    stars_copy = stars[::]
    size = len(arr)
    for i in range(size):
        for j in range(size):
            flag = False
            if arr[i][j] == 0:
                # если ист пуст, то просто добавляем элемент
                if not stars_copy:
                    stars_copy.append(container(i, j))
                else:
                    # иначе проверяем вхождение строки и столбца для каждого
                    # нуля
                    for k in stars_copy:
                        for d in range(size):
                            if k.i != i or k.j != d:
                                continue
                            else:
                                flag = True
                                break
                        for d in range(size):
                            if k.i != d or k.j != j:
                                continue
                            else:
                                flag = True
                                break
                    # если вхождений нет, то добавляем элемент в список
                    if not flag:
                        stars_copy.append(container(i, j))
    return stars_copy

# закрываем столбцы/строки
# если flag == True, закрываем столбцы, иначе - строки


def close_element(old, arr, flag):
    old_copy = old[::]
    if flag:
        for s in arr:
            old_copy.append(s.j)
    else:
        for s in arr:
            old_copy.append(s.i)
    return old_copy

# открываем столбцы/строки
# если flag == True, открываем столбцы, иначе - строки


def open_element(old, arr, flag):
    old_copy = old[::]
    if flag:
        for s in arr:
            for q in old_copy:
                if s.j == q:
                    old_copy.remove(q)
                else:
                    continue
    else:
        for s in arr:
            for q in old_copy:
                if s.i == q:
                    old_copy.remove(q)
                else:
                    continue
    return old_copy


# поиск незакрытых нулей
def check_unclose_nulls(arr, closed_columns, closed_rows):
    size = len(arr)
    open_nulls = []
    for i in range(size):
        for j in range(size):
            flag = False
            if arr[i][j] == 0:
                for d in closed_columns:
                    if d == j:
                        flag = True
                        break
                for d in closed_rows:
                    if d == i:
                        flag = True
                        break
                if not flag:
                    open_nulls.append(container(i, j))
    if open_nulls:
        return open_nulls
    else:
        return False

# проверка, есть ли нули со звездочкой в строке с незакрытым нулем


def check_stars_for_unclose_nulls(unclose_nulls, stars):
    flag = False
    star = []
    if unclose_nulls:
        for u in unclose_nulls:
            for s in stars:
                if u.i == s.i:
                    flag = True
                    star.append(s)
                    break
                else:
                    continue
        if flag:
            return star
        else:
            return False


# поиск минимального из незакрытых лементов


def find_min_in_unclose(arr, closed_columns, closed_rows):
    min = 1000
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if (i in closed_rows or j in closed_columns):
                continue
            else:
                if arr[i][j] < min:
                    min = arr[i][j]
    return min

# добавить А к каждому элементу закрытой строки
# так же сразу вычитаем А из констант приведения строк


def a_plus_to_close_row(arr, a, closed_rows, min_rows):
    copy_arr = arr[::]
    for i in closed_rows:
        # так же сразу вычитаем А из констант приведения строк
        min_rows[i] -= a
        for j in range(len(arr)):
            copy_arr[i][j] += a
    return copy_arr

# вычесть А из каждого открытого столбца
# так же сразу прибавляем А к константам приведения столбцов


def a_minus_open_column(arr, a, closed_columns, min_colums):
    copy_arr = arr[::]
    for i in range(len(arr)):
        if i not in closed_columns:
            # так же сразу прибавляем А к константам приведения столбцов
            min_colums[i] += a
            for j in range(len(arr)):
                copy_arr[j][i] -= a
    return copy_arr

# checking closed columns for answer


def is_answer(arr, closed_columns):
    if len(closed_columns) == len(arr):
        return True
    else:
        return False


def part_6_2(Z, stars):
    flag = False
    tmp = stars[0]
    for s in stars:
        if s.j == Z.j:
            flag = True
            tmp = s
        else:
            continue
    if flag:
        return tmp
    else:
        return False


def part_6_3(Z, lines):
    flag = False
    for s in lines:
        if s.i == Z.i:
            flag = True
            tmp = s
    if flag:
        return tmp
    else:
        return False


def part_6_4(stars, lines, z_list):
    for s in stars:
        for z in z_list:
            if z.i == s.i and z.j == s.j:
                stars.remove(s)
    for s in lines:
        for z in z_list:
            if z.i == s.i and z.j == s.j:
                stars.append(s)
    lines = []


def my_fun(arr):
    stars = []  # список нулей со звездочками
    closed_columns = []  # закрытые стлобцы
    closed_rows = []  # закрытые строки
    lines = []  # список нулей со штрихами
    z_list = []  # список ряда
    print "Исходный массив:"
    my_print(arr)
    min_rows = find_min_in_row(arr)  # нашли мин в строках п.1
    edited_arr = rows_edit(arr, min_rows)  # вычли мин из строк п.1.1
    min_colums = find_min_in_colum(edited_arr)  # нашли мин в столбцах п.2
    # вычли мин из столбцов п.2.1
    edited_arr = colums_edit(edited_arr, min_colums)
    print "Измененный массив:"
    my_print(edited_arr)
    stars = check_nulls(edited_arr, stars)  # нашли нули со звезд п.3
    print "Массив индексов нулей помеченных звездочкой:"
    for c in stars:
        print c.i, c.j
    # закрываем столбцы п.4
    closed_columns = close_element(closed_columns, stars, True)
    answer = not is_answer(arr, closed_columns)
    # time.sleep(1)
    while answer:
        print "Ответ не найден, идем дальшe..."
        # ищем незакрытый нуль п.5
        unclose_nulls = check_unclose_nulls(
            edited_arr, closed_columns, closed_rows)
        while unclose_nulls:
            # есть незакрытый нуль, помечаем его штрихом
            print "Есть незакрытый нуль..."
            for t in unclose_nulls:
                print "Его индексы: {} {}".format(t.i, t.j)
                lines.append(t)
            # проверяем наличием 0* в строке с 0'
            # time.sleep(1)
            buf = check_stars_for_unclose_nulls(unclose_nulls, stars)
            if buf:  # Если в строке с 0' есть 0*
                print "Есть нуль со здвездочкой"
                # открываем столбец
                closed_columns = open_element(closed_columns, buf, True)
                # закрываем строку
                closed_rows = close_element(closed_rows, buf, False)
                # ищем незакрытые нули
                unclose_nulls = check_unclose_nulls(
                    edited_arr, closed_columns, closed_rows)
                buf = check_stars_for_unclose_nulls(unclose_nulls, stars)
                # time.sleep(1)
            else:
                print "Нет нуля со звездочкой"
                print "Выполняем пункт 6.1"
                Z = unclose_nulls[0]
                z_list.append(Z)
                # time.sleep(1)
                while part_6_2(Z, stars):
                    print "Выполняем пункт 6.2"
                    Z = part_6_2(Z, stars)
                    z_list.append(Z)
                    print "Выполняем пункт 6.3"
                    Z = part_6_3(Z, lines)
                    # time.sleep(1)
                else:
                    print "Выполняем пункт 6.4"
                    part_6_4(stars, lines, z_list)
                    closed_columns = []
                    closed_rows = []
                    # time.sleep(1)
                    closed_columns = close_element(closed_columns, stars, True)
                    answer = not is_answer(arr, closed_columns)
                    break
        else:
            # нашли мин среди незакрытых элементов
            A = find_min_in_unclose(arr, closed_columns, closed_rows)
            # добавили А к каждому э-у закр строки
            # вычли А из констант приведения строки
            edited_arr = a_plus_to_close_row(
                edited_arr, A, closed_rows, min_rows)
            # вычли А из каждого э-а откр столбца
            # добавили А к константам приведения столбца
            edited_arr = a_minus_open_column(
                edited_arr, A, closed_columns, min_colums)
            print "Массив после процедуры пунтка 7"
            my_print(edited_arr)
            closed_columns = close_element(closed_columns, stars, True)
            answer = not is_answer(arr, closed_columns)
    else:
        print "Ответ: "
        for s in stars:
            print s.i, s.j

a = [
    [5, 1, 7, 2, 4],
    [3, 2, 5, 8, 3],
    [4, 2, 6, 3, 5],
    [5, 4, 2, 3, 8],
    [7, 3, 2, 5, 4],
]

b = [
    [4, 3, 8, 5],
    [1, 7, 9, 3],
    [6, 4, 5, 2],
    [2, 8, 7, 3],
]

c = [
    [10, 7, 1],
    [7, 10, 1],
    [5, 5, 10],
]
my_fun(a)
