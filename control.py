import oppereit as opp
import view
import os

def buttun_click():
    type_opp = input("Ввеидет 1 для счета вещественных чисел,\n"
                  "Или 0 для счета комплексных чисел:\n")
    os.system('cls')
    if type_opp=="1":
        zeloe()
    elif type_opp=="0":
        complexnoe()
    else:
        print("Введено не верное значение")
        buttun_click()
    

def zeloe():
    print("Модуль вещественных чисел")
    value_a = view.get_value_ves()
    value_b = view.get_value_ves()
    opp.init(value_a, value_b)
    operator = input("Введите  оперетор (+,-,*,/,//,%)\n")
    if operator == "+":
        result = opp.sum()
        view.view_data(result)
    elif operator == "-":
        result = opp.minus()
        view.view_data(result)
    elif operator == "*":
        result = opp.mult()
        view.view_data(result)
    elif operator == "/":
        result = opp.dif()
        view.view_data(result)
    elif operator == "//":
        result = opp.dif_2()
        view.view_data(result)
    elif operator == "%":
        result = opp.dif_3()
        view.view_data(result)

def complexnoe():
    print("Модуль комплексных чисел")
    value_a = view.get_value_com()
    value_b = view.get_value_com()
    opp.init(value_a, value_b)
    operator = input("Введите  оперетор (+,-,*,/)\n")
    if operator == "+":
        result = opp.sum()
        view.view_data(result)
    elif operator == "-":
        result = opp.minus()
        view.view_data(result)
    elif operator == "*":
        result = opp.mult()
        view.view_data(result)
    elif operator == "/":
        result = opp.dif()
        view.view_data(result)

