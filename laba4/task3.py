from enum import Enum


class Operation(Enum):
    Amount = "+"
    Difference = "-"
    Multiply = "*"
    Divide = "/"


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))
operation_input = input("Введите тип операции (+, -, *, /): ")


def calculate(firstNumber, secondNumber, operation):
    if operation == Operation.Amount:
        result = firstNumber + secondNumber
    elif operation == Operation.Difference:
        result = firstNumber - secondNumber
    elif operation == Operation.Multiply:
        result = firstNumber * secondNumber
    elif operation == Operation.Divide:
        if secondNumber == 0:
            return "Ошибка: деление на ноль!"
        result = firstNumber / secondNumber
    else:
        return "Нет такой операции"

    return f"{firstNumber} {operation.value} {secondNumber} = {result}"


try:
    operation = Operation(operation_input)
    result = calculate(firstNumber, secondNumber, operation)
    print(result)
except ValueError:
    print("Ошибка: неверный тип операции. Пожалуйста, используйте +, -, *, /.")