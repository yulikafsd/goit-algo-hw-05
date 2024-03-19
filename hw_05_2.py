from typing import Callable
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    # приймає рядок як аргумент 
    # Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
    pattern = r"\s(\d+\.\d+)\s"
    numbers = re.findall(pattern, text)
    # повертає генератор, що ітерує по всіх дійсних числах у тексті
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    # приймає генератор як аргумент при виклику
    # використовує генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку 
    profit = 0
    for sum in func(text):
        profit += sum
    return profit

if __name__ == '__main__':
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
