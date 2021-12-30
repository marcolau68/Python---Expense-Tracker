from tkinter import *
from tkinter import ttk
import sqlite3
import datetime


root = Tk()
root.title('Money Management')
root.geometry('600x600')
root.config(background = '#21969e')


# Main menu

menu = Menu(root)
root.config(menu=menu)


# Check total expenses


def total_expense():
    total_expense_screen = Frame(root, bg='white', width=500, height=500)
    total_expense_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_total_expense_screen = Button(total_expense_screen, text='back', command=total_expense_screen.destroy)
    quit_total_expense_screen.place(relx=0, rely=0, anchor='nw')

    show_total_expense = ttk.Treeview(total_expense_screen,  height = 25)
    show_total_expense['columns'] = ('one', 'two', 'three', 'four')

    show_total_expense.column('#0', width = 0)
    show_total_expense.column('one', width = 100)
    show_total_expense.column('two', width = 100)
    show_total_expense.column('three', width = 100)
    show_total_expense.column('four', width = 200)

    show_total_expense.heading('one', text = 'Date', anchor = 'w')
    show_total_expense.heading('two', text = 'Amount Spent', anchor = 'w')
    show_total_expense.heading('three', text = 'Purpose', anchor = 'w')
    show_total_expense.heading('four', text = 'Notes', anchor = 'w')

    total_expense_list = []

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    c.execute("SELECT * FROM Expense")
    conn.commit()

    total_expense_list = c.fetchall()

    for i in range(len(total_expense_list)):
        show_total_expense.insert('', 'end', text = '', values = (total_expense_list[i]))

    conn.commit()

    net_expense = 0

    c.execute("SELECT * FROM Expense")
    conn.commit()
    for item in c.fetchall():
        net_expense += item[1]

    net_expense_label = Label(total_expense_screen, text='Net Expense is: %s' % (net_expense))
    net_expense_label.place(relx=1, rely=1, anchor='se')

    c.close()
    conn.close()

    show_total_expense.place(relx = 0, rely = 0.1)


# Check category expense


def category_expense(category):
    expense_screen = Frame(root, bg='white', width=500, height=500)
    expense_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_expense_screen = Button(expense_screen, text='back', command=expense_screen.destroy)
    quit_expense_screen.place(relx=0, rely=0, anchor='nw')

    show_expense = ttk.Treeview(expense_screen,  height = 25)
    show_expense['columns'] = ('one', 'two', 'three', 'four')

    show_expense.column('#0', width = 0)
    show_expense.column('one', width = 100)
    show_expense.column('two', width = 100)
    show_expense.column('three', width = 100)
    show_expense.column('four', width = 200)

    show_expense.heading('one', text = 'Date', anchor = 'w')
    show_expense.heading('two', text = 'Amount Spent', anchor = 'w')
    show_expense.heading('three', text = 'Purpose', anchor = 'w')
    show_expense.heading('four', text = 'Notes', anchor = 'w')

    expense_list = []

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    c.execute("SELECT * FROM Expense WHERE Purpose=?", (category,))
    conn.commit()

    expense_list = c.fetchall()

    for i in range(len(expense_list)):
        show_expense.insert('', 'end', text = '', values = (expense_list[i]))

    conn.commit()

    expenses = 0

    c.execute("SELECT * FROM Expense WHERE Purpose=?", (category,))
    conn.commit()
    for item in c.fetchall():
        expenses += item[1]

    expense_label = Label(expense_screen, text='%s Expense is: %s' % (category, expenses))
    expense_label.place(relx=1, rely=1, anchor='se')

    c.close()
    conn.close()

    show_expense.place(relx = 0, rely = 0.1)


# Time Expense

def time_expense(time):
    time_expense_screen = Frame(root, bg='white', width=500, height=500)
    time_expense_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_time_expense_screen = Button(time_expense_screen, text='back', command=time_expense_screen.destroy)
    quit_time_expense_screen.place(relx=0, rely=0, anchor='nw')

    show_time_expense = ttk.Treeview(time_expense_screen,  height = 25)
    show_time_expense['columns'] = ('one', 'two', 'three', 'four')

    show_time_expense.column('#0', width = 0)
    show_time_expense.column('one', width = 150)
    show_time_expense.column('two', width = 150)
    show_time_expense.column('three', width = 200)

    show_time_expense.heading('one', text = 'Date', anchor = 'w')
    show_time_expense.heading('two', text = 'Amount Spent', anchor = 'w')
    show_time_expense.heading('three', text = 'Purpose', anchor = 'w')
    show_time_expense.heading('four', text= 'Notes', anchor='w')

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    expenses = 0
    time_expense_list = []

    if time == 'day':
        today = datetime.date.today()
        date = today.strftime('%Y-%m-%d')

        c.execute("SELECT * FROM Expense WHERE Date = ? ", (date,))
        conn.commit()
        for item in c.fetchall():
            expenses += item[1]

        expense_label = Label(time_expense_screen, text='Net Expense is: %s' % (expenses))
        expense_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Expense WHERE Date = ? ", (date,))
        conn.commit()

        time_expense_list = c.fetchall()

        for i in range(len(time_expense_list)):
            show_time_expense.insert('', 'end', text = '', values = (time_expense_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_time_expense.place(relx = 0, rely = 0.1)

    elif time == 'month':
        today = datetime.date.today()
        date = today.strftime('%Y-%m')

        upper_combine = date + '-01'
        upper = ''.join(upper_combine)

        lower_combine = date + '-31'
        lower = ''.join(lower_combine)

        c.execute("SELECT * FROM Expense WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            expenses += item[1]

        expense_label = Label(time_expense_screen, text='Net Expense is: %s' % (expenses))
        expense_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Expense WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()

        time_expense_list = c.fetchall()

        for i in range(len(time_expense_list)):
            show_time_expense.insert('', 'end', text = '', values = (time_expense_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_time_expense.place(relx = 0, rely = 0.1)

    elif time == 'year':
        today = datetime.date.today()
        date = today.strftime('%Y')

        upper_combine = date + '-01-01'
        upper = ''.join(upper_combine)

        lower_combine = date + '-12-31'
        lower = ''.join(lower_combine)

        c.execute("SELECT * FROM Expense WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            expenses += item[1]

        expense_label = Label(time_expense_screen, text='Net Expense is: %s' % (expenses))
        expense_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Expense WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()

        time_expense_list = c.fetchall()

        for i in range(len(time_expense_list)):
            show_time_expense.insert('', 'end', text = '', values = (time_expense_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_time_expense.place(relx = 0, rely = 0.1)


# Check income


def total_income():
    total_income_screen = Frame(root, bg='white', width=500, height=500)
    total_income_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_total_income_screen = Button(total_income_screen, text='back', command=total_income_screen.destroy)
    quit_total_income_screen.place(relx=0, rely=0, anchor='nw')

    show_total_income = ttk.Treeview(total_income_screen,  height = 25)
    show_total_income['columns'] = ('one', 'two', 'three', 'four')

    show_total_income.column('#0', width = 0)
    show_total_income.column('one', width = 100)
    show_total_income.column('two', width = 100)
    show_total_income.column('three', width = 100)
    show_total_income.column('four', width = 200)

    show_total_income.heading('one', text = 'Date', anchor = 'w')
    show_total_income.heading('two', text = 'Income', anchor = 'w')
    show_total_income.heading('three', text = 'Source', anchor = 'w')
    show_total_income.heading('four', text = 'Notes', anchor = 'w')

    total_expense_list = []

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    c.execute("SELECT * FROM Income")
    conn.commit()

    total_income_list = c.fetchall()

    for i in range(len(total_income_list)):
        show_total_income.insert('', 'end', text = '', values = (total_income_list[i]))

    conn.commit()

    net_income = 0

    c.execute("SELECT * FROM Income")
    conn.commit()
    for item in c.fetchall():
        net_income += item[1]

    net_income_label = Label(total_income_screen, text='Net Income is: %s' % (net_income))
    net_income_label.place(relx=1, rely=1, anchor='se')

    c.close()
    conn.close()

    show_total_income.place(relx = 0, rely = 0.1)


# Check category income


def category_income(category):
    income_screen = Frame(root, bg='white', width=500, height=500)
    income_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_income_screen = Button(income_screen, text='back', command=income_screen.destroy)
    quit_income_screen.place(relx=0, rely=0, anchor='nw')

    show_income = ttk.Treeview(income_screen,  height = 25)
    show_income['columns'] = ('one', 'two', 'three', 'four')

    show_income.column('#0', width = 0)
    show_income.column('one', width = 100)
    show_income.column('two', width = 100)
    show_income.column('three', width = 100)
    show_income.column('four', width = 200)

    show_income.heading('one', text = 'Date', anchor = 'w')
    show_income.heading('two', text = 'Income', anchor = 'w')
    show_income.heading('three', text = 'Source', anchor = 'w')
    show_income.heading('four', text = 'Notes', anchor = 'w')

    expense_list = []

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    c.execute("SELECT * FROM Income WHERE Source=?", (category,))
    conn.commit()

    income_list = c.fetchall()

    for i in range(len(income_list)):
        show_income.insert('', 'end', text = '', values = (income_list[i]))

    conn.commit()

    income = 0

    c.execute("SELECT * FROM Income WHERE Source=?", (category,))
    conn.commit()
    for item in c.fetchall():
        income += item[1]

    income_label = Label(income_screen, text='%s Income is: %s' % (category, income))
    income_label.place(relx=1, rely=1, anchor='se')

    c.close()
    conn.close()

    show_income.place(relx = 0, rely = 0.1)


# Time Income


def time_income(time):
    time_income_screen = Frame(root, bg='white', width=500, height=500)
    time_income_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_time_income_screen = Button(time_income_screen, text='back', command=time_income_screen.destroy)
    quit_time_income_screen.place(relx=0, rely=0, anchor='nw')

    show_time_income = ttk.Treeview(time_income_screen,  height = 25)
    show_time_income['columns'] = ('one', 'two', 'three', 'four')

    show_time_income.column('#0', width = 0)
    show_time_income.column('one', width = 150)
    show_time_income.column('two', width = 150)
    show_time_income.column('three', width = 200)

    show_time_income.heading('one', text = 'Date', anchor = 'w')
    show_time_income.heading('two', text = 'Income', anchor = 'w')
    show_time_income.heading('three', text = 'Source', anchor = 'w')
    show_time_income.heading('four', text= 'Notes', anchor='w')

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    income = 0

    if time == 'day':
        today = datetime.date.today()
        date = today.strftime('%Y-%m-%d')

        c.execute("SELECT * FROM Income WHERE Date = ? ", (date,))
        conn.commit()
        for item in c.fetchall():
            income += item[1]

        income_label = Label(time_income_screen, text='Net Income is: %s' % (income))
        income_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Income WHERE Date = ? ", (date,))
        conn.commit()

        time_income_list = c.fetchall()

        for i in range(len(time_income_list)):
            show_time_income.insert('', 'end', text = '', values = (time_income_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_time_income.place(relx = 0, rely = 0.1)

    elif time == 'month':
        today = datetime.date.today()
        date = today.strftime('%Y-%m')

        upper_combine = date + '-01'
        upper = ''.join(upper_combine)

        lower_combine = date + '-31'
        lower = ''.join(lower_combine)

        c.execute("SELECT * FROM Income WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            income += item[1]

        expense_label = Label(time_income_screen, text='Net Income is: %s' % (income))
        expense_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Income WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()

        time_income_list = c.fetchall()

        for i in range(len(time_income_list)):
            show_time_income.insert('', 'end', text = '', values = (time_income_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_time_income.place(relx = 0, rely = 0.1)

    elif time == 'year':
        today = datetime.date.today()
        date = today.strftime('%Y')

        upper_combine = date + '-01-01'
        upper = ''.join(upper_combine)

        lower_combine = date + '-12-31'
        lower = ''.join(lower_combine)

        c.execute("SELECT * FROM Income WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            income += item[1]

        income_label = Label(time_income_screen, text='Net Income is: %s' % (income))
        income_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Income WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()

        time_income_list = c.fetchall()

        for i in range(len(time_income_list)):
            show_time_income.insert('', 'end', text = '', values = (time_income_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_time_income.place(relx = 0, rely = 0.1)


# Check balance

def total_balance():
    total_balance_screen = Frame(root, bg='white', width=500, height=500)
    total_balance_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_total_balance_screen = Button(total_balance_screen, text='back', command=total_balance_screen.destroy)
    quit_total_balance_screen.place(relx=0, rely=0, anchor='nw')

    show_total_balance = ttk.Treeview(total_balance_screen,  height = 25)
    show_total_balance['columns'] = ('one', 'two', 'three')

    show_total_balance.column('#0', width = 0)
    show_total_balance.column('one', width = 150)
    show_total_balance.column('two', width = 150)
    show_total_balance.column('three', width = 200)

    show_total_balance.heading('one', text = 'Date', anchor = 'w')
    show_total_balance.heading('two', text = 'Type', anchor = 'w')
    show_total_balance.heading('three', text = 'Amount', anchor = 'w')

    total_balance_list = []

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    positive_balance = 0
    negative_balance = 0

    c.execute("SELECT * FROM Balance WHERE Type = 'Income'")
    conn.commit()
    for item in c.fetchall():
        positive_balance += item[2]

    c.execute("SELECT * FROM Balance WHERE Type = 'Expense'")
    conn.commit()
    for item in c.fetchall():
        negative_balance += item[2]

    net_balance = positive_balance - negative_balance

    net_balance_label = Label(total_balance_screen, text='Net Balance is: %s' % (net_balance))
    net_balance_label.place(relx=1, rely=1, anchor='se')

    c.execute("SELECT * FROM Balance")
    conn.commit()

    total_balance_list = c.fetchall()

    for i in range(len(total_balance_list)):
        show_total_balance.insert('', 'end', text = '', values = (total_balance_list[i]))

    conn.commit()

    c.close()
    conn.close()

    show_total_balance.place(relx = 0, rely = 0.1)


# Time Balance


def category_balance(category):
    category_balance_screen = Frame(root, bg='white', width=500, height=500)
    category_balance_screen.place(relx=0.5, rely=0.5, anchor='center')

    quit_category_balance_screen = Button(category_balance_screen, text='back', command=category_balance_screen.destroy)
    quit_category_balance_screen.place(relx=0, rely=0, anchor='nw')

    show_category_balance = ttk.Treeview(category_balance_screen,  height = 25)
    show_category_balance['columns'] = ('one', 'two', 'three')

    show_category_balance.column('#0', width = 0)
    show_category_balance.column('one', width = 150)
    show_category_balance.column('two', width = 150)
    show_category_balance.column('three', width = 200)

    show_category_balance.heading('one', text = 'Date', anchor = 'w')
    show_category_balance.heading('two', text = 'Type', anchor = 'w')
    show_category_balance.heading('three', text = 'Amount', anchor = 'w')

    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    positive_balance = 0
    negative_balance = 0
    category_balance_list = []

    if category == 'day':
        today = datetime.date.today()
        date = today.strftime('%Y-%m-%d')

        c.execute("SELECT * FROM Balance WHERE Type = 'Income' and Date = ? ", (date,))
        conn.commit()
        for item in c.fetchall():
            positive_balance += item[2]

        c.execute("SELECT * FROM Balance WHERE Type = 'Expense' and Date = ? ", (date,))
        conn.commit()
        for item in c.fetchall():
            negative_balance += item[2]

        net_balance = positive_balance - negative_balance

        net_balance_label = Label(category_balance_screen, text='Net Balance is: %s' % (net_balance))
        net_balance_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Balance WHERE Date = ? ", (date,))
        conn.commit()

        category_balance_list = c.fetchall()

        for i in range(len(category_balance_list)):
            show_category_balance.insert('', 'end', text = '', values = (category_balance_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_category_balance.place(relx = 0, rely = 0.1)

    elif category == 'month':
        today = datetime.date.today()
        date = today.strftime('%Y-%m')

        upper_combine = date + '-01'
        upper = ''.join(upper_combine)

        lower_combine = date + '-31'
        lower = ''.join(lower_combine)

        c.execute("SELECT * FROM Balance WHERE Type = 'Income' and Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            positive_balance += item[2]

        c.execute("SELECT * FROM Balance WHERE Type = 'Expense' and Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            negative_balance += item[2]

        net_balance = positive_balance - negative_balance

        net_balance_label = Label(category_balance_screen, text='Net Balance is: %s' % (net_balance))
        net_balance_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Balance WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()

        category_balance_list = c.fetchall()

        for i in range(len(category_balance_list)):
            show_category_balance.insert('', 'end', text = '', values = (category_balance_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_category_balance.place(relx = 0, rely = 0.1)

    elif category == 'year':
        today = datetime.date.today()
        date = today.strftime('%Y')

        upper_combine = date + '-01-01'
        upper = ''.join(upper_combine)

        lower_combine = date + '-12-31'
        lower = ''.join(lower_combine)

        c.execute("SELECT * FROM Balance WHERE Type = 'Income' and Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            positive_balance += item[2]

        c.execute("SELECT * FROM Balance WHERE Type = 'Expense' and Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()
        for item in c.fetchall():
            negative_balance += item[2]

        net_balance = positive_balance - negative_balance

        net_balance_label = Label(category_balance_screen, text='Net Balance is: %s' % (net_balance))
        net_balance_label.place(relx=1, rely=1, anchor='se')

        c.execute("SELECT * FROM Balance WHERE Date BETWEEN ? and ?", (upper, lower,))
        conn.commit()

        category_balance_list = c.fetchall()

        for i in range(len(category_balance_list)):
            show_category_balance.insert('', 'end', text = '', values = (category_balance_list[i]))

        conn.commit()

        c.close()
        conn.close()

        show_category_balance.place(relx = 0, rely = 0.1)


# Reset Functions


def reset(data):
    conn = sqlite3.connect('Financial Tracker.db ')
    c = conn.cursor()

    if data == 'Expense' or data == 'All':
        c.execute('DELETE FROM Expense')
        conn.commit()

        c.execute('DELETE FROM Balance WHERE Type = "Expense"')
        conn.commit()

    if data == 'Income' or data == 'All':
        c.execute('DELETE FROM Income')
        conn.commit()

        c.execute('DELETE FROM Balance WHERE Type = "Income"')
        conn.commit()

    c.close()
    conn.close()


# Log out


def log_out():
    create_welcome()


# Expense Menu

expense_menu = Menu(menu)
menu.add_cascade(label = 'Expense', menu = expense_menu)

expense_menu.add_command(label = 'Total', command = total_expense)
expense_menu.add_separator()

sort_expense_menu = Menu(expense_menu)
expense_menu.add_cascade(label = 'By Category', menu = sort_expense_menu)

sort_expense_menu.add_command(label = 'Travel', command = lambda: category_expense('Travel'))
sort_expense_menu.add_command(label = 'Food', command = lambda: category_expense('Food'))
sort_expense_menu.add_command(label = 'Entertainment', command = lambda: category_expense('Entertainment'))
sort_expense_menu.add_command(label = 'Fees', command = lambda: category_expense('Fees'))
sort_expense_menu.add_command(label = 'Others', command = lambda: category_expense('Others'))

expense_menu.add_separator()
expense_menu.add_command(label = 'Daily Expense', command = lambda: time_expense('day'))
expense_menu.add_command(label = 'Monthly Expense', command = lambda: time_expense('month'))
expense_menu.add_command(label = 'Yearly Expense', command = lambda: time_expense('year'))


# Income Menu

income_menu = Menu(menu)
menu.add_cascade(label = 'Income', menu = income_menu)

income_menu.add_command(label = 'Total', command = total_income)
income_menu.add_separator()

income_source_menu = Menu(income_menu)
income_menu.add_cascade(label = 'By Source', menu = income_source_menu)

income_source_menu.add_command(label = 'Allowance', command = lambda: category_income('Allowance'))
income_source_menu.add_command(label = 'Earnings', command = lambda: category_income('Earnings'))
income_source_menu.add_command(label = 'Others', command = lambda: category_income('Others'))

income_menu.add_separator()
income_menu.add_command(label = 'Daily Income', command = lambda: time_income('day'))
income_menu.add_command(label = 'Monthly Income', command = lambda: time_income('month'))
income_menu.add_command(label = 'Yearly Income', command = lambda: time_income('year'))


# Total Menu

balance_menu = Menu(menu)
menu.add_cascade(label = 'Balance', menu = balance_menu)

balance_menu.add_command(label = 'Total Balance', command = total_balance)
balance_menu.add_separator()
balance_menu.add_command(label = 'Daily Balance', command = lambda: category_balance('day'))
balance_menu.add_command(label = 'Monthly Balance', command = lambda: category_balance('month'))
balance_menu.add_command(label = 'Yearly Balance', command = lambda: category_balance('year'))

# Setting Menu

setting_menu = Menu(menu)
menu.add_cascade(label = 'Setting', menu = setting_menu)

setting_menu.add_command(label = 'Reset All', command = lambda: reset('All'))
setting_menu.add_separator()
setting_menu.add_command(label = 'Reset Expense Data', command = lambda: reset('Expense'))
setting_menu.add_command(label = 'Reset Income Data', command = lambda: reset('Income'))
setting_menu.add_separator()
setting_menu.add_command(label = 'Log out', command = log_out)


# Home screen


def create_home_screen():
    home_screen = Frame(root, bg = '#21969e', width = 500, height = 500)
    home_screen.place(relx = 0.5, rely = 0.5, anchor = 'center')

    # Expense Entry Screen

    def expense_entry():
        global expense_amount, expense_purpose, expense_notes

        expense_entry_screen = Frame(root, bg='white', width=500, height=500)
        expense_entry_screen.place(relx=0.5, rely=0.5, anchor='center')

        quit_expense_entry_screen = Button(expense_entry_screen, text='back', command=expense_entry_screen.destroy)
        quit_expense_entry_screen.place(relx=0, rely=0, anchor='nw')

        expense_amount_label = Label(expense_entry_screen, text='Amount Spent: ')
        expense_amount_label.place(x=100, y=150)

        expense_amount_input = Entry(expense_entry_screen)
        expense_amount_input.place(x=220, y=150)

        expense_purpose_label = Label(expense_entry_screen, text='Purpose:  ')
        expense_purpose_label.place(x=100, y=200)

        expense_purpose_input = ttk.Combobox(expense_entry_screen,
                                             values=['Travel', 'Food', 'Entertainment', 'Fees', 'Others'])

        expense_purpose_input.place(x=220, y=200)

        expense_notes_label = Label(expense_entry_screen, text='Notes (optional) : ')
        expense_notes_label.place(x=100, y=250)

        expense_notes_input = Entry(expense_entry_screen)
        expense_notes_input.place(x=220, y=250)

        def save_expense():
            date = datetime.date.today()
            expense_amount = expense_amount_input.get()
            expense_purpose = expense_purpose_input.get()
            expense_notes = expense_notes_input.get()
            type = 'Expense'

            conn = sqlite3.connect('Financial Tracker.db ')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Expense (
                                        Date BLOB, 
                                        Expense REAL,
                                        Purpose TEXT,
                                        Note BLOB
                                        )''')

            c.execute(
                '''INSERT INTO Expense (Date, Expense, Purpose, Note) VALUES (:date, :amount, :purpose, :notes)''',
                {'date': date, 'amount': expense_amount, 'purpose': expense_purpose, 'notes': expense_notes})

            conn.commit()

            c.execute('''CREATE TABLE IF NOT EXISTS Balance (
                                                Date BLOB,
                                                Type TEXT, 
                                                Amount REAL
                                                )''')

            c.execute('''INSERT INTO Balance (Date, Type, Amount) VALUES (:date, :type, :amount)''',
                      {'date': date, 'type': type, 'amount': expense_amount})

            conn.commit()

            c.close()
            conn.close()

            expense_amount_input.delete(0, END)
            expense_purpose_input.delete(0, END)
            expense_notes_input.delete(0, END)

        expense_submit = Button(expense_entry_screen, text='Submit', command=save_expense)
        expense_submit.place(relx=0.5, y=320)

    expense_entry_button = Button(home_screen, text = 'Expense Entry', width = 15, height = 4, command = expense_entry)
    expense_entry_button.place(relx = 0.3, rely = 0.5, anchor = 'center')


# Income Entry Screen


    def income_entry():
        global income_amount, income_source, income_notes

        income_entry_screen = Frame(root, bg='white', width=500, height=500)
        income_entry_screen.place(relx=0.5, rely=0.5, anchor='center')

        quit_income_entry_screen = Button(income_entry_screen, text='back', command=income_entry_screen.destroy)
        quit_income_entry_screen.place(relx=0, rely=0, anchor='nw')

        income_amount_label = Label(income_entry_screen, text='Amount Earned: ')
        income_amount_label.place(x=100, y=150)

        income_amount_input = Entry(income_entry_screen)
        income_amount_input.place(x=220, y=150)

        income_source_label = Label(income_entry_screen, text='Source:  ')
        income_source_label.place(x=100, y=200)

        income_source_input = ttk.Combobox(income_entry_screen,
                                           values=['Allowance', 'Earnings', 'Others'])

        income_source_input.place(x=220, y=200)

        income_notes_label = Label(income_entry_screen, text='Notes (optional) : ')
        income_notes_label.place(x=100, y=250)

        income_notes_input = Entry(income_entry_screen)
        income_notes_input.place(x=220, y=250)

        def save_income():
            date = datetime.date.today()
            income_amount = income_amount_input.get()
            income_source = income_source_input.get()
            income_notes = income_notes_input.get()
            type = 'Income'

            conn = sqlite3.connect('Financial Tracker.db ')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Income (
                                        Date BLOB, 
                                        Income REAL,
                                        Source TEXT,
                                        Note BLOB
                                        )''')

            c.execute('''INSERT INTO Income (Date, Income, Source, Note) VALUES (:date, :income, :source, :notes)''',
                      {'date': date, 'income': income_amount, 'source': income_source, 'notes': income_notes})

            conn.commit()

            c.execute('''SELECT * FROM Income''')

            conn.commit()

            c.execute('''CREATE TABLE IF NOT EXISTS Balance (
                                                Date BLOB, 
                                                Type  TEXT, 
                                                Amount REAL
                                                )''')
            # c.execute('DELETE FROM Income')

            c.execute('''INSERT INTO Balance (Date, Type, Amount) VALUES (:date, :type, :income)''',
                      {'date': date, 'type': type, 'income': income_amount})

            conn.commit()

            c.execute('''SELECT * FROM Income''')

            conn.commit()

            c.close()
            conn.close()

            income_amount_input.delete(0, END)
            income_source_input.delete(0, END)
            income_notes_input.delete(0, END)

        income_submit = Button(income_entry_screen, text='Submit', command=save_income)
        income_submit.place(relx=0.5, y=320)

    income_entry_button = Button(home_screen, text = 'Income Entry', width = 15, height = 4, command = income_entry)
    income_entry_button.place(relx = 0.7, rely = 0.5, anchor = 'center')


# Log in Screen

def create_login():
    log_in_screen = Frame(root, bg = 'white', width = 500, height = 500)
    log_in_screen.place(relx = 0.5, rely = 0.5, anchor = 'center')

    username_label = Label(log_in_screen, text = 'Username: ')
    username_label.place(x = 100, y = 150)

    username_input = Entry(log_in_screen)
    username_input.place(x = 220, y = 150)

    password_label = Label(log_in_screen, text='Password:  ')
    password_label.place(x=100, y=200)

    password_input = Entry(log_in_screen, show = '*')
    password_input.place(x = 220, y = 200)

    def back_to_welcome():
        log_in_screen.destroy()
        create_welcome()

    quit_login_screen = Button(log_in_screen, text='back', command=back_to_welcome)
    quit_login_screen.place(relx=0, rely=0, anchor='nw')

    def log_in():
        conn = sqlite3.connect('Financial Tracker.db ')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS Login (
                                        Username BLOB, 
                                        Password BLOB)''')

        conn.commit()

        c.execute("SELECT * FROM Login")
        conn.commit()
        username, password = c.fetchone()

        c.close()
        conn.close()

        if username_input.get() == username and password_input.get() == password:
            log_in_screen.destroy()
            create_home_screen()
        elif username_input.get() != username and password_input.get() == password:
            incorrect_label = Label(log_in_screen, text = 'Incorrect', fg = 'red')
            incorrect_label.place(relx=0.5, y=400, anchor = 's')
            username_input.delete(0, END)
        elif username_input.get() == username and password_input.get() != password:
            incorrect_label = Label(log_in_screen, text='Incorrect', fg='red')
            incorrect_label.place(relx=0.5, y=400, anchor = 's')
            password_input.delete(0, END)
        else:
            incorrect_label = Label(log_in_screen, text='Incorrect', fg='red')
            incorrect_label.place(relx=0.5, y=400, anchor = 's')
            username_input.delete(0, END)
            password_input.delete(0, END)

    login_submit = Button(log_in_screen, text='Submit', command = log_in)
    login_submit.place(relx=0.6, y=270)

    def change_password():
        change_password_screen =  Frame(log_in_screen, width = 500, height = 500)
        change_password_screen.place(relx = 0.5, rely = 0.5, anchor = 'center')

        old_password_label = Label(change_password_screen, text='Old Password: ')
        old_password_label.place(x=110, y=150)

        old_password_input = Entry(change_password_screen, show='*')
        old_password_input.place(x=220, y=150)

        new_password_label = Label(change_password_screen, text='New Password:  ')
        new_password_label.place(x=105, y=200)

        new_password_input = Entry(change_password_screen, show='*')
        new_password_input.place(x=220, y=200)

        new_password_check_label = Label(change_password_screen, text='New Password Again:  ')
        new_password_check_label.place(x=70, y=250)

        new_password_check_input = Entry(change_password_screen, show='*')
        new_password_check_input.place(x=220, y=250)

        quit_change_password_screen = Button(change_password_screen, text='back', command=change_password_screen.destroy)
        quit_change_password_screen.place(relx=0, rely=0, anchor='nw')

        def confirm_change_password():
            conn = sqlite3.connect('Financial Tracker.db ')
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS Login (
                                                    Username BLOB, 
                                                    Password BLOB)''')

            conn.commit()

            c.execute("SELECT * FROM Login")
            conn.commit()
            username, password = c.fetchone()

            if old_password_input.get() == password and new_password_input.get() == new_password_check_input.get():
                password = new_password_input.get()
                c.execute("DELETE FROM Login")
                conn.commit()
                c.execute("INSERT INTO Login VALUES (?, ?)", (username, password,))
                conn.commit()
                change_password_screen.destroy()
            elif old_password_input.get() != password:
                old_password_input.delete(0, END)
                label = Label(change_password_screen, text='Incorrect', fg='red')
                label.place(relx=0.5, y=400, anchor='s')
            elif new_password_input.get() != new_password_check_input.get():
                new_password_input.delete(0, END)
                new_password_check_input.delete(0, END)
                label = Label(change_password_screen, text='Incorrect', fg='red')
                label.place(relx=0.5, y=400, anchor='s')
            else:
                old_password_input.delete(0, END)
                new_password_input.delete(0, END)
                new_password_check_input.delete(0, END)
                label = Label(change_password_screen, text='Incorrect', fg='red')
                label.place(relx=0.5, y=400, anchor='s')

            c.close()
            conn.close()

        change_password_submit = Button(change_password_screen, text='Submit', command=confirm_change_password)
        change_password_submit.place(relx=0.5, y=320)

    change_password = Button(log_in_screen, text='Change Password', command = change_password)
    change_password.place(relx=0.25, y=270)


# Welcome Screen

def create_welcome():
    welcome_screen = Frame(root, bg = '#21969e', width = 600, height = 600)
    welcome_screen.place(relx = 0.5, rely = 0.5, anchor = 'center')

    welcome_sign = Label(welcome_screen, text = 'Welcome ', bg = '#21969e', font = ('Times', 48, 'bold'))
    welcome_sign.place(relx = 0.5, rely = 0.3, anchor = 'center')

    marco_sign = Label(welcome_screen, text = 'Marco ', bg = '#21969e', font = ('Times', 48, 'bold'))
    marco_sign.place(relx = 0.5, rely = 0.6, anchor = 'center')

    def destroy_welcome(event):
        welcome_screen.destroy()
        quit_home_screen = Button(root, text='quit', command=root.destroy)
        quit_home_screen.place(relx=0, rely=0, anchor='nw')
        create_login()

    welcome_screen.bind('<Button-1>', destroy_welcome)
    welcome_sign.bind('<Button-1>', destroy_welcome)
    marco_sign.bind('<Button-1>', destroy_welcome)


create_welcome()


root.mainloop()