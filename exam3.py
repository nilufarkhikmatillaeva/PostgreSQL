
class User:
    def __init__(self, name, phone, email,password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.is_admin = False
        self.cart = []



class Admin:
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

class Product:
    def __init__(self, product_id, title, price, pr_number):
        self.title = title
        self.price = price
        self.pr_number = pr_number

p1 = Product('123','non',5000,20)
p2 = Product('124','Chocolate',15000,30)
p3 = Product('125', 'meat',120000,15)


class Shop:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        self.products = []
        self.users = []
        self.data = []

    def add_user(self):
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')
        password = input('Password: ')

        user = User(name, phone, email, password)
        self.users.append(user)

    def show_users(self):
        count = 0
        for user in self.users:
            count += 1
            if user.is_admin:
                print(f'{count}.Admin: {user.name} phone: {user.phone} email: {user.email}')
            else:
                print(f'{count}.Customer: {user.name} phone: {user.phone} email: {user.email}')



    def add_product(self):
        product_id = input('Product ID: ')
        title = input('Title: ')
        price = int(input('Price: '))
        pr_number = int(input('Number: '))

        product = Product(product_id,title, price, pr_number )
        self.products.append(product)

    def remove_product(self):
        self.show_products()
        choice = int(input('Which product do you want to remove? '))
        if 1<= choice <= len(self.products):
            self.products.pop(choice-1)
        else:
            print('Invalid choice')



    def show_products(self):
        count = 0
        for item in self.products:
            count += 1
            print(f'{count}.product name: {item.title}\n price: {item.price}\n number of products: {item.pr_number}')


    def add_to_cart(self,user):
        print('\n---------Available products---------')
        index = 1
        for product in self.products:
            print(f'{index}. {product.title}: {product.price} number of product: {product.pr_number}')
            index += 1


        choice = int(input('Choose product: '))
        selected_product = self.products[choice-1]

        qty = int(input('Quantity: '))

        user.cart.append({
            "product": selected_product,
            "quantity": qty
        })

    def show_cart(self,user):
        if not user.cart:
            print('Savat bosh ')
            return

        for item in user.cart:
            product = item["product"]
            quantity = item["quantity"]
            print(f'product: {product.title} quantity: {quantity} price: {product.price}')


    def place_order(self,user):
        if not user.cart:
            print('Cart is empty')
            return
        total = 0
        for item in user.cart:
            product = item["product"]
            quantity = item["quantity"]
            print(f'Buyurtmangiz: {product.title}')

            if quantity > product.pr_number:
                print('Not enough stock')

            elif quantity <= product.pr_number:
                product.pr_number -= quantity

            total += product.price * quantity

        user.cart.clear()
        self.balance += total
        print(f'Buyurtma topshirildi! Total: {total}')

    def show_balance(self):
        print(f'Balance: {self.balance}')

shop_1 = Shop('Shop 1', 1000000)
u1 = User('ali', '123456', 'ali@gmail.com', '0101')
admin1 = User("admin",123456789, "admin@gmail.com", "0202")
admin1.is_admin = True
shop_1.users.append(admin1)
shop_1.users.append(u1)

shop_1.products.append(p1)
shop_1.products.append(p2)
shop_1.products.append(p3)

def login(shop):
    name = input('Name: ')
    password = input('Password: ')

    for user in shop.users:
        if user.name == name and user.password == password:
            print(f"Welcome, {user.name}")
            return user

    print('Invalid username or password')
    return None

def shop_menu(shop, current_user):
    while True:
        if current_user.is_admin:
            key = input(" 1. Add product\n 2. Show products\n 3. Show users\n 4. Add users\n 5. Remove product\n 6. Check balance\n 7. Exit\nChoose: ")
            if key == "1":
                shop.add_product()
            elif key == "2":
                shop.show_products()
            elif key == "3":
                shop.show_users()
            elif key == "4":
                shop.add_user()
            elif key == "5":
                shop.remove_product()
            elif key == "6":
                shop.show_balance()
            elif key == "7":
                current_user = None
                while not current_user:
                    current_user = login(shop)
            else:
                print("Invalid choice.")
        else:
            key = input(" 1. Show products\n 2. Savatga qo'shish\n 3. Savatni ko'rish\n 4. Buyurtma berish\n 5. Exit\nChoose: ")
            if key == "1":
                shop.show_products()
            elif key == "2":
                shop.add_to_cart(current_user)
            elif key == "3":
                shop.show_cart(current_user)
            elif key == "4":
                shop.place_order(current_user)
            elif key == "5":
                current_user = None
                while not current_user:
                    current_user = login(shop)
            else:
                print("Invalid choice.")

current_user = None
while not current_user:
    current_user = login(shop_1)

shop_menu(shop_1,current_user)
