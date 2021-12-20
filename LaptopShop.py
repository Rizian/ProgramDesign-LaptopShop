from LaptopClass import Laptop

# add more and change if needed | format: "name (all lowercase)" : Laptop("Name", price in dollars, amount in stock),
laptops = {
    "dell" : Laptop("Dell", 500, 12), 
    "lenovo" : Laptop("Lenovo", 1300, 5),   # temporary placeholders, change if needed
    "hp" : Laptop("HP", 850, 20),
        }
    
# Displays the list of items available to purchase
def printShopItems():
    print("\t|---------------------------------------|")
    print("\t|------------Laptops for sale-----------|")
    print("\t|---------------------------------------|")
    print("\t|Brand\t\t|Price\t\t|Stock\t|")
    print("\t|---------------|---------------|-------|")
    for i in laptops:
        print(f"\t|{laptops[i].get_brand()}\t\t|${laptops[i].get_price():.2f}\t|{laptops[i].get_stock()}\t|")
    print("\t|_______________|_______________|_______|")
    print("")

# Prints the selected purchase order
def printOrder(item, amount, total):
    print("\t|-----------------------------------------------|")
    print("\t|-------------------Your Order------------------|")
    print("\t|-----------------------------------------------|")
    print("\t|Brand\t\t|Price\t\t|Amount\t\t|")
    print("\t|---------------|---------------|---------------|")
    print(f"\t|{laptops[item].get_brand()}\t\t|${laptops[item].get_price():.2f}\t|x{amount}\t\t|")
    print("\t|-----------------------------------------------|")
    print(f"\t|\t\tTotal Price:\t ${total:.2f}\t|")
    print("\t|_______________________________________________|")

def main():
    while True:
        printShopItems()
        
        while True:
            select = input("Enter which laptop brand you would like to purchase >> ").lower()
            if select not in laptops:
                print("Brand not found. Please Re-enter.\n")
            elif select in laptops and (laptops[select].get_stock() == "N/A"):
                print(f"{laptops[select].get_brand()} laptops are currently out of stock.\n")
                retry = input("Would you like to purchase a different brand? (Y/N) >> ").lower()
                if retry == "y":
                    continue
                else:
                    quit()
            else:
                break
        
        print(f"\nYou have chosen to purchase {laptops[select].get_brand()} laptop(s).\n")

        while True:
            try:
                amount = int(input("Enter the amount you would like to purchase >> "))
            except ValueError:
                print("Please enter a non-decimal number.\n")
                continue
            total = laptops[select].calc_total_purchase(amount)
            if amount <= 0:
                print("Purchases cannot be zero or negative.")
                print("Please enter a positive number.\n")
                continue
            elif total == "Insufficient Stock":
                print("Not enough in stock for purchase. Please purchase within stock.\n")
                continue
            else:
                break
        
        print(f"\nYou have chosen to purchase {amount} laptop(s).\n")
        print("Your order:\n")
        printOrder(select, amount, total)
        print("")
        
        restart = input("Would you like to purchase more? (Y/N) >> ").lower()
        if restart == "y":
            print("Remaining Stock:\n")
            continue
        else:
            print("Remaining Stock:\n")
            printShopItems()
            break

if __name__ == "__main__":
    main()