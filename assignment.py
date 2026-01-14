# ABMI/00952/2023 - MUROKIH JOY KAMATHI
# BBIT PYTHON PROJECT
# SALON & BEAUTY SERVICE SYSTEM

clients = []

class Client:
    def __init__(self, client_id, client_name, phone_number):
        self.client_id = client_id
        self.client_name = client_name
        self.phone_number = phone_number
        self.service = None
        self.amount = 0

    def display(self):
        print(f"ID: {self.client_id}, Name: {self.client_name}, Phone: {self.phone_number}")
        if self.service:
            print(f"Service: {self.service.service_name}, Amount Paid: KES {self.amount}")

class Service:
    def __init__(self, service_name, price):
        self.service_name = service_name
        self.price = price

    def discount(self):
        return 0

class HairService(Service):
    def discount(self):
        return 0.10

class NailService(Service):
    def discount(self):
        return 0.05

class MakeupService(Service):
    def discount(self):
        return 0.15

class MassageService(Service):
    def discount(self):
        return 0

class Payment:
    def pay(self, amount):
        pass

class MpesaPayment(Payment):
    def pay(self, amount):
        print(f"Payment of KES {amount} made via Mpesa.")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of KES {amount} made via Card.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Payment of KES {amount} made via Cash.")

def get_client_by_id(client_id):
    for client in clients:
        if client.client_id == client_id:
            return client
    return None

def add_client():
    client_id = input("Enter client ID: ")
    client_name = input("Enter client name: ")
    phone_number = input("Enter phone number: ")

    clients.append(Client(client_id, client_name, phone_number))
    print("Client added successfully.")

def view_clients():
    if not clients:
        print("No client records found.")
    else:
        for client in clients:
            client.display()

def search_client():
    search_id = input("Enter client ID to search: ")
    client = get_client_by_id(search_id)
    if client:
        client.display()
    else:
        print("Client not found.")

def update_client():
    search_id = input("Enter client ID to update: ")
    client = get_client_by_id(search_id)
    if client:
        new_phone = input("Enter new phone number: ")
        client.phone_number = new_phone
        print("Client record updated successfully.")
    else:
        print("Client not found.")

def select_service():
    client_id = input("Enter client ID for service: ")
    client = get_client_by_id(client_id)

    if not client:
        print("Client not found. Please add client first.")
        return

    services = {
        1: HairService("Hair Styling", 3000),
        2: NailService("Nail Treatment", 2000),
        3: MakeupService("Makeup", 5000),
        4: MassageService("Body Massage", 4000)
    }

    print("\nAVAILABLE SERVICES")
    for key, service in services.items():
        print(f"{key}. {service.service_name} - KES {service.price}")

    choice = int(input("Select a service: "))
    selected_service = services.get(choice)

    if not selected_service:
        print("Service not found.")
        return

    discount_rate = selected_service.discount()
    discount_amount = selected_service.price * discount_rate
    total_amount = selected_service.price - discount_amount

    client.service = selected_service
    client.amount = total_amount

    print("\nPAYMENT DETAILS")
    print("Service Selected:", selected_service.service_name)
    print("Original Price:", selected_service.price)
    print("Discount:", discount_rate)
    print("Total Payable: KES", total_amount)

    print("\nSelect Payment Method")
    print("1. Mpesa")
    print("2. Card")
    print("3. Cash")

    pay_choice = input("Enter payment choice: ")

    if pay_choice == "1":
        payment = MpesaPayment()
    elif pay_choice == "2":
        payment = CardPayment()
    elif pay_choice == "3":
        payment = CashPayment()
    else:
        print("Invalid payment option.")
        return

    payment.pay(total_amount)
    print("Service completed successfully.")

def main_menu():
    while True:
        print("\nSALON MANAGEMENT SYSTEM")
        print("1. Add New Client")
        print("2. View All Clients")
        print("3. Search Client by ID")
        print("4. Update Client Record")
        print("5. Select Service & Make Payment")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            search_client()
        elif choice == "4":
            update_client()
        elif choice == "5":
            select_service()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()
