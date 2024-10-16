import tkinter as tk
from tkinter import *
import sqlite3
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import random

root = tk.Tk()
root.title("Grocery Management")
root.geometry("1000x800")

# data Bank
con = sqlite3.connect("shop.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS shop(
            name text PRIMARY KEY , 
            sell INT ,
            buy INT,
            count INT);''');

cur.execute('''CREATE TABLE IF NOT EXISTS invoice(
            id  PRIMARY KEY ,
            date text ,
            count INT ,
            total INT);''');

con.commit()

# UI

# Home Page
def homePage ():
    home_frame = tk.Frame(bg="alice blue")
    home_frame.place(x = 0 , y = 0 , width =1000 , height = 800 )
    welcome_Text = tk.Label(home_frame , text= "سوپر مارکت ولیعصر" , font = ("" , 30) ,bg="alice blue")
    welcome_Text.place( y=20 , x=400)

    productsBtn = tk.Button(home_frame , text = "محصولات" , font = ("" , 22) , bg = "orange" ,command=Shop.productdisplay)
    productsBtn.place(x = 420 , y = 200 , width=250 )

    sellBtn = tk.Button(home_frame , text = "فروش" , font = ("" , 22) , bg = "gray" , command = sellPage) 
    sellBtn.place(x = 420 , y = 300 , width=250 )

    invoiceBtn = tk.Button(home_frame , text = "فاکتور ها" , font = ("" , 22), bg = "orange" , command=Invoice)
    invoiceBtn.place(x = 420 , y = 400 , width=250 )

    exitBtn = tk.Button(home_frame , text = "خروج" , font = ("" , 22) , bg = "gray" , command= closePage)
    exitBtn.place(x = 420 , y = 500 , width=250 )

# Shop Class

class Shop :

    def productdisplay ():
        product_frame = tk.Frame(bg = "alice blue")
        product_frame.place(x = 0 , y = 0 , width = 1000 , height = 800)
        
        global nameInput , sellPriceInput , buyPriceInput , countnumberInput
        
        # product Name
        nameLabel = tk.Label(product_frame , text = "نام کالا" , font = ("Arial" , 18) , bg = "alice blue")
        nameLabel.place( x = 50 , y = 22 , width = 100 , height = 20)

        nameInput = tk.Entry(product_frame ,font = ("Arial" , 12)) 
        nameInput.place( x = 180 , y = 20 , width = 200 , height = 25)

        # Sell price
        sellPriceLabel = tk.Label(product_frame , text = "قیمت فروش" , font = ("Arial" , 18) , bg = "alice blue")
        sellPriceLabel.place( x = 400 , y = 22 , width = 100 , height = 20)

        sellPriceInput = tk.Entry(product_frame ,font = ("Arial" , 12) )
        sellPriceInput.place( x = 520 , y = 20 , width = 200 , height = 25)

        # Buy price
        buyPriceLabel = tk.Label(product_frame , text = "قیمت خرید" , font = ("Arial" , 18) , bg = "alice blue")
        buyPriceLabel.place( x = 50 , y = 80 , width = 100 , height = 20)

        buyPriceInput = tk.Entry(product_frame ,font = ("Arial" , 12) )
        buyPriceInput.place( x = 180 , y = 78 , width = 200 , height = 25)

        # count
        countLabel = tk.Label(product_frame , text = "موجودی" , font = ("Arial" , 18) , bg = "alice blue")
        countLabel.place( x = 400 , y = 80 , width = 100 , height = 20)

        countnumberInput = tk.Entry(product_frame ,font = ("Arial" , 12) )
        countnumberInput.place( x = 520 , y = 78 , width = 200 , height = 25)

        # Buttons -----------------

        #  Display BTN
        displayBtn = tk.Button(product_frame , text="مشاهده همه" , font = ("Arial" , 18) , command = Shop.displayAll )
        displayBtn.place(x=800 , y=20 , width=120 , height=30)


        # Add BTN
        addBtn = tk.Button(product_frame , text="اضافه کردن" , font = ("Arial" , 18) , command= Shop.add )
        addBtn.place(x=800 , y=60 , width=120 , height=30)

        # Update BTN
        rmvBtn = tk.Button(product_frame , text="ویرایش " , font = ("Arial" , 18) )
        rmvBtn.place(x=800 , y=100 , width=120 , height=30)

        # Remove BTN
        rmvBtn = tk.Button(product_frame , text="حذف کردن " , font = ("Arial" , 18) , command = Shop.remove )
        rmvBtn.place(x=800 , y=140 , width=120 , height=30)

        # Close BTN
        closeBtn = tk.Button(product_frame , text="بازگشت" , font = ("Arial" , 18)  , command= homePage , bg = "orange")
        closeBtn.place(x=800 , y=730 , width=120 , height=50 )

        # Search BTN
        searchBtn = tk.Button(product_frame , text=" جستجو کالا" , font = ("Arial" , 18))
        searchBtn.place(x=50 , y=150 , width=120 , height=30)
        
        searchInput = tk.Entry(product_frame)
        searchInput.place(x = 180 , y = 150 , width = 200 , height = 30)
        
        # textRsult
        global productdisplayTable
        productdisplayTable = ttk.Treeview(product_frame , columns=("name" , "sell" , "buy" , "count")  , show = "headings")
        productdisplayTable.heading("name" , text="نام کالا")
        productdisplayTable.heading("sell" , text="قیمت فروش")
        productdisplayTable.heading("buy" , text="قیمت خرید")
        productdisplayTable.heading("count" , text="موجودی")
        productdisplayTable.place(x = 50 , y = 200 , width = 870 , height = 500)
    
    # Add Function
    def add ():

        global name , sell , buy , count
        name = nameInput.get()
        sell = int(sellPriceInput.get())
        buy = int(buyPriceInput.get())
        count = int(countnumberInput.get())
        data = [name , sell , buy , count]
        
        if name == " " or sell == 0 or buy == 0 or count == 0 :
             messagebox.showerror("Error" , "لطفا فیلد های مورد نظر را پر کنید")
        else:
            cur.execute('''INSERT INTO shop VALUES(?,?,?,?);''' , data)
            con.commit()
            
            nameInput.delete("0" , "end")
            sellPriceInput.delete("0" , "end")
            buyPriceInput.delete("0" , "end")
            countnumberInput.delete("0" , "end")

    # Display Function
    def displayAll ():
    
        cur.execute('''SELECT * FROM shop;''')
        result = cur.fetchall()
        
        for record in productdisplayTable.get_children():
            productdisplayTable.delete(record)
            
        for i in result:
            productdisplayTable.insert(parent="" , index= 0 , values=(i))    
        
    # Remove Function
    def remove():
        name = nameInput.get()
        cur.execute('''SELECT * FROM shop  WHERE name = ?''' , (name,))
        result = cur.fetchall()
        if name == "":
            messagebox.showerror("Error" , "!لطفا کالای موردنظر را انتخاب کنید")
        else :
            for i in result:
                nameInput.insert('0' , i[0])
                sellPriceInput.insert('0' , i[1])
                buyPriceInput.insert('0' , i[2])
                countnumberInput.insert('0' , i[3])

                Q = messagebox.askyesno("اخطار" , f'آیا مطمئن هستید میخواهید {name} را حذف کنید؟')
                if Q :
                    cur.execute('''DELETE FROM shop WHERE name = ?;''' , (name,))
                    con.commit()
                    nameInput.delete("0" , "end")
                    sellPriceInput.delete("0" , "end")
                    buyPriceInput.delete("0" , "end")
                    countnumberInput.delete("0" , "end")
                    
    # Update Button
    # def update ():
        
        
# Sell Page
def sellPage():
    sell_frame = tk.Frame(bg="alice blue")
    sell_frame.place(x = 0 , y = 0 , width=1000 , height= 800)
    
    product_label = tk.Label(sell_frame , text= "نام محصول" , font=("" , 20),bg="alice blue")
    product_label.place( x = 60 , y = 50)
    
    global productInput
    productInput = tk.Entry(sell_frame)
    productInput.place(x = 200 , y = 55 , width=200 , height=30)

    count_label = tk.Label(sell_frame , text= "تعداد" , font=("" , 20),bg="alice blue")
    count_label.place( x = 90 , y = 120)

    global countInput
    countInput = tk.Entry(sell_frame)
    countInput.place(x = 200 , y = 125 , width=200 , height=30)
    
    # Date Entry
    global cal
    cal = Calendar(sell_frame , selectmode = "day" , year = datetime.now().year , month = datetime.now().month , day = datetime.now().day )
    cal.place(x = 170 , y = 200)

    date_label = tk.Label(sell_frame , text= "تاریخ" , font=("" , 20),bg="alice blue")
    date_label.place( x = 90 , y = 190)
    
    # Add to Cart Button
    addCart = tk.Button(sell_frame , text="اضافه به سبد خرید" , font = ("Arial" , 20) , bg = "Green" , command=sellApp.addCart)
    addCart.place(x = 180 , y = 450 )

    # Add to Cart Button
    deleteCart = tk.Button(sell_frame , text="حذف سبد خرید" , font = ("Arial" , 20) , bg = "red3" , command=sellApp.deleteCart)
    deleteCart.place(x = 180 , y = 520 , width=191)
    
    #  Final Invoice
    invoiceBtn = tk.Button(sell_frame , text = "فاکتور نهایی" , font=("" , 20) , bg="Orange")
    invoiceBtn.place(x= 650 , y = 600)
    
    #  Invoice Display
    scroll = tk.Scrollbar(sell_frame)
    global textBox
    textBox = tk.Text(sell_frame  , font = ("Arial" , 16), yscrollcommand=scroll.set)
    textBox.place(x = 450 , y = 50 ,width = 500 , height = 500 )
    scroll.place(x= 950 , y = 50 , width = 30 , height = 500)
    scroll.configure(command=textBox.yview)
    
          
    textBox.insert("end" , "                   به سوپر مارکت ولیعصر خوش آمدید");
    textBox.insert("end" , "                                                      فاکتور فروش");
    textBox.insert("end" , "                                          =====================================");
    textBox.insert("end" , "                    نام کالا                  تعداد                   قیمت");
    textBox.insert("end" , "\n");
    textBox.insert("end" , "\n");
    
    # Back
    backBtn = tk.Button(sell_frame , text= "بازگشت" , font=("" , 20) , bg = "Grey" , command=homePage)
    backBtn.place(x = 670 , y = 670)

# Sell Function
class sellApp:
    def addCart ():
        # data for making an invoice table
        product = productInput.get()
        count = int(countInput.get())
        date = cal.get_date()
        # Uuid 
        i = random.randint(10000 , 99999)
        Uuid = f'#B{i}'
        
        # getting price and amount of stock
        cur.execute('''SELECT * FROM shop WHERE name = ?;''' , (product,))
        result = cur.fetchall()

        for p in result:
            price = p[1] * count;
            Inventory_amount = p[3]
        
        current_amount = Inventory_amount - count;
        prices = []
        if not result :
            messagebox.showerror("erorr" , "اطلاعات وارد شده نادرست است!")
        if count > Inventory_amount :
            messagebox.showerror("error" , f"مقدار انتخاب شده بیش از موجودی انبار می باشد \n                       موجودی: {Inventory_amount}")
        else:
            # if textBox.get('1.0' , 'end-1c'):
            #     textBox.delete('4.0' , "end");

            textBox.insert("end" , f"                 {product}                {count}              {price}");
            textBox.insert("end" , "\n");
            textBox.insert("end" , "\n");
            productInput.delete("0" , "end")
            countInput.delete("0" , "end")

            prices.append(price)
            print(prices)
            
# Delete from Cart   
    def deleteCart():
        textBox.delete("2.0" , "end-1c")
                   
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

def closePage():

    root.destroy()
# Shop.productdisplay()
# homePage()
sellPage()
root.mainloop()
