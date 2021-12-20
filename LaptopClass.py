class Laptop:
    "This is a class for a laptop brand"

    def __init__(self, brand, price, stock):
        self.set_brand(brand)
        self.set_price(price)
        self.set_stock(stock)

    def __str__(self):
        return f"Brand Name: {self.get_brand}\nPrice: {self.get_price:.2f}\nAvailable Stock: {self.get_stock}"

    def set_brand(self, brand) -> str:
        self.__brand = brand
    def set_price(self, price) -> float:
        self.__price = price
    def set_stock(self, stock) -> int:
        self.__stock = stock

    def get_brand(self):
        return self.__brand
    def get_price(self):
        return self.__price
    def get_stock(self):
        if self.__stock <= 0:
            return "N/A"
        return self.__stock
        
    def calc_total_purchase(self, amount):
        total_cost = self.__price * amount
        if amount > self.__stock:
            return "Insufficient Stock"
        elif amount <= 0:
            pass
        else:
            self.__stock -= amount
        return total_cost