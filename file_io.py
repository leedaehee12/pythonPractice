#file_io.py

#파일에 쓰기
with open("example.txt", "w") as file:
    file.write("hello World!\n")
    file.write("this is a test file.\n")

    print("파일에 쓰기 완료")


    #파일에서 읽기
with open("example.txt", "r") as file:
    content = file.read()


    print("파일내용 : ")
    print(content)

# 파일에 덧붙여 쓰기
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

    print("파일에 덧붙이기 완료")



