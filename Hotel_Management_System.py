# Project on Hotel Reservation System - Python-MySQL connectivity

import mysql.connector as my


# Function for adding customer's informations

def add():
    
     mydb=my.connect(host="localhost", user="root", passwd="", database="dbproject")
     mycur=mydb.cursor()
     ch='y'
     while ch == 'y' or ch == 'Y':
        cust_id = int(input("\nEnter the customer id: "))
        cust_name = input("Enter the customer name: ")
        address = input("Enter the address: ")
        roomno = int(input("Enter the room no.: "))
        mobileno = int(input("Enter the mobile no.: "))
        check_in = input("Enter the check in date (YYYY-MM-DD): ")
        check_out = input("Enter the check out date (YYYY-MM-DD): ")
        adv_payment = float (input("Enter the advance amount: "))
        room_type = int(input("Room Type:-\n 1: Suit (Rs. 1500/day) \n 2: Delux (Rs. 1000/day) \n 3: Standard (Rs. 500/day) \n \n Enter your choice: "))

        if room_type == 1 :
            room_type= "Suite"
        elif room_type == 2 :
            room_type= "Delux"
        elif room_type == 3 :
            room_type= "Standard"
        

        str="INSERT INTO HOTEL VALUES ({}, '{}', '{}', {}, {}, '{}', '{}', {}, '{}')"
    
        query= (str.format(cust_id, cust_name, address, roomno, mobileno, check_in, check_out, adv_payment, room_type))

        mycur.execute(query)
        mydb.commit()

        print("\n\nCustomer record successfully inserted.\n\n")
        ch=input("Want to add more records (y/n): ")
    
# Function for searching customer's data

def search():
     
     mydb=my.connect(host="localhost", user="root", passwd="", database="dbproject")
     mycur= mydb.cursor()
     cno=int(input("Enter the customer id: "))
     str="SELECT * FROM HOTEL WHERE cust_id = {}"
     query=str.format(cno)
     print("=========================================")
     
     mycur.execute(query)
     myrec=mycur.fetchall()
     for x in myrec:
         cust_id = x[0]
         cust_name = x[1]
         address = x[2]
         roomno = x[3]
         mobileno = x[4]
         check_in = x[5]
         check_out = x[6]
         adv_payment = x[7]
         room_type = x[8]

         print("",cust_id,'\n',cust_name,'\n',address,'\n',roomno,'\n',mobileno,'\n',check_in,'\n',check_out,'\n',adv_payment,'\n',room_type)
     
# Function to display all data

def display():

     mydb=my.connect(host="localhost", user="root", passwd="", database="dbproject")
     mycur= mydb.cursor()
     mycur.execute("SELECT * FROM Hotel")

     print("=========================================")
    
     myrec=mycur.fetchall() 
     for x in myrec:
         
         cust_id = x[0]
         cust_name = x[1]
         address = x[2]
         roomno = x[3]
         mobileno = x[4]
         check_in = x[5]
         check_out = x[6]
         adv_payment = x[7]
         room_type = x[8]
         print("",cust_id,'\n',cust_name,'\n',address,'\n',roomno,'\n',mobileno,'\n',check_in,'\n',check_out,'\n',adv_payment,'\n',room_type)
         print("---------------------------")

# Function to edit data already updated

def edit():

     mydb=my.connect(host="localhost", user="root", passwd="", database="dbproject")
     mycur= mydb.cursor()
     mycur.execute("SELECT * FROM Hotel")

     print("=========================================")

     print ("Before Updation:-")
     myrec=mycur.fetchall()
     for x in myrec:
         cust_id = x[0]
         cust_name = x[1]
         address = x[2]
         roomno = x[3]
         mobileno = x[4]
         check_in = x[5]
         check_out = x[6]
         adv_payment = x[7]
         room_type = x[8]

         print("",cust_id,'\n',cust_name,'\n',address,'\n',roomno,'\n',mobileno,'\n',check_in,'\n',check_out,'\n',adv_payment,'\n',room_type)
         print("---------------------------")

     cust_id = int(input("Enter the customer id whose record is to be Updated: "))
     print("\nEnter the new data\n")
     cust_name = input("Enter the customer name: ")
     address = input("Enter the address: ")
     roomno = int(input("Enter the Room no.: "))
     mobileno = int(input("Enter the mobile no.: "))
     check_in = input("Enter the check in date (YYYY-MM-DD): ")
     check_out = input("Enter the check out date (YYYY-MM-DD): ")
     adv_payment = float (input("Enter the advance amount: "))
     room_type = int(input("Room Type:-\n 1: Suit (Rs. 1500/day) \n 2: Delux (Rs. 1000/day) \n 3: Standard (Rs. 500/day) \n \n Enter your choice: "))

     if room_type == 1 :
         room_type= "Suite"
     elif room_type == 2 :
         room_type= "Delux"
     elif room_type == 3 :
         room_type= "Standard"

     mycur=mydb.cursor()
     
     str="UPDATE HOTEL SET cust_name='{}',address='{}',roomno={},mobileno={},check_in='{}',check_out='{}',adv_payment={},room_type='{}' WHERE cust_id={}"
     query= str.format(cust_name, address, roomno, mobileno, check_in, check_out, adv_payment, room_type,cust_id)

     mycur.execute(query)
     mydb.commit()
     
     mycur.execute("SELECT * FROM Hotel")

     print("=========================================")

     print ("After Updation:-")
     myrec=mycur.fetchall()
     for x in myrec:
         cust_id = x[0]
         cust_name = x[1]
         address = x[2]
         roomno = x[3]
         mobileno = x[4]
         check_in = x[5]
         check_out = x[6]
         adv_payment = x[7]
         room_type = x[8]

         print("",cust_id,'\n',cust_name,'\n',address,'\n',roomno,'\n',mobileno,'\n',check_in,'\n',check_out,'\n',adv_payment,'\n',room_type)
         print("---------------------------")

# Function to delete the record of a customer

def delete():

     mydb=my.connect(host="localhost", user="root", passwd="", database="dbproject")
     mycur= mydb.cursor()
     mycur.execute("SELECT * FROM Hotel")

     print("=========================================")

     print ("Before Deletion:-")
     myrec=mycur.fetchall()
     for x in myrec:
         cust_id = x[0]
         cust_name = x[1]
         address = x[2]
         roomno = x[3]
         mobileno = x[4]
         check_in = x[5]
         check_out = x[6]
         adv_payment = x[7]
         room_type = x[8]
         print("",cust_id,'\n',cust_name,'\n',address,'\n',roomno,'\n',mobileno,'\n',check_in,'\n',check_out,'\n',adv_payment,'\n',room_type)
         print("---------------------------")
     
     cust_id = int(input("Enter the customer id whose record is to be deleted: "))
     str="DELETE FROM HOTEL WHERE cust_id={}"
     query= str.format(cust_id)
     mycur.execute(query)
     mydb.commit()
     
     print("\nRecord successfully Deleted.")

# Function to generate report of a customer

def generate():
     
     Tax = 0

     mydb=my.connect(host="localhost", user="root", passwd="", database="dbproject")
     mycur= mydb.cursor()
     cust_id = int(input("Enter the customer id: "))

     str="SELECT cust_id,cust_name,address,roomno,mobileno,check_in,check_out,adv_payment,room_type, dayofyear(check_out) - dayofyear(check_in) FROM HOTEL WHERE cust_id={} "
     query = str.format(cust_id)
     print("=========================================")
     mycur.execute(query)
     myrec=mycur.fetchall()
     for x in myrec:
         cust_id = x[0]
         cust_name = x[1]
         address = x[2]
         roomno = x[3]
         mobileno = x[4]
         check_in = x[5]
         check_out = x[6]
         adv_payment = x[7]
         room_type = x[8]
         days = x[9]

     print("=========================================")
     print(" Hotel The Shivneri,")
     print(" 5/10, Street 76,")
     print(" Indore ( M.P.)")
     print("=========================================")
     print(" Customer ID No.: ",cust_id)
     print(" Customer Name: ",cust_name)
     print(" Customer Address: ",address)
     print("=========================================")
     print(" Room No.",roomno)
     print(" Mobile No.",mobileno)
     print("=========================================")
     print(" Check In Date: ",check_in)
     print(" Check Out Date: ",check_out)
     print(" Room Type: ",room_type)
     print("=========================================")
     print(" No. of days stayed: ", days)
     if room_type == "Suite" :
        price = 1500
     elif room_type == "Delux" :
        price = 1000
     elif room_type == "Standard" :
        price = 500

     total = days * price
     print(" Total: ",total)
     print(" Advance: ", adv_payment)
     Tax = total*0.10
     print(" Tax: ",Tax)
     net = (float(total)+float(Tax))-float(adv_payment)
     netamt = float(total)+float(Tax)
     print(" Net Amount: ",netamt)
     print(" Total Balance Payable by Customer",net)
    

# main

ch = 'y'

while ch =='y' or ch =='Y' :
     print("=========================================")
     print("MENU")
     print("1. To add new record")
     print("2. To search a record")
     print("3. To update the record")
     print("4. To delete a record")
     print("5. To view all record")
     print("6. To generate the report")
     print("7. For exit ")
     print("=========================================")
     ch=int(input("Enter your choice: "))
     
     if ch == 1 :
         add()
     elif ch == 2:
         search()
     elif ch == 3:
         edit()
     elif ch == 4:
         delete()
     elif ch == 5:
         display()
     elif ch == 6:
         generate()
     elif ch == 7:
         break
     

     print("=========================================")
     print("")
     ch = input("Want to display Main Menu (y/n): ")

    
