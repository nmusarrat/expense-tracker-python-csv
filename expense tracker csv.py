import csv

expenses=[]

try:
    file=open('expenses.csv','r')
    reader=csv.reader(file)


    for row in reader:
        if len(row)!=3:
            continue

        date=row[0]
        item=row[1]
        amount=float(row[2])
        expenses.append([date,item,amount])
    file.close()
except FileNotFoundError:
    file=open('expenses.csv','w',newline='')
    writer=csv.writer(file)
    writer.writerow(['Date','Item','Amount'])
    file.close()

while True:
    print('\nExpense Tracker:')
    print('1.Add expense')
    print('2.View expenses')
    print('3.Total spent')
    print('4.Search by item:')
    print('5.Delete expense:')
    print('6.Highest expense:')
    print('7.Exit')

    choice=input('Choose an option:')

    if choice=='1':
        date=input('Enter date:')
        item=input('Enter item:')
        amount=float(input('Enter amount:'))

        expenses.append([date,item,amount])

        file=open('expenses.csv','a',newline='')
        writer=csv.writer(file)
        writer.writerow([date,item,amount])
        file.close()

        print('Expense added.')
    elif choice=='2':
        print('\nYour Expenses:')
        for i,expense in enumerate(expenses):
            print(i,expense[0],expense[1],expense[2])
    elif choice=='3':
        total=0
        for expense in expenses:
            total+=expense[2]

        print('Total spent:',total)
    elif choice=='4':
        search_item=input('Enter item to search:')

        for e in expenses:
            if e[1].lower()==search_item.lower():
                print(e[0],e[1],e[2])
    elif choice=='5':
        print('\nExpenses:')

        for i,expense in enumerate(expenses):
            print(i,expense[0],expense[1],expense[2])
        try:
            index=int(input('enter expense number to delete:'))
        except ValueError:
            print('Invalid number.')
            continue

        if 0<=index<len(expenses):
            delete=expenses.pop(index)
            print('Deleted:',delete)

            file=open('expenses.csv','w',newline='')
            writer=csv.writer(file)

            for e in expenses:
                writer.writerow(e)
            file.close()
        else:
            print('Invalid option.')
    elif choice=='6':
        if len(expenses)==0:
            print('No expenses recorded.')
        else:
            highest=expenses[0]

            for e in expenses:
                if e[2]>highest[2]:
                    highest=e

            print('Highest expense:',highest[1],highest[2])
    elif choice=='7':
        print('Goodbye')
        break
    else:
        print('Invalid option.')
