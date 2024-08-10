#exception_handling.py


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    except TypeError:
        print("Error: Both inputs must be numbers.")
        result = None
    else:
        print("Division Success")
    finally:
        print("Execution completed.")
    return result

#함수호출
print(divide(10,2))# 정상동작
print(divide(10,0))# 제로익셉션
print(divide(10,"a"))# 타입익셉션


def handle_exceptions():
    try:
        #ValueError 발생시
        number = int("not_a_number")
    except ValueError as ve:
        print(f"ValueError caught : {ve}")
    
    try:
        #IndexError 발생
        numbers = [1,2,3]
        print(numbers[5])
    except IndexError as ie:
        print(f"IndexError caught : {ie}")

    try:
        #Key Error 발생
        dictionary = {"key1" : "value1"}
        print(dictionary["non_existent_key"])
    except KeyError as ke:
        print(f"KeyError caught : {ke}")

#함수호출
handle_exceptions()

#사용자 정의 예외 클래스
class NegativeNumberError(Exception):
    pass

#숫자처리함수
def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print(f"{number} is a positive number.")

#함수호출
try:
    check_positive_number(10)
    check_positive_number(8)
    check_positive_number(-5)
except NegativeNumberError as nne:
    print(f"NegativeNumberError caught {nne}")


