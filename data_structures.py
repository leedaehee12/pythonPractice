#data_structures.py

#리스트 생성
fruits = ["apple", "banana", "cherry"]

#요소추가
fruits.append("orange")

#요소접근
print("첫번째과일 : ", fruits[0])

#요소수정
fruits[1] = "blueBarry"

#요소삭제
del fruits[2] 

#리스트출력
print("리스트 : ", fruits)


#튜플 생성
coordinates = (10, 20)

#요소접근
print("첫번쨰 좌표 : ", coordinates[0])

# 불변성(튜플은 수정불가)
# 오류발생
#coordinates[0] = 15

#튜플 출력
print("튜플 : " , coordinates)


#딕셔너리 생성
person = {
    "name": "jhon",
    "age" :  30,
    "city" : "newYork"
}

#요소접근
print("이름", person["name"])

#요소 추가, 수정
person["emali"] = "jhon@email.com"
person["age"] = 31

#딕셔너리 출력
print("딕셔너리 : ", person)

#집합생성
unique_number = {1,2,3,4,4,5}

#요소추가
unique_number.add(6)

#요소삭제
unique_number.remove(3)

#중복제거된 집합 출력
print("집합 : ", unique_number)

#집합연산(합집합, 교집합)
another_set = {4, 5, 6, 7}
print("합집합 : " , unique_number.union(another_set))
print("교집합 : " , unique_number.intersection(another_set))