#Q1. Declare a function add_two_numbers. It takes two parameters and it returns a sum
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(3, 4)) # 7
#Q2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    return PI * r * r
print(area_of_circle(10)) # 314.0
#Q3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for i in args:
        if type(i) == int:
            total += i
        else:
            return "All items should be numbers"
    return total
print(add_all_nums(1, 2, 3, 4, 5)) # 15
#Q4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celcius_to-fahrenheit.
def convert_celcius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(convert_celcius_to_fahrenheit(36)) # 96.8
#Q5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ["September", "October", "November"]:
        return "Autumn"
    elif month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Month not found"
print(check_season("April")) # Spring
print(check_season("January")) # Winter
#Q6. Write a function called calculate_slope which return the slope of a linear equation.
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 4)) # 1.0
#Q7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a, b, c):
    D = b**2 - 4*a*c
    x1 = (-b + math.sqrt(D)) / 2*a
    x2 = (-b - math.sqrt(D)) / 2*a
    return x1, x2
print(solve_quadratic_eqn(1, -5, 6)) # (3.0, 2.0)
#Q8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)
print_list(["Apple", "Banana", "Orange"]) # Apple Banana Orange
#Q9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)):
        reversed_list.append(lst.pop())
    return reversed_list
print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
#Q10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    return [i.capitalize() for i in lst]
print(capitalize_list_items(["apple", "banana", "orange"])) # ['Apple', 'Banana', 'Orange']
#Q11. Declare a function named add_item. It takes a list and an item parameter and it returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item([1, 2, 3], 4)) # [1, 2, 3, 4]
#Q12. Declare a function named remove_item. It takes a list and an item parameter and it returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item([1, 2, 3], 2)) # [1, 3]
#Q13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    return sum(range(n+1))
print(sum_of_numbers(5)) # 15
#Q14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    return sum([i for i in range(n+1) if i % 2 != 0])
print(sum_of_odds(5)) # 9
#Q15. Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(n):
    return sum([i for i in range(n+1) if i % 2 == 0])
print(sum_of_evens(5)) # 6
#Q16. Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    return len([i for i in range(n+1) if i % 2 == 0]), len([i for i in range(n+1) if i % 2 != 0]) 
print(evens_and_odds(5)) # (3, 2)
#Q17. Write a function which takes a list of numbers and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))
print(unique_list([1, 2, 2, 3, 4, 4, 5])) # [1, 2, 3, 4, 5]
#Q18. Write a function that takes a number and returns a list of its digits.
def list_of_digits(n):
    return [int(i) for i in str(n)]
print(list_of_digits(12345)) # [1, 2, 3, 4, 5]
#Q19. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(5)) # 120
#Q20. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(11)) # True
#Q21. Write a functions which checks if all items are unique in the list.
def is_all_unique(lst):
    return len(lst) == len(set(lst))
print(is_all_unique([1, 2, 3, 4, 5])) # True
print(is_all_unique([1, 2, 2, 3, 4, 5])) # False
#Q22. Write a function which checks if all the items of the list are of the same data type.
def is_same_data_type(lst):
    return len(set([type(i) for i in lst])) == 1
print(is_same_data_type([1, 2, 3])) # True
print(is_same_data_type([1, 2, "a"])) # False
#Q23. Write a function which check if provided variable is a valid python variable
def is_valid_variable(var):
    return var.isidentifier()
print(is_valid_variable("name")) # True
print(is_valid_variable("my-name")) # False
#Q24. Write a function which returns the number of vowels in a given string.
def count_vowels(s):
    return len([i for i in s if i in "aeiou"])
print(count_vowels("apple")) # 2
#Q25. Write a function which checks if all the letters in the word are vowels.
def is_all_vowels(s):
    return len([i for i in s if i in "aeiou"]) == len(s)
print(is_all_vowels("apple")) # False
print(is_all_vowels("aie")) # True
#Q26. Write a function which checks if all the letters in the word are consonants.
def is_all_consonants(s):
    return len([i for i in s if i not in "aeiou"]) == len(s)
print(is_all_consonants("apple")) # False
print(is_all_consonants("bcd")) # True
#Q27.2. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(s):
    return len(s) == 0
print(is_empty("")) # True
print(is_empty("apple")) # False
#Q28. Write different functions which take lists. They should calculate_mean, calculate_median,calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)
def calculate_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    return lst[n//2]
def calculate_mode(lst):
    return max(set(lst), key=lst.count)
def calculate_range(lst):
    return max(lst) - min(lst)
def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum([(i - mean) ** 2 for i in lst]) / len(lst)
def calculate_std(lst):
    return calculate_variance(lst) ** 0.5
print(calculate_mean([1, 2, 3, 4, 5])) # 3.0
print(calculate_median([1, 2, 3, 4, 5])) # 3
print(calculate_mode([1, 2, 2, 3, 4, 5])) # 2
print(calculate_range([1, 2, 3, 4, 5])) # 4
print(calculate_variance([1, 2, 3, 4, 5])) # 2.0
print(calculate_std([1, 2, 3, 4, 5])) # 1.4142135623730951
#Q29. Write a function called is_palindrome which checks if a word is a palindrome. 
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam")) # True
print(is_palindrome("apple")) # False
#Q30. Write a function called is_anagram which checks if two words are anagrams of each other.
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
print(is_anagram("listen", "silent")) # True
print(is_anagram("triangle", "integral")) # True
print(is_anagram("apple", "banana")) # False








