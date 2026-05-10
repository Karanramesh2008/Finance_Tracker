
import os
from datetime import date
import transactions 

def montly_s():
    if len(transactions.transaction)==0:
        print("No Transaction Record.")
        return
    '''print("a.This Month")
    print("b.Past Months.")'''
    choice='a'
    if choice=='a':
        today=str(date.today()).split("-")
        y=today[0]
        m=today[1]
    '''else:
        c=str()'''
    print(f"{'Transaction_No':<15} {'Date':<10}{'Type':<10} {'Amount':<10} {'Category':<15} {'Note':<15}")
    inc,exp=0,0
    for i,q in enumerate(transactions.transaction,start=1):
        t_m=q['date'].split('-')[1]
        t_y=q['date'].split('-')[0]
        if (t_m==m and t_y==y):
           print(f"{i:<15} {q['date']:<10} {q['type']:<10} {q['amount']:<9.2f} {q['category']:<15} {q['note']:<15}")
           if q['type']=='Income':
               inc+=q['amount']
           else:
               exp+=q['amount']
    if inc==0 and exp==0:
        print("No Transaction")

    print(f"\nTotal Income : ₹{inc:.2f}")
    print(f"Total Expenses : ₹{exp:.2f}")
    print(f"Balance : ₹{inc-exp:.2f}")

def category_breakdown():
    try:
        print("Choice:\n1.Income\n2.Expense")
        choice=int(input("Enter the choice: ").strip())
        if choice==1:
            ype='Income'
        elif choice==2:
            ype='Expense'
        else:
            print("Please enter valid type")
            return
        cate={}
        if len(transactions.transaction)==0:
            print("Null")
            return
        tote=0.0
        for q in transactions.transaction:
            if q['type']==ype:
                if q['category'] not in cate:
                    cate[q['category']]=0.0
                cate[q['category']]+=float(q['amount'])
                tote+=float(q['amount'])
        if(tote==0):
            print("No matching Trasaction found")
            return
        print(f"This month {ype}")
        print(f"{'Category':<10} {'Amount':<10} {'Percentage':<10}")

        for a,b in cate.items():
                print(f"{str(a):<10} {b:<10} {(b/tote)*100:<8.2f}%")
        
        print('-'*20)
        print(f"{'Total:':<10} {tote:<9.2f}")
    except ValueError:
        print("Invalid Input.")
        return

def export():
    today=(str(date.today()))
    month=today.split("-")[1]
    year=today.split("-")   [0]

    toi=0
    toe=0
    for q in transactions.transaction:
        if q['type']=='Income':
            toi+=q['amount']
        else:
            toe+=q['amount']
    tob=toi-toe

    m_i=0
    m_e=0
    for q in transactions.transaction:
        t_m=q['date'].split('-')[1]
        t_y=q['date'].split('-')[0]
        if t_m==month and t_y==year:
            if q['type']=='Income':
                m_i+=q['amount']
            else:
                m_e+=q['amount']
    m_b=m_i-m_e
    
    with open('report.txt','w',encoding='utf-8') as f:
        f.write("="*45+'\n')
        f.write("   PERSONAL FINANCE REPORT\n")
        f.write(f"   Generated: {today}\n")
        f.write("="*45+'\n\n')
        
        f.write("OVERALL SUMMARY\n")
        f.write("-"*25+"\n")
        f.write(f"Total Income   : ₹{toi:.2f}\n")
        f.write(f"Total Expense  : ₹{toe:.2f}\n")
        f.write(f"Balance        : ₹{tob:.2f}\n\n")

        f.write("THIS MONTH SUMMARY\n")
        f.write("-"*25+"\n")
        f.write(f"Income   : ₹{m_i:.2f}\n")
        f.write(f"Expense  : ₹{m_e:.2f}\n")
        f.write(f"Balance  : ₹{m_b:.2f}\n\n")

        f.write("ALL TRANSACTIONS\n")
        f.write("-"*25+"\n")

        for i,q in enumerate(transactions.transaction,start=1):
            f.write(f"{i}. {q['type']:<8} | Rs.{float(q['amount']):<9.2f} | {q['category']:<12} | {q['note']:<15} | {q['date']}\n")
            
        f.write("\n"+"="*45)
        f.write("\n\t END OF REPORT\n")
        f.write("="*45)
    
    print(f"✅  Report saved to 'report.txt' !")
    print(f"📂  Location : {os.path.abspath('report.txt')}")
    print("\n")
