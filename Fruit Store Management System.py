stock = {}

def addfruit(fruit_name,qty,price):
    if fruit_name in stock:
        print("Entered Fruit already exist")
    else:
        stock[fruit_name] = {
            "qty" : qty,
            "price" : price 
            }
        print("data entered successful")

def updatestock(fruit_name,qty,price):
    if fruit_name in stock:
        stock[fruit_name] = {"qty":qty ,"price":price} 
        print("update successfully")
    else:
        print("Enter a Valid Fruit Name")    

def viewstock():
    for fruit_name,total in stock.items():
        print(f"Fruit Name = {fruit_name}")
        print(f"Qty = {total['qty']}")
        print(f"Price = {total['price']}")
        print()
        print(stock)

#>>>>>>>>>>>>>>>>>>>>>>>>Display<<<<<<<<<<<<<<<<<<<<<<<<
while True:
    print("Welcome To Fruit Market")
    print()
    print("1.Manager")
    print("2.costumer")
    
    role_id = int(input("Enter your Role :"))

    if role_id == 1:
        print()
        print("Fruit Market Manager ")
        print()
        print("1.Add Fruit Stock")
        print("2.View Fruit Stock")
        print("3.Update Fruit Stock")
        print()


        manager_choice = int(input("Enter Manager's Choice :"))

        if manager_choice == 1:
            print("Add Fruit Stock")
            print()
            fruit_name = input("Enter Fruit Name :") 
            qty = int(input("Enter Quantity in kg :"))
            price = int(input("Enter Price Of Fruit :"))

            addfruit(fruit_name,qty,price)

            

        elif manager_choice == 2:
            print()
            viewstock()    
            print()

        elif manager_choice == 3:
            print()
            print("Update Fruit Stock")
            print()
            fruit_name = input("Enter Fruit Name :")
            qty = int(input("Enter Quantity in kg :"))
            price = int(input("Enter Price Of Fruit :"))
            updatestock(fruit_name,qty,price)


    if role_id == 2:
        print("view avaiable Fruits")
        print()
        viewstock()
        print()
        print("Thank you for visiting")
        print(stock)
