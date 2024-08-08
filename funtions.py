#funtions.py

#함수정의
def greet(name):
    return f"hello, {name}!"

#함수호출
print(greet("alice"))
print(greet("bob"))

#기본값이 있는 함수
def greet_with_default(name = "Guest"):
    return f"Hello, {name}!"

print(greet_with_default())
print(greet_with_default("Charlie"))

def arithemetic_operations(a,b):
    sum_ = a+b
    diff = a-b
    product = a*b
    quotient = a/b
    return sum_, diff, product, quotient

# 함수호출
result_ = arithemetic_operations(10,5)
print("sum_ :", result_[0])
print("diff :", result_[1])
print("product :", result_[2])
print("quotient :", result_[3])

#람다함수
square = lambda x: x ** 2
print("square of 4:", square(4))