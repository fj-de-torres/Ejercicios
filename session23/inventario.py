
from os import system
from time import sleep
from colorama import Fore, Back, Style


stock = {}
def clear():
    system("cls || clear")

def add_item(item:str,quantity:int) ->dict:
    stock[item] = quantity
    return stock

def update_stock(item:str, quantity:int) -> dict:
    if item in stock:
        stock[item] = quantity
    else:
        response = input(f"{item} is not in stock yet. Should we add it?(y/n)")
        if response == "y" or "Y":
            add_item(item,quantity)
    return stock

def del_item(item:str) ->dict:
    if item in stock:
        stock.pop(item)
        print(f"{item} removed from stock")
        sleep(2)
    else:
        print(f"Item {item} is not in stock")
        sleep(2)

def print_stock(stock):
    if len(stock) != 0:
        for items,quant in stock.items():
            print(f"Item: {items}", f"Num of items: {quant}")
        #print(stock)
    else:
        print(Style.BRIGHT + "Stock is empty!")
while True:
    clear()
    response = input("""
          Choose within the following options:
            1 Add item to stock
            2 Update existing item from stock
            3 Remove item from stock
            4 Print stock
            5 Exit
          """)
    match response:
        case "1":
            clear()
            item = input("Please insert item name to add to stock: ")
            quantity = input(f"Please insert quantity for {item}: ")
            print(add_item(item,quantity))
        
        case "2":
            clear()
            item = input("Please insert item name to update in stock: ")
            quantity = input(f"Please insert  new quantity for {item}: ")
            print(update_stock(item,quantity=1))
            sleep(2)
        
        case "3":
            clear()
            item = input("Please choose item name to remove from stock: ")
            print(del_item(item))
            sleep(2)

        case "4":
            clear()
            print_stock(stock)
            sleep(3)

        case "5":
            print(Fore.YELLOW + "Exiting...")
            sleep(2)
            break
        
        case _:

            print(Fore.RED + "No valid option choosen")
            sleep(2)
            break
