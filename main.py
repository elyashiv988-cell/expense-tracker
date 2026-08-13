import datetime
from expenses import *

def show_expenses(expenses):
    if len(expenses)>0:
        for item in expenses:
            print(f"{item["date"]} | {item["title"]} | {item["category"]} | {item[ "amount"]}")
        print(f"{calculate_total(expens_list)} ILS")
    else:
        print("Empty list")

def calculate_total(expenses):
    total=0
    
    for item in expenses:
        total+=float(item["amount"])
    return total

def add_expense(expenses,title,category,amount):
    new_item={}
    new_item["date"]=datetime.datetime.now()
    new_item["title"]=title
    new_item["category"]=category
    new_item["amount"]=amount
    expenses.append(new_item)

def ask_for_expense(expenses):
    
    choose_to_add=input("Would you want to add item to the list expenses? (y/n) ")
    while choose_to_add=="y" or choose_to_add=="yes":
        title=input("Enter the title item ")
        category=input("Enter the category item ")
        is_num=False
        while not is_num:
            try:
                amount=float(input("Enter the amount itme "))
                is_num=True
            except ValueError:
                print("Amount must be number!")

        add_expense(expens_list,title,category,amount)
        choose_to_add=input("Would you want to add item to the list expenses? (y/n) ")
    show_expenses(expens_list)

def main():
    show_expenses(expens_list)
    ask_for_expense(expens_list)

main()




