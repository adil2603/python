def div(n_1, n_2):
    try:
        n_1, n_2 = int(n_1), int(n_2)
        div_num = n_1 / n_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero"
    return round(div_num, 2)


print(div(input("Введите первое число: "), input("Введите второе число: ")))