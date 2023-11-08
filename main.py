# def two_number_division(number_one: int, number_two: int) -> float:
#     try:
#         return number_one / number_two
#     except Exception as err:
#         print(f"You got {err} error!")

# def betkas(number_one: int, number_two: int) -> float:
#     answer_number = two_number_division(number_one, number_two)
#     if not answer_number:
#         return 0    
#     return answer_number ** 2



# # two_number_division(4, 0)
# print(betkas(4, 0))



# Create a program which takes a sentence as your birth dau (YYYY:MM:DD)
# The program should return sum of all numbers, bigest and lowest number division 
# and days with power of month (dd ** mm)
# The code should be structured correctly: functions, error handling and logging.
from typing import List
import datetime


def is_date_correct(birth_date: str) -> str:
    try:
        string_date_correct = datetime.datetime.strptime(birth_date, "%Y:%m:%d")
        return birth_date
    except ValueError:
        print("Date invalid")

def date_string_to_list(string_date: str) -> List[int]:
    list_of_int: List[int] = [int(char) for char in string_date if char.isdigit()]
    return list_of_int

def date_string_to_months_days(string_date: str) -> int:
    list: List[int] = [int(chars) for chars in string_date.split(":")]
    days_power_months: int = list[-1] ** list[-2]
    return days_power_months
    
def sum_of_list(list_with_integers: List[int]) -> int:
    list_sum: int = sum(list_with_integers)
    return list_sum

def list_high_low_division(list_with_integers: List[int]) -> float:
    try:
        high_low_division: float = max(list_with_integers) / min(list_with_integers)
        return high_low_division
    except ZeroDivisionError:
        print("Division by zero is not possible")
    
if __name__ == "__main__":
    birth_date = input("Please provide your birth date in format 'YYYY:MM:DD' ")
    new_date = is_date_correct(birth_date)
    if new_date:
        list_with_integers = date_string_to_list(new_date)
        division = list_high_low_division(list_with_integers)
        power = date_string_to_months_days(new_date)
        sum_of = sum_of_list(list_with_integers)
        print(f"Bigest and lowest number division is {division}" )
        print(f"Days with power of month is {power}")
        print(f"Sum of all numbers is {sum_of}")
