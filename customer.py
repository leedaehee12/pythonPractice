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
            
def main():
    manager = CustomerManager()

    # 고객 추가
    customer1 = Customer("C001", "Alice Smith", "alice@example.com", "123-456-7890")
    customer2 = Customer("C002", "Bob Johnson", "bob@example.com", "987-654-3210")

    manager.add_customer(customer1)
    manager.add_customer(customer2)

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

if __name__ == "__main__":
    main()

                    
        