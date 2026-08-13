from rich.console import Console
from rich.table import Table
import datetime
from expenses import *

def show_expenses(expenses):

    table = Table(title="Expenses list")
    table.add_column("Date",justify="right",style="cyan", no_wrap=True)
    table.add_column("Title",style="green")
    table.add_column("Category",style="yellow")
    table.add_column("Amount",justify="right",style="red")

    for item in expenses:
        table.add_row(str(item["date"]), item["title"], item["category"], str(item[ "amount"]))
    console = Console()
    console.print(table)

    console.print(f"[bold red]Total: {calculate_total(expens_list)} ILS[/bold red]")
    

def calculate_total(expenses):
    total=0
    
    for item in expenses:
        total+=float(item["amount"])
    return f"{total:.2f}"

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




