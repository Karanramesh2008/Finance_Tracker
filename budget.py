import json
import os
from datetime import date
from data import transaction  
from data import budget

budget={}
b='budget.json'
def save_budget():
    with open(b,'w') as c:
        json.dump(budget,c)
def load_budget():
    global budget
    if os.path.exists(b):
        try:
            with open(b,'r') as lt:
                budget=json.load(lt)
                print("Loaded")
        except json.JSONDecodeError:
            print("JSON FILE CORRUPTED, creating new")
            budget={}
    else:
        budget={}

def set_budget():
    i=input("Enter the category: ").lower()
    if i=='':
        print("Category cannot be empty.")
        return
    try:
        limit=float(input(f"Enter the limit for '{i}' : ₹"))
        if limit<=0:
            print("Limit must be greater than 0")
            return
        budget[i]=limit
        save_budget()
        print(f"Budget of ₹ {limit:.2f} set for '{i}' !")
    except ValueError:
        print(f"Please enter a valid amount!")

def view_budget():
    if len(budget)==0:
        print("No budget record is found.")
        return
    
    today=str(date.today()).split("-")
    month=today[1]
    year=today[0]
    print("\n"+"="*55)
    print(f"{'Category':<15} {'Budget':>10} {'Spent':>10} {'Remaining':>10}")
    print("="*55)

    for cat,lim in budget.items():
        spent=0
        for q in transaction:
            t_m=q['date'].split('-')[1]
            t_y=q['date'].split('-')[0]
            if (q['type']=='Expense' and q['category'].lower()==cat and t_m==month and t_y==year):
                spent+=q['amount']
        remaining=lim-spent
        print(f"{cat:<15} ₹{lim:>8.2f} ₹{spent:>8.2f} ₹{remaining:>8.2f}")
        
        if spent>lim:
            print(f" ⚠️ Exceeded budget for '{cat}' by ₹{spent-lim:.2f}")
        elif spent>lim *0.8:
            print(f" ⚠️ 80% of '{cat}' budget used!")
    print('='*55)
                

def check_budget(category):
    if category.lower() not in budget:
        return
    today=str(date.today()).split("-")
    month=today[1]
    year=today[0]
    spent=0
    for q in transaction:
        t_m=q['date'].split('-')[1]
        t_y=q['date'].split('-')[0]
        if (q['type']=='Expense' and q['category'].lower()==category and t_m==month and t_y==year):
            spent+=q['amount']
        
    lim=budget[category.lower()]   
    if spent>lim:
        print(f" ⚠️ Exceeded budget for '{category}'! Spent  ₹{spent-lim:.2f} of ₹{lim:.2f}")
    elif spent>lim *0.8:
        print(f" ⚠️ 80% of '{category}' budget used! Spent  ₹{spent:.2f} of ₹{lim:.2f} ")
    print('='*55)