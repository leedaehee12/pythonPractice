import mariadb

#데이터베이스 연결
try:
    connection = mariadb.connect(
        user = "pythonUser",
        password = "1234",
        host = "localhost",
        port = 3306,
        database = "pythonpractice"
    )
    print("DataBase connenction Sucessful")
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platfrom{e}")
    exit(1)

 # 커서 생성
cursor = connection.cursor()

def crate_table():
    try:
        cursor.execute
        (
        """
        CREATE TABLE IF NOT EXISTS customers
        (id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        ematl VARCHAR(100),
        phone VARCHAR(20)
        )
        """
        )
        print("Table create sucess")
    
    except mariadb.Error as e:
        print(f"Error crating table : {e}")
    
crate_table()
    