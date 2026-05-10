import transactions
import summary
import budget



budget.load_budget()
transactions.load_transaction()
e=True
print("="*45)
print("\tWelcome to Finance Tracker")
print("="*45)
while e:
    print("Choice\na.Add Income \nb.Add expenses \nc.View Balance \nd.View Transactions\ne.Delete Transaction\nf.Montly Summary\ng.Category Breakdown\nh.Budget\ni.Report\nj.Quit")
    choice=input("Enter the choice: ")
    if choice=='a':
        print("Income")
        transactions.add_income()
    elif choice=='b':
        print("Expenses")
        transactions.add_expenses()
    elif choice=='c':
        print("Balance")
        transactions.balance()
    elif choice=='d':
        print("Transaction")
        transactions.view_t()
    elif choice=='e':
        transactions.delete_t()
    elif choice=='f':
        summary.montly_s()
    elif choice=='g':
        summary.category_breakdown()
    elif choice=='h':
        r=True
        while r:
            print("1.Set Budget \n2.View_Budget \n3.Back to Main Menu")
            try:
                cho=int(input("Enter choice:"))
                if cho==1:
                    budget.set_budget()
                elif cho==2:
                    budget.view_budget()
                elif cho==3:
                    r=False
                else:
                    print("Enter Invalid Choice.")
            except ValueError:
                print("Invalid Input")
    elif choice=='i':
        summary.export()
    elif choice=='j':
        print("="*45)
        print("Thank you for using our App")
        print("="*45)
        e=False
    else:
        print("Please enter valid choices")

