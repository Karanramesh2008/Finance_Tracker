import json
import os
from datetime import date
from data import transaction
import budget


t='trasaction.json'
transaction=[]
def save_transaction():
    with open(t,'w') as c:
        json.dump(transaction,c)


def load_transaction():
    global transaction
    if os.path.exists(t):
        try:
            with open(t,'r') as lt:
                transaction=json.load(lt)
                print("Loaded")
        except json.JSONDecodeError:
            print("JSON FILE CORRUPTED, creating new")
            transaction=[]
    else:
        transaction=[]


def add_income():
    i={}
    i['date']=str(date.today())
    i['type']='Income'
    try:
        amount=float(input("Enter the income amount: "))
        if amount<=0:
            print("Amount should be greater than 0")
            return 
        i['amount']=amount
    except ValueError:
        print("Amount should be valid number")
        return
    i['category']=input("Enter the income category: ")
    if i['category']=='':
        i['category']='general'
    i['note']=input("Enter the note: ")
    if i['note']=='':
        i['note']='-'
    transaction.append(i)
    save_transaction()


def add_expenses():
    i={}
    i['date']=str(date.today())
    i['type']='Expense'
    try:
        amount=float(input("Enter the Expense amount: "))
        if amount<=0:
            print("Amount should be greater than 0")
            return 
        i['amount']=amount
    except ValueError:
        print("Amount should be valid number")
        return
    i['category']=input("Enter the expense category: ")
    if i['category']=='':
        i['category']='general'
    i['note']=input("Enter the note: ")
    if i['note']=='':
        i['note']='-'
    transaction.append(i)
    save_transaction()
    budget.check_budget(i['category'])


def view_t():
    if len(transaction)==0:
        print("No Transaction Found")
        return
    print("a.View All Transaction\nb.View Expenses\nc.View Income")
    c=input("Enter your choice: ")
    print("-----------Your Transaction--------------")
    print(f"{'Transaction_No':<15} {'Date':<10}{'Type':<10} {'Amount':<10} {'Category':<15} {'Note':<15}")
    if(c=='a'):
        for q in transaction:
             print(f"{transaction.index(q)+1:<15} {q['date']:<10} {q['type']:<10} {q['amount']:<9.2f} {q['category']:<15} {q['note']:<15}")
    elif(c=='c'):
        for q in transaction:
            if q['type']=='Income':
                print(f"{transaction.index(q)+1:<15} {q['date']:<10} {q['type']:<10} {q['amount']:<9.2f} {q['category']:<15} {q['note']:<15}")
    elif(c=='b'):
        for q in transaction:
            if q['type']=='Expense':
                print(f"{transaction.index(q)+1:<15} {q['date']:<10} {q['type']:<10} {q['amount']:<9.2f} {q['category']:<15} {q['note']:<15}")

    return

def balance():
    if len(transaction)==0:
        print("Nil")
        return
    ia=0
    ex=0
    for q in transaction:
        if q['type']=='Income':
            ia+=q['amount']
        if q['type']=='Expense':
            ex+=q['amount']
    bal=ia-ex;
    print(f"Total Income: ₹{ia:.2f}",)
    print(f"Total Expenses: ₹{ex:.2f}",)
    print(f"Balance: ₹{bal:.2f}")


def delete_t():
    if len(transaction)==0:
        print("No Transaction Available\n\n")
        return
    view_t()
    try:
        d=int(input("Enter the Transaction No to Delete: "))
        if 1<=d<=len(transaction):
            y=input(f"Do you want to delete this recored {transaction[d-1]} (y/n): ")
            if(y=='y'):
                print(f"Transaction {transaction.pop(d-1)} is deleted")
                save_transaction()
        else:
            print("Invalid Transaction No.")
            return
    except ValueError:
        print("Invalid Choice.")
        return
