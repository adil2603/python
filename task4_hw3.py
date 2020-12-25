def my_pow(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Введите действительное положительное число и целое отрицательное число"
    return res


print(my_pow(7.1, -4))