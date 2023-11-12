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
# from typing import List
# import datetime


# def is_date_correct(birth_date: str) -> str:
#     try:
#         string_date_correct = datetime.datetime.strptime(birth_date, "%Y:%m:%d")
#         return birth_date
#     except ValueError:
#         print("Date invalid")

# def date_string_to_list(string_date: str) -> List[int]:
#     list_of_int: List[int] = [int(char) for char in string_date if char.isdigit()]
#     return list_of_int

# def date_string_to_months_days(string_date: str) -> int:
#     list: List[int] = [int(chars) for chars in string_date.split(":")]
#     days_power_months: int = list[-1] ** list[-2]
#     return days_power_months
    
# def sum_of_list(list_with_integers: List[int]) -> int:
#     list_sum: int = sum(list_with_integers)
#     return list_sum

# def list_high_low_division(list_with_integers: List[int]) -> float:
#     try:
#         high_low_division: float = max(list_with_integers) / min(list_with_integers)
#         return high_low_division
#     except ZeroDivisionError:
#         print("Division by zero is not possible")
    
# if __name__ == "__main__":
#     birth_date = input("Please provide your birth date in format 'YYYY:MM:DD' ")
#     new_date = is_date_correct(birth_date)
#     if new_date:
#         list_with_integers = date_string_to_list(new_date)
#         division = list_high_low_division(list_with_integers)
#         power = date_string_to_months_days(new_date)
#         sum_of = sum_of_list(list_with_integers)
#         print(f"Bigest and lowest number division is {division}" )
#         print(f"Days with power of month is {power}")
#         print(f"Sum of all numbers is {sum_of}")

# from typing import List


# date_list = [0, 1, 2]

# def divide_num(date_list: List[float]) -> float:
#     try:
#         div_num = max(date_list)/min(date_list)
#         return div_num
#     except ZeroDivisionError:
#         print(f"Division from {min(date_list)}")
#     except Exception as err:
#         print(err)


# try:
#     divide_num(date_list)
#     print(2 + 2)
# except Exception as err:
#     print(err)

# create a program which takes random sequence of numbers and letters (example: 'dfssdfsdfsdf655sdf2654fs6d4646'). sequence length should be not less than 25 characters.  
# The program sgould return (All stages requires separate functions, with logging all necessary data to file and error handling):
# 1) list of letters ordered
# 2) list of letters of reversed order
# 3) funtion which return list with only uniques letters (Can't repeat)
# 4) the same do with numbers
# 5)the sum of amount of letters and numbers are provided
# Rules:
# The program after text entered, should provide options list of actions:
# 1) Get list ordered
# 2) Get list ordered reversed etc...

# If there is special symbols,gaps - they should be added to special data structure , as we will have option :
# n) Show special symbols if provided.
# After any option is being used, terminal should ask if we want to use another option or to exit the program.
# If we choose to use another option, the option we already choose should be marked as `checked`:
# 1) Get list ordered[checked]
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def string_with_numbers_and_letters_only():
    list_of_numbers_and_letters = []
    user_input = ''
    list_of_special_chars = []
    while len(user_input) < 24:
        user_input = input("Enter a sequnce with letters and numbers, and sequence length should not be less than 25 characters: ")
        for char in user_input:
            if char.isalnum():
                list_of_numbers_and_letters.append(char.lower())
            else:
                list_of_special_chars.append(char)
    return list_of_numbers_and_letters   

def user_option(some_list):
    user_option = '1'
    dict_of_options = {'1' : '', '2' : '', '3' : '', '4' : '', '5' : '', '6' : '', '7' : '', 'n' : ''}
    while user_option in dict_of_options.keys():
        user_option = input(f"""
Enter a number from 1 to 7 for which action you want to take or any other key to exit the program:
                            
1) Get list of letters ordered {dict_of_options['1']}
2) Get list of letters ordered reversed {dict_of_options['2']}
3) Get list of unique letters {dict_of_options['3']}
4) Get list of numbers ordered {dict_of_options['4']}
5) Get list of numbers ordered reversed {dict_of_options['5']}
6) Get list of unique numbers {dict_of_options['6']}
7) Get letter and number amounts {dict_of_options['7']}
n) Get special symbols {dict_of_options['n']}
""")
        if user_option == '1':
            dict_of_options['1'] = '[Checked]' 
            logging.info(f"Option number {user_option} was picked ")
            print(ordered_letter_list(some_list))
        elif user_option == '2':
            dict_of_options['2'] = '[Checked]'
            logging.info(f"Option number {user_option} was picked ")
            print(reversed_letter_list(some_list))
        elif user_option == '3':
            dict_of_options['3'] = '[Checked]'
            logging.info(f"Option number {user_option} was picked ")
            print(unique_letter_list(some_list))
        elif user_option == '4':
            dict_of_options['4'] = '[Checked]'
            logging.info(f"Option number {user_option} was picked ")
            print(ordered_number_list(some_list))
        elif user_option == '5':
            dict_of_options['5'] = '[Checked]'
            logging.info(f"Option number {user_option} was picked ")
            print(reversed_number_list(some_list))
        elif user_option == '6':
            dict_of_options['6'] = '[Checked]'
            logging.info(f"Option number {user_option} was picked ")
            print(unique_number_list(some_list))
        elif user_option == '7':
            dict_of_options['7'] = '[Checked]'
            logging.info(f"Option number {user_option} was picked ")
            print(amounts_of_letters_and_numbers(some_list))
        # elif user_option == 'n':
        #     dict_of_options['n'] = '[Checked]'
        #     logging.info(f"Option number {user_option} was picked ")
        #     print(amounts_of_letters_and_numbers(some_list))
        else:
            print("You exited the program!")
    

def ordered_letter_list(list_of_letters_numbers: List[str]) -> List[str]:
    letter_list = [char for char in list_of_letters_numbers if char.isalpha()]
    return sorted(letter_list)

def reversed_letter_list(list_of_letters_numbers: List[str]) -> List[str]:
    letter_list = [char for char in list_of_letters_numbers if char.isalpha()]
    return sorted(letter_list, reverse=True)

def unique_letter_list(list_of_letters_numbers: List[str]) -> List[str]:
    letter_list = [char for char in list_of_letters_numbers if char.isalpha()]
    letter_set = set(letter_list)
    return list(letter_set)

def ordered_number_list(list_of_letters_numbers: List[str]) -> List[str]:
    number_list = [char for char in list_of_letters_numbers if char.isdigit()]
    return sorted(number_list)

def reversed_number_list(list_of_letters_numbers: List[str]) -> List[str]:
    number_list = [char for char in list_of_letters_numbers if char.isdigit()]
    return sorted(number_list, reverse=True)

def unique_number_list(list_of_letters_numbers: List[str]) -> List[str]:
    number_list = [char for char in list_of_letters_numbers if char.isdigit()]
    number_set = set(number_list)
    return list(number_set)

def amounts_of_letters_and_numbers(list_of_letters_numbers: List[str]) -> Tuple[int]:
    letter_list = [char for char in list_of_letters_numbers if char.isalpha()]
    number_list = [char for char in list_of_letters_numbers if char.isdigit()]
    return len(letter_list), len(number_list) 


if __name__ == "__main__":
        list_not_ordered = string_with_numbers_and_letters_only()
        user_option(list_not_ordered)
       
    