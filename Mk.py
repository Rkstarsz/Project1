from secrets import choice
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tempfile
import os
import tkinter.messagebox
from PIL import Image,ImageTk
from numpy import delete


class pos:

    def __init__(self,root):
        self.root = root
        self.root.title("7th Even-The Cake Shop ")
        self.root.geometry("1350x750+0+0")
        self.root.configure(bg="Dark Red")
        self.input_value = True

        img=Image.open("images/Cake1.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        img=Image.open("images/Cake2.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img)

        
        img=Image.open("images/Cake3.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img)

        img=Image.open("images/Cake4.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img)

        img=Image.open("images/Cake5.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img)

        img=Image.open("images/Cake6.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img)

        img=Image.open("images/Coffe1.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img)

        img=Image.open("images/Coffe2.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_7=ImageTk.PhotoImage(img)
        
        img=Image.open("images/Coffe3.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_8=ImageTk.PhotoImage(img)

        img=Image.open("images/Coffe4.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_9=ImageTk.PhotoImage(img)

        img=Image.open("images/Coffe5.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_10=ImageTk.PhotoImage(img)

        img=Image.open("images/Coffe6.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_11=ImageTk.PhotoImage(img)

        img=Image.open("images/Drink1.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_12=ImageTk.PhotoImage(img)

        img=Image.open("images/Drink2.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img)
        
        img=Image.open("images/Drink3.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_14=ImageTk.PhotoImage(img)

        img=Image.open("images/Drink4.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_15=ImageTk.PhotoImage(img)

        img=Image.open("images/Drink5.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_16=ImageTk.PhotoImage(img)

        img=Image.open("images/Drink6.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_17=ImageTk.PhotoImage(img)

        img=Image.open("images/Ice1.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_18=ImageTk.PhotoImage(img)

        img=Image.open("images/Ice2.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_19=ImageTk.PhotoImage(img)
        
        img=Image.open("images/Ice3.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_20=ImageTk.PhotoImage(img)

        img=Image.open("images/Ice4.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_21=ImageTk.PhotoImage(img)

        img=Image.open("images/Ice5.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_22=ImageTk.PhotoImage(img)

        img=Image.open("images/Ice6.jpg")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg_23=ImageTk.PhotoImage(img)

        global operator
        operator=""
        Change_Input= StringVar()
        Cash_Input= StringVar()
        Tax_Input= StringVar()
        SubTotal_Input= StringVar()
        Total= StringVar()
        Item= StringVar()
        Qty= StringVar()
        Amount= StringVar()
        Choice= StringVar()
        Cash_Input= StringVar()

        MainFrame= Frame(self.root,bg="Purple")
        MainFrame.grid(padx=8,pady=5)

        ButtonFrame= Frame(MainFrame,bd=5,width=1350,height=160,padx=4,pady=4,bg="purple",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame= Frame(MainFrame,bd=5,width=1300,height=400,padx=5,bg="purple",relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFTCover= LabelFrame(DataFrame,bd=5,width=800,height=300,pady=2,relief=RIDGE,
                            bg="purple",font=("arial",12,"bold"),text="7th Even")
        DataFrameLEFTCover.pack(side=LEFT)

        ChangeBtnFrame= Frame(DataFrameLEFTCover,bd=5,width=300,height=460,pady=5,bg="purple",relief=RIDGE)
        ChangeBtnFrame.pack(side=LEFT,padx=4)

        ReceiptFrame= Frame(DataFrameLEFTCover,bd=5,width=200,height=400,pady=5,padx=1,relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT,padx=0)

        FoodItemFrame= LabelFrame(DataFrame,bd=5,width=450,height=300,padx=5,pady=2,relief=RIDGE,bg="purple",
                                 font=("arial",12,"bold"),text="Items")
        FoodItemFrame.pack(side=RIGHT)

        CalFrame= Frame(ButtonFrame,bd=5,width=432,height=140,relief=RIDGE)
        CalFrame.grid(row=0,column=0,padx=5)

        ChangeFrame= Frame(ButtonFrame,bd=5,width=500,height=140,pady=4,relief=RIDGE)
        ChangeFrame.grid(row=0,column=1,padx=5)

        RemoveFrame= Frame(ButtonFrame,bd=5,width=400,height=140,padx=4,pady=4,bg="purple",relief=RIDGE)
        RemoveFrame.grid(row=0,column=2,padx=5)
    
    #==================================Function Calls==================================
        def iprint():
            q = self.txtReceipt.get("1.0", "end - 1c")
            print(q)
            filename = tempfile.mktemp(".txt")
            open(filename, "w") . write(q)
            os.startfile(filename,"print")

        def btnClearDisplay():
            global operator
            operator=""
            Change_Input.set("")
            Cash_Input.set("0")
            Tax_Input.set("")
            SubTotal_Input.set("")
            Total.set("")
            for i in self.POS_record.get_children():
                self.POS_record.delete(i)

        def Change():
            Change_Input.set("")
            Cash_Input.set("0")

        def Delete():
            ItemCost=0.0
            Tax = 2.5
            for child in self.POS_record.get_children():
                ItemCost +=float(self.POS_record.item(child,"values")[2])
            SubTotal_Input.set(str("$%.2f"%(ItemCost)))
            Tax_Input.set(str("$%.2f"%((ItemCost*Tax)/100)))
            Total.set(str("$%.2f"%((ItemCost)+((ItemCost * Tax)/100))))
            Selected_Item=(self.POS_record.selection()[0])
            self.POS_record.delete(Selected_Item)
            giveChange()

        def giveChange():
            ItemCost=0.0
            Tax = 2.5
            CashInput = float(Cash_Input.get())
            for child in self.POS_record.get_children():
                ItemCost +=float(self.POS_record.item(child,"values")[2])
            Change_Input.set(str("$%.2f"%(CashInput-((ItemCost)+((ItemCost * Tax)/100)))))
            if (Cash_Input.get() == "0"):
                Change_Input.set("")
                Method_of_Pay()

        def Method_of_Pay():
            if (choice.get() == "Cash"):
                self.txtCost.focus()
                Cash_Input.set("")
            elif (choice.get()==""):
                Cash_Input.set("0")
                Change_Input.set("") 
    #==============================CalculatorFrame Widget==================================================
        self.lblSubTotal =Label(CalFrame,font=("arial",14,"bold"),text="Sub Total",bd=5)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5)

        self.txtSubTotal = Entry(CalFrame,font=("arial",14,"bold"),bd=2,width=24,justify="left",textvariable=SubTotal_Input)
        self.txtSubTotal.grid(row=0,column=1)

        self.lblTax =Label(CalFrame,font=("arial",14,"bold"),text="Tax",bd=5)
        self.lblTax.grid(row=1,column=0,sticky=W,padx=5)

        self.txtTax = Entry(CalFrame,font=("arial",14,"bold"),bd=2,width=24,justify="left",textvariable=Tax_Input)
        self.txtTax.grid(row=1,column=1)

        self.lblTotal =Label(CalFrame,font=("arial",14,"bold"),text="Total",bd=5)
        self.lblTotal.grid(row=2,column=0,sticky=W,padx=5)

        self.txtTotal = Entry(CalFrame,font=("arial",14,"bold"),bd=2,width=24,justify="left",textvariable=Total)
        self.txtTotal.grid(row=2,column=1)
    #    =======================CalculatorFrame Widget==================================================
        self.lblMoP =Label(ChangeFrame,font=("arial",14,"bold"),text="Method of Payment",bd=2)
        self.lblMoP.grid(row=0,column=0,sticky=W,padx=2)

        self.cboMoP = ttk.Combobox(ChangeFrame,width=36,font=("arial",14,"bold"),state="readonly",textvariable=Choice,justify="right")
        self.cboMoP["values"]=("","Cash","Visa Card","Master Card")
        self.cboMoP.current(0)
        self.cboMoP.grid(row=0,column=1)

        self.lblCost =Label(ChangeFrame,font=("arial",14,"bold"),text="Cost",bd=5)
        self.lblCost.grid(row=1,column=0,sticky=W,padx=2)

        self.txtCost = Entry(ChangeFrame,font=("arial",14,"bold"),bd=2,width=38,textvariable=Cash_Input,justify="right")
        self.txtCost.grid(row=1,column=1)
        self.txtCost.insert(0,"0")

        self.lblChange =Label(ChangeFrame,font=("arial",14,"bold"),text="Change",bd=5)
        self.lblChange.grid(row=2,column=0,sticky=W,padx=2)

        self.txtChange = Entry(ChangeFrame,font=("arial",14,"bold"),bd=2,width=38,textvariable=Change_Input,justify="right")
        self.txtChange.grid(row=2,column=1,sticky=W)
    #    =======================Button,Pay,print,Remove==================================================
        self.btnPay=Button(RemoveFrame,padx=2,font=("arial",15,"bold"),text="Pay",width=10,height=1,bd=2,command=giveChange)
        self.btnPay.grid(row=0,column=0,padx=4,pady=2)

        self.btnPrint=Button(RemoveFrame,padx=2,font=("arial",15,"bold"),text="Print",width=10,height=1,bd=2,command=iprint)
        self.btnPrint.grid(row=1,column=1,padx=4,pady=2)

        self.btnReset=Button(RemoveFrame,padx=2,font=("arial",15,"bold"),text="Reset",width=10,height=1,bd=2,command=btnClearDisplay)
        self.btnReset.grid(row=1,column=0,padx=4,pady=2)

        self.btnRemove=Button(RemoveFrame,padx=2,font=("arial",15,"bold"),text="Remove",width=10,height=1,bd=2,command=Delete)
        self.btnRemove.grid(row=0,column=1,padx=4,pady=2)

    #============================================Function============================
        def IceCake_1():
            itemCost= 2.85
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Rainbow IceCream","1","2.85"))
            self.txtReceipt.insert(END,("Rainbow IceCream"+"\t\t\t"+"2.85"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.85)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.85)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.85)+((itemCost-2.85)*Tax)/100)))

        def IceCake_2():
            itemCost= 2.35
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Vanilla IceCream","1","2.35"))
            self.txtReceipt.insert(END,("Vanilla IceCream"+"\t\t\t"+"2.35"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.35)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.35)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.35)+((itemCost-2.35)*Tax)/100)))

        def IceCake_3():
            itemCost= 1.65
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Brownie IceCream","1","1.65"))
            self.txtReceipt.insert(END,("Brownie IceCream"+"\t\t\t"+"1.65"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.65)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.65)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.65)+((itemCost-1.65)*Tax)/100)))

        def IceCake_4():
            itemCost= 3.12
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("MixFruit IceCream","1","3.12"))
            self.txtReceipt.insert(END,("MixFruit IceCream"+"\t\t\t"+"3.12"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 3.12)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 3.12)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 3.12)+((itemCost-3.12)*Tax)/100)))

        def IceCake_5():
            itemCost= 3.87
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Candy IceCream","1","3.87"))
            self.txtReceipt.insert(END,("Candy IceCream"+"\t\t\t"+"3.87"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 3.87)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 3.87)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 3.87)+((itemCost-3.87)*Tax)/100)))

        def IceCake_6():
            itemCost= 1.67
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Strawberry IceCream","1","1.67"))
            self.txtReceipt.insert(END,("Strawberry IceCream"+"\t\t\t"+"1.67"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.67)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.67)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.67)+((itemCost-1.67)*Tax)/100)))

    #==================================Func for Drinks====
        def Drink_1():
            itemCost= 1.75
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Orange Lemon","1","1.75"))
            self.txtReceipt.insert(END,("Orange Lemon"+"\t\t\t"+"1.75"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.75)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.75)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.75)+((itemCost-1.75)*Tax)/100)))

        def Drink_2():
            itemCost= 1.65
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Black Soda","1","1.65"))
            self.txtReceipt.insert(END,("Black Soda"+"\t\t\t"+"1.65"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.65)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.65)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.65)+((itemCost-1.65)*Tax)/100)))

        def Drink_3():
            itemCost= 2.25
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Lemon Soda","1","2.25"))
            self.txtReceipt.insert(END,("Lemon Soda"+"\t\t\t"+"2.25"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.25)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.25)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.25)+((itemCost-2.25)*Tax)/100)))

        def Drink_4():
            itemCost= 1.35
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Strawberry Shake","1","1.35"))
            self.txtReceipt.insert(END,("Strawberry Shake"+"\t\t\t"+"1.35"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.35)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.35)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.35)+((itemCost-1.35)*Tax)/100)))

        def Drink_5():
            itemCost= 1.95
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Apple Soda","1","1.95"))
            self.txtReceipt.insert(END,("Apple Soda"+"\t\t\t"+"1.95"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.95)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.95)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.95)+((itemCost-1.95)*Tax)/100)))

        def Drink_6():
            itemCost= 1.45
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Blueberry Soda","1","1.45"))
            self.txtReceipt.insert(END,("Blueberry Soda"+"\t\t\t"+"1.45"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.45)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.45)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.45)+((itemCost-1.45)*Tax)/100)))

    #===================Func for Coffee============

        def Coffee_1():
            itemCost= 1.70
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Capuccino","1","1.70"))
            self.txtReceipt.insert(END,("Capuccino"+"\t\t\t"+"1.70"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.70)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.70)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.70)+((itemCost-1.70)*Tax)/100)))

        def Coffee_2():
            itemCost= 1.80
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Classic Cold Coffee","1","1.80"))
            self.txtReceipt.insert(END,("Classic Cold Coffee"+"\t\t\t"+"1.80"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.80)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.80)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.80)+((itemCost-1.80)*Tax)/100)))

        def Coffee_3():
            itemCost= 2.30
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Caramel Salted Coffee","1","2.30"))
            self.txtReceipt.insert(END,("Caramel Salted Coffee"+"\t\t\t"+"2.30"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.30)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.30)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.30)+((itemCost-2.30)*Tax)/100)))

        def Coffee_4():
            itemCost= 1.90
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Choclate Capuccino","1","1.90"))
            self.txtReceipt.insert(END,("Choclate Capuccino"+"\t\t\t"+"1.90"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 1.90)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 1.90)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 1.90)+((itemCost-1.90)*Tax)/100)))

        def Coffee_5():
            itemCost= 3.75
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Slay Coffee","1","3.75"))
            self.txtReceipt.insert(END,("Slay Coffee"+"\t\t\t"+"3.75"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 3.75)))
                Tax_Input.set(str("$%.2f"%(((itemCost -3.75)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 3.75)+((itemCost-3.75)*Tax)/100)))

        def Coffee_6():
            itemCost= 3.90
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("hotChoclate Coffee","1","3.90"))
            self.txtReceipt.insert(END,("hotChoclate Coffee"+"\t\t\t"+"3.90"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 3.90)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 3.90)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 3.90)+((itemCost-3.90)*Tax)/100)))

    #===================Func for Cake============

        def Cake_1():
            itemCost= 2.90
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Choclate Cake","1","2.90"))
            self.txtReceipt.insert(END,("Choclate Cake"+"\t\t\t"+"2.90"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.90)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.90)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.90)+((itemCost-2.90)*Tax)/100)))

        def Cake_2():
            itemCost= 2.20
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("MixFriut Cake","1","2.20"))
            self.txtReceipt.insert(END,("MixFriut Cake"+"\t\t\t"+"2.20"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.20)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.20)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.20)+((itemCost-2.20)*Tax)/100)))

        def Cake_3():
            itemCost= 2.90
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Mango Cake","1","2.90"))
            self.txtReceipt.insert(END,("Mango Cake"+"\t\t\t"+"2.90"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.90)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.90)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.90)+((itemCost-2.90)*Tax)/100)))

        def Cake_4():
            itemCost= 3.20
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Choco Truffle Cake","1","3.20"))
            self.txtReceipt.insert(END,("Choco Truffle Cake"+"\t\t\t"+"3.20"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 3.20)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 3.20)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 3.20)+((itemCost-3.20)*Tax)/100)))

        def Cake_5():
            itemCost= 2.78
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Strawberry Cake","1","2.78"))
            self.txtReceipt.insert(END,("Strawberry Cake"+"\t\t\t"+"2.78"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.78)))
                Tax_Input.set(str("$%.2f"%(((itemCost -2.78)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.78)+((itemCost-2.78)*Tax)/100)))

        def Cake_6():
            itemCost= 2.70
            Tax = 2.5
            self.POS_record.insert("",tk.END,values=("Cranberry Cake","1","2.70"))
            self.txtReceipt.insert(END,("Cranberry Cake"+"\t\t\t"+"2.70"+"\n"))
            for child in self.POS_record.get_children():
                itemCost += float(self.POS_record.item(child,"values")[2])
                SubTotal_Input.set(str("$%.2f"%(itemCost - 2.70)))
                Tax_Input.set(str("$%.2f"%(((itemCost - 2.70)*Tax)/100)))
                Total.set(str("$%.2f"%((itemCost - 2.70)+((itemCost-2.70)*Tax)/100)))


        def btnClick(numbers):
            global operator
            operator = operator+str(numbers)
            Cash_Input.set(operator)


    #=======================================TreeView=Text=Widget=====================
        scroll_y=Scrollbar(ReceiptFrame,orient=VERTICAL)
        self.POS_record=ttk.Treeview(ReceiptFrame,height=20,columns=("Item","Qty","Amount"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.POS_record.heading("Item",text="Item")
        self.POS_record.heading("Qty",text="Qty")
        self.POS_record.heading("Amount",text="Amount")

        self.POS_record["show"]="headings"

        self.POS_record.column("Item",width=120)
        self.POS_record.column("Qty",width=100)
        self.POS_record.column("Amount",width=100)

        self.POS_record.pack(fill=BOTH,expand=1)
        self.POS_record.bind("<ButtonRelease-1>")

        self.txtReceipt=Text(ReceiptFrame,width=79,height=1,font=("arial",5,"bold"))
        self.txtReceipt.pack()

        self.txtReceipt.insert(END,"Item\t\t\t\t Qty\t\t\t Amount\t\n")





    #    ========================Button Calculate=========================================================
        self.btn7=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="7",bd=8,command=lambda:btnClick(7),bg="Dark Red")
        self.btn7.grid(row=0,column=0)

        self.btn8=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="8",bd=8,command=lambda:btnClick(8),bg="Dark Red")
        self.btn8.grid(row=0,column=1)

        self.btn9=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="9",bd=8,command=lambda:btnClick(9),bg="Dark Red")
        self.btn9.grid(row=0,column=2)

    #    ========================Button Calculate=========================================================
        self.btn4=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="4",bd=8,command=lambda:btnClick(4),bg="Dark Red")
        self.btn4.grid(row=1,column=0)

        self.btn5=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="5",bd=8,command=lambda:btnClick(5),bg="Dark Red")
        self.btn5.grid(row=1,column=1)

        self.btn6=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="6",bd=8,command=lambda:btnClick(6),bg="Dark Red")
        self.btn6.grid(row=1,column=2)

    #    ========================Button Calculate=========================================================
        self.btn1=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="1",bd=8,command=lambda:btnClick(1),bg="Dark Red")
        self.btn1.grid(row=2,column=0)

        self.btn2=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="2",bd=8,command=lambda:btnClick(2),bg="Dark Red")
        self.btn2.grid(row=2,column=1)

        self.btn3=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="3",bd=8,command=lambda:btnClick(3),bg="Dark Red")
        self.btn3.grid(row=2,column=2)
    #    ========================Button Calculate=========================================================
        self.btn0=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="0",bd=8,command=lambda:btnClick(0),bg="Dark Red")
        self.btn0.grid(row=3,column=0)

        self.btnDot=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text=".",bd=8,command=lambda:btnClick("."),bg="Dark Red")
        self.btnDot.grid(row=3,column=1)

        self.btnC=Button(ChangeBtnFrame,padx=13,pady=22,font=("arial",20,"bold"),text="C",bd=8,bg="Dark Red",command=Change)
        self.btnC.grid(row=3,column=2)

    #    =======================Button Items of Cake==================================================
        self.btnCake1=Button(FoodItemFrame,padx=2,image=self.photoimg,width=104,height=104,bd=2,command=Cake_1)
        self.btnCake1.grid(row=0,column=0,padx=4,pady=2)

        self.btnCake2=Button(FoodItemFrame,padx=2,image=self.photoimg_1,width=104,height=104,bd=2,command=Cake_2)
        self.btnCake2.grid(row=0,column=1,padx=4,pady=2)

        self.btnCake3=Button(FoodItemFrame,padx=2,image=self.photoimg_2,width=104,height=104,bd=2,command=Cake_3)
        self.btnCake3.grid(row=0,column=2,padx=4,pady=2)

        self.btnCake4=Button(FoodItemFrame,padx=2,image=self.photoimg_3,width=104,height=104,bd=2,command=Cake_4)
        self.btnCake4.grid(row=0,column=3,padx=4,pady=2)

        self.btnCake5=Button(FoodItemFrame,padx=2,image=self.photoimg_4,width=104,height=104,bd=2,command=Cake_5)
        self.btnCake5.grid(row=0,column=4,padx=4,pady=2)

        self.btnCake6=Button(FoodItemFrame,padx=2,image=self.photoimg_5,width=104,height=104,bd=2,command=Cake_6)
        self.btnCake6.grid(row=0,column=5,padx=4,pady=2)
    #    =======================Button Items of Coffee==================================================
        self.btnCoffe1=Button(FoodItemFrame,padx=2,image=self.photoimg_6,width=104,height=104,bd=2,command=Coffee_1)
        self.btnCoffe1.grid(row=1,column=0,padx=4,pady=2)

        self.btnCoffe2=Button(FoodItemFrame,padx=2,image=self.photoimg_7,width=104,height=104,bd=2,command=Coffee_2)
        self.btnCoffe2.grid(row=1,column=1,padx=4,pady=2)

        self.btnCoffe3=Button(FoodItemFrame,padx=2,image=self.photoimg_8,width=104,height=104,bd=2,command=Coffee_3)
        self.btnCoffe3.grid(row=1,column=2,padx=4,pady=2)

        self.btnCoffe4=Button(FoodItemFrame,padx=2,image=self.photoimg_9,width=104,height=104,bd=2,command=Coffee_4)
        self.btnCoffe4.grid(row=1,column=3,padx=4,pady=2)

        self.btnCoffe5=Button(FoodItemFrame,padx=2,image=self.photoimg_10,width=104,height=104,bd=2,command=Coffee_5)
        self.btnCoffe5.grid(row=1,column=4,padx=4,pady=2)

        self.btnCoffe6=Button(FoodItemFrame,padx=2,image=self.photoimg_11,width=104,height=104,bd=2,command=Coffee_6)
        self.btnCoffe6.grid(row=1,column=5,padx=4,pady=2)
    #    =======================Button Items of Drinks==================================================
        self.btnDrink1=Button(FoodItemFrame,padx=2,image=self.photoimg_12,width=104,height=104,bd=2,command=Drink_1)
        self.btnDrink1.grid(row=2,column=0,padx=4,pady=2)

        self.btnDrink2=Button(FoodItemFrame,padx=2,image=self.photoimg_13,width=104,height=104,bd=2,command=Drink_2)
        self.btnDrink2.grid(row=2,column=1,padx=4,pady=2)

        self.btnDrink3=Button(FoodItemFrame,padx=2,image=self.photoimg_14,width=104,height=104,bd=2,command=Drink_3)
        self.btnDrink3.grid(row=2,column=2,padx=4,pady=2)

        self.btnDrink4=Button(FoodItemFrame,padx=2,image=self.photoimg_15,width=104,height=104,bd=2,command=Drink_4)
        self.btnDrink4.grid(row=2,column=3,padx=4,pady=2)

        self.btnDrink5=Button(FoodItemFrame,padx=2,image=self.photoimg_16,width=104,height=104,bd=2,command=Drink_5)
        self.btnDrink5.grid(row=2,column=4,padx=4,pady=2)

        self.btnDrink6=Button(FoodItemFrame,padx=2,image=self.photoimg_17,width=104,height=104,bd=2,command=Drink_6)
        self.btnDrink6.grid(row=2,column=5,padx=4,pady=2)
    #    =======================Button Items of Cake==================================================
        self.btnIce1=Button(FoodItemFrame,padx=2,image=self.photoimg_18,width=104,height=104,bd=2,command=IceCake_1)
        self.btnIce1.grid(row=3,column=0,padx=4,pady=2)

        self.btnIce2=Button(FoodItemFrame,padx=2,image=self.photoimg_19,width=104,height=104,bd=2,command=IceCake_2)
        self.btnIce2.grid(row=3,column=1,padx=4,pady=2)

        self.btnIce3=Button(FoodItemFrame,padx=2,image=self.photoimg_20,width=104,height=104,bd=2,command=IceCake_3)
        self.btnIce3.grid(row=3,column=2,padx=4,pady=2)

        self.btnIce4=Button(FoodItemFrame,padx=2,image=self.photoimg_21,width=104,height=104,bd=2,command=IceCake_4)
        self.btnIce4.grid(row=3,column=3,padx=4,pady=2)

        self.btnIce5=Button(FoodItemFrame,padx=2,image=self.photoimg_22,width=104,height=104,bd=2,command=IceCake_5)
        self.btnIce5.grid(row=3,column=4,padx=4,pady=2)

        self.btnIce6=Button(FoodItemFrame,padx=2,image=self.photoimg_23,width=104,height=104,bd=2,command=IceCake_6)
        self.btnIce6.grid(row=3,column=5,padx=4,pady=2)

        















        



        









if __name__ =='__main__':
    root = Tk()
    application = pos(root)
    root.mainloop()
