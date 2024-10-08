import csv

class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id  = customer_id 
        self.name = name
        self.email = email
        self.phone = phone
        
        
    def update_info(self, name = None, email = None, phone = None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
    
    def __str__(self) -> str:
        return f"ID : {self.customer_id}, Name : {self.name}, Email : {self.email}, Phone : {self.phone}"
            
                        
class CustomerManager:
    def __init__(self):
        self.customers = {}
    
    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
    
    def list_customers(self):
        for customer in self.customers.values():
            print(customer)
            
    def update_customer(self, customer_id, name = None, email = None, phone = None):
        customer = self.customers.get(customer_id)
        if customer:
            customer.update_info(name, email, phone)
        else:
            print(f"Customer with ID {customer_id} not found")
    
    def find_customer(self, name):
        found = False
        for customer in self.customers.values():
            if customer.name.lower() == name.lower():
                print(customer)
                found = True
        if not found:
            print(f"Customer with name {name} not fount")
            
    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer with ID {customer_id} has been deletede")
        else:
            print(f"Customer with ID {customer_id} Not Found")
    
    def save_to_file(self, filename):
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Phone"])
            for customer in self.customers.values():
                writer.writerow([customer.customer_id, customer.name, customer.email, customer.phone])
                print(f"Data saved to {filename}.")
    
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header
                for row in reader:
                    customer_id, name, email, phone = row
                    customer = Customer(customer_id, name, email, phone)
                    self.add_customer(customer)
            print(f"Data loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
            
def main():
    manager = CustomerManager()

    # 고객 추가
    customer1 = Customer("C001", "Alice Smith", "alice@example.com", "123-456-7890")
    customer2 = Customer("C002", "Bob Johnson", "bob@example.com", "987-654-3210")

    manager.add_customer(customer1)
    manager.add_customer(customer2)
    
    # 고객 목록 저장
    manager.save_to_file("customers.csv")

    # 기존 데이터 삭제 (테스트용)
    manager.customers = {}

    # 파일에서 고객 목록 불러오기
    manager.load_from_file("customers.csv")

    # 불러온 고객 목록 출력
    manager.list_customers()


    # 고객 목록 출력
    print("Customer List:")
    manager.list_customers()

    # 고객 정보 수정
    print("\nUpdating Alice's email:")
    manager.update_customer("C001", email="alice.smith@newdomain.com")

    # 수정된 고객 목록 출력
    print("\nUpdated Customer List:")
    manager.list_customers()

    # 고객 검색
    print("\nSearching for Bob Johnson:")
    manager.find_customer("Bob Johnson")

    # 존재하지 않는 고객 검색
    print("\nSearching for Non-existent Customer:")
    manager.find_customer("Charlie Brown")
    
      # 고객 목록 출력
    print("Customer List:")
    manager.list_customers()

    # 고객 삭제
    print("\nDeleting customer with ID C001:")
    manager.delete_customer("C001")

    # 삭제된 후 고객 목록 출력
    print("\nCustomer List after deletion:")
    manager.list_customers()

    # 존재하지 않는 고객 삭제 시도
    print("\nTrying to delete non-existent customer with ID C003:")
    manager.delete_customer("C003")

if __name__ == "__main__":
    main()

                    
        