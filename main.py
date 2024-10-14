import tkinter as tk
from tkinter import *
import sqlite3
from tkcalendar import Calendar
from tkinter import ttk

root = tk.Tk()
root.title("Grocery Management")
root.geometry("1000x800")

# UI

# Home Page
def homePage ():
    home_frame = tk.Frame(bg="alice blue")
    home_frame.place(x = 0 , y = 0 , width =1000 , height = 800 )
    welcome_Text = tk.Label(home_frame , text= "سوپر مارکت ولیعصر" , font = ("" , 30) ,bg="alice blue")
    welcome_Text.place( y=20 , x=400)

    productsBtn = tk.Button(home_frame , text = "محصولات" , font = ("" , 22) , bg = "orange")
    productsBtn.place(x = 420 , y = 200 , width=250 )

    sellBtn = tk.Button(home_frame , text = "فروش" , font = ("" , 22) , bg = "gray" , command = sell) 
    sellBtn.place(x = 420 , y = 300 , width=250 )

    invoiceBtn = tk.Button(home_frame , text = "فاکتور ها" , font = ("" , 22), bg = "orange" , command=Invoice)
    invoiceBtn.place(x = 420 , y = 400 , width=250 )

    exitBtn = tk.Button(home_frame , text = "خروج" , font = ("" , 22) , bg = "gray")
    exitBtn.place(x = 420 , y = 500 , width=250 )

# Sell Page
def sell():
    def getdate ():
        print(cal.get_date())
    sell_frame = tk.Frame(bg="alice blue")
    sell_frame.place(x = 0 , y = 0 , width=1000 , height= 800)
    
    product_label = tk.Label(sell_frame , text= "نام محصول" , font=("" , 20),bg="alice blue")
    product_label.place( x = 60 , y = 50)
    productInput = tk.Entry(sell_frame)
    productInput.place(x = 200 , y = 55 , width=200 , height=30)

    count_label = tk.Label(sell_frame , text= "تعداد" , font=("" , 20),bg="alice blue")
    count_label.place( x = 90 , y = 120)
    countInput = tk.Entry(sell_frame)
    countInput.place(x = 200 , y = 125 , width=200 , height=30)
    
    # Date Entry
    cal = Calendar(sell_frame , selectmode = "day" , year = 2024 , month = 10 , day = 14 )
    cal.place(x = 170 , y = 200)
    date_label = tk.Label(sell_frame , text= "تاریخ" , font=("" , 20),bg="alice blue")
    date_label.place( x = 90 , y = 190)
    
    # Add to Cart Button
    addCart = tk.Button(sell_frame , text="اضافه به سبد خرید" , font = ("Arial" , 20) , bg = "Green" , command=getdate)
    addCart.place(x = 180 , y = 450 )
    
    #  Final Invoice
    invoiceBtn = tk.Button(sell_frame , text = "فاکتور نهایی" , font=("" , 20) , bg="Orange")
    invoiceBtn.place(x= 650 , y = 600)
    
    #  Invoice Display
    scroll = tk.Scrollbar(sell_frame)
    textBox = tk.Text(sell_frame  , font = ("Arial" , 16), yscrollcommand=scroll.set)
    textBox.place(x = 450 , y = 50 ,width = 500 , height = 500 )
    scroll.place(x= 950 , y = 50 , width = 30 , height = 500)
    scroll.configure(command=textBox.yview)
    
    # Back
    backBtn = tk.Button(sell_frame , text= "بازگشت" , font=("" , 20) , bg = "Grey" , command=homePage)
    backBtn.place(x = 670 , y = 670)

# Invoices Page
def Invoice():
    invoice_frame = tk.Frame(bg = "alice blue")
    invoice_frame.place(x= 0 , y = 0 , width=1000 , height= 800 )
    
    searchBtn = tk.Button(invoice_frame , text = "جستجو" , font=("" , 20) , bg = "orange")
    searchBtn.place( x = 80 , y = 50 , width= 120 , height=40 )
    
    searchInput = tk.Entry(invoice_frame)
    searchInput.place(x = 230 , y = 55 , width=300 , height=30)
    
    invoiceDisplaAllBtn = tk.Button(invoice_frame , text = "نمایش همه فاکتورها" , font=("" , 20) , bg = "orange")
    invoiceDisplaAllBtn.place( x = 700 , y = 40 , width= 200 , height=60 )
    
    backBtn = tk.Button(invoice_frame , text= "بازگشت" , font=("" , 20) , bg = "Grey" , command=homePage)
    backBtn.place(x = 40 , y =745 , height=40)
    
    # add Table
    invoiceTable = ttk.Treeview(invoice_frame , columns=('number' , "invoice_id" , "date" , "cost") , show = "headings")
    invoiceTable.place(y=150 , x = 40 ,  width = 900 , height= 590)
    invoiceTable.heading('number', text="ردیف" )
    invoiceTable.heading('invoice_id', text="شماره فاکتور" )
    invoiceTable.heading('date', text="تاریخ" )
    invoiceTable.heading('cost', text="مبلغ فاکتور" )
    
    
    # isnert value
    invoiceTable.insert(parent="" , index= 0 , values=(1,2,3,4))
    
homePage()
root.mainloop()
