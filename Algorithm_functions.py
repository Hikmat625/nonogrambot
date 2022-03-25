def testing(i):
    print("working" + str(i))


def finput(arr, size):
    """
    :param arr:
    :param size:
    :return:
    """
    for i in range(size):
        arr.append(str(input()).split())
        arr[i] = [int(x) for x in arr[i]]


def fprint(arr):
    for i in arr:
        print(i)


def check_for_fulls(arr, size):
    """
    :param arr:
    :param size:
    :return:
    """
    return_arr = []
    for i in range(len(arr)):
        if sum(arr[i]) + len(arr[i]) - 1 == size:
            return_arr.append(i)
    return return_arr


def draw(arr, x, y, n):
    """
    :param arr:
    :param x:
    :param y:
    :param n:
    :return:
    """
    arr[x][y] = n


def draw_horizontal_line(arr, list, y):
    changed_line = []
    for i in list:
        for j in range(i):
            changed_line.append(1)
        changed_line.append(2)
    changed_line.pop()
    arr[y] = changed_line


def fill_all_full_rows(arr, input_list, fulls_list):
    """

    :param arr:
    :param input_list:
    :param fulls_list:
    :return:
    """
    for i in range(len(fulls_list)):
        draw_horizontal_line(arr, input_list[fulls_list[i]], fulls_list[i])


def draw_vertical_line(arr, list, x):
    """
    :param arr:
    :param list:
    :param x:
    :return:
    """
    changed_column = []
    for i in list:
        for j in range(i):
            changed_column.append(1)
        changed_column.append(2)
    changed_column.pop()
    for i in range(len(changed_column)):
        arr[i][x] = changed_column[i]


def fill_all_full_columns(arr, input_list, fulls_list):
    """
    :param arr:
    :param input_list:
    :param fulls_list:
    :return:
    """
    for i in range(len(fulls_list)):
        draw_vertical_line(arr, input_list[fulls_list[i]], fulls_list[i])


def gap_in_list(input_list):
    counter = 0
    counters = [0]
    for i in input_list:
        if i == 1:
            counters.append(counter)
            counter = 0
        if i == 2:
            counters.append(counter)
            counter = 0
        if i == 0:
            counter = counter + 1
    return max(counters)


def fill_gaps_between_for_1_digit_rows(arr, input_list):
    for i in range(len(input_list)):
        started = False
        if len(input_list[i]) == 1 and input_list[i][0] >= gap_in_list(input_list[i]):
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    started = not started
                    if not started:
                        break
                if started and arr[i][j] == 0:
                    arr[i][j] = 1


def testver(arr, input_list):
    for i in range(len(input_list)):
        temp = 0
        counter = 0
        status = True
        if len(input_list[i]) == 1 and input_list[i][0] >= gap_in_list(arr[i]):
            while status:
                if temp > 13:
                    break
                if(arr[i][temp] == 1 and arr[i][temp + 1] == 0):
                    status = False
                temp += 1
            while counter <= gap_in_list(arr[i]):
                if temp + counter < len(arr):
                    arr[i][temp + counter] = 1
                    counter += 1


def bottom_guided_columns(arr, columns):
    """
    :param arr:
    :param columns:
    :return:
    """
    temp = 0
    for i in range(len(arr[-1])):
        if arr[-1][i] == 1:
            for j in range(columns[i][-1]):
                arr[-1 - j][i] = 1
                temp = j
            if j < len(arr) - 1:
                arr[-2 - temp][i] = 2


def top_guided_columns(arr, columns):
    for i in range(len(arr[0])):
        if arr[0][i] == 1:
            for j in range(columns[i][0]):
                arr[j][i] = 1
                temp = j
            if j < len(arr) - 1:
                arr[1 + temp][i] = 2


def left_guided_rows(arr, rows):
    for i in range(len(arr)):
        if arr[i][0]:
            for j in range(rows[i][0]):
                arr[i][j] = 1
                temp = j
            if j < len(arr) - 1:
                arr[i][temp + 1] = 2


'''
def gamearray_to_numbers(arr):
    outputs = []
    output = []
    counter = 0
    for i in arr:
        for j in i:
            if j == 0:
                if counter != 0:
                    output.append(counter)
                    counter = 0
            if j == 1:
                counter = counter + 1
            if j == 2:
                if counter != 0:
                    output.append(counter)
                    counter = 0
        if counter != 0 and counter != 2:
            output.append(counter)
            counter = 0
        outputs.append(output)
    return outputs
'''
