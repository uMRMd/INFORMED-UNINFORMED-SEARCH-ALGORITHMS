def add(a, b):
    return a+b


def second_min(number_list):
    x = insertion_sort(number_list)
    x = x[1]
    return x


def insertion_sort(number_list):
    i = 1
    while i < len(number_list):
        j = i
        while j > 0 and number_list[j-1] > number_list[j]:
            temp = number_list[j]
            number_list[j] = number_list[j-1]
            number_list[j-1] = temp
            j = j-1

        i = i+1
    return number_list
