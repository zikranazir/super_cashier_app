# **Super Cashier 😃**

![alt](/src/Fearless.png)

    Disclaimer: 
    This repository is an individual project created for the Software and Data Engineering course at PACMANN.



## **How To Use**
---
### Running Application on Python Console:
1. Clone this repository into your local machine.
2. Open your favorite terminal and locate to **Super Cashier App** directory.
3. Download and create python virtual environtment. For example using `virtualenv .myenv` and activate using `source .myenv/bin/activate`.
4. Install the dependencies using `pip -r install requierements.txt`
5. Iniate the database using command `python init_db.py`
6. Running the **Super Cashier App** with command `python cashier.py`

### Running Applcation on Flask:
1. Follow similar steps 1-5 above.
2. On your terminal execute this command `flask run` to running application.
3. Open your browser and go to [127.0.0.1:5000](127.0.0.1:5000) or [localhost:5000](localhost:5000).


## **Objective**
---
Develop a self-service cashier application that enables users to add items to their shopping cart, update or delete items, remove transactions, view their shopping cart, and checkout by themselves. The application should provide a user-friendly interface that allows customers to easily navigate through the different options. Moreover, it should be able to handle multiple transactions simultaneously to ensure a seamless shopping experience for all users.


## **Flowchart**
---
![flowchart](src/flowchart.jpg)

## **Code Explainations**
### main.py
This script is the class  for the **super cashier app**. In this class there are consists of several method, such as:
 - add item
 - check item
 - update item (inc. update qty and update price_)
 - delete item
 - remove transaction
 - check carts
 - checkouts
 - create uuid
  
Here is the explaination for every method:

1. Importing Library
![alt](src/importlib.png)

2. Defines Class Transaction()
![initclass](src/initclass.png)
The above code defines a class called Transaction which contains a constructor method called init(). This constructor method initializes the class with two properties, items and total_price. The items property is defined as an empty list and total_price is set to zero. This class is designed to represent a transaction, and the constructor method initializes the transaction by creating an empty list for the items and setting the total price to zero.

3. Method add_item()
![alt](/src/additem.png)
The code above defines a method called 'add_item' within a class that is used to add an item to a transaction. This method takes a tuple consisting of the name, quantity, and price of the item to be added. The method then appends this tuple to the list of items in the transaction and calculates the total price by multiplying the quantity of the item with its price and adding it to the total price attribute of the transaction object. Finally, the method returns None as it doesn't have a return statement.
   
4. Method check_item()
![alt](/src/checkitem.png)
This is a method in a class that checks if a certain item exists in a transaction. The method takes an argument called 'item_name' which is a string representing the name of the item to be checked. 

5. Method update_item()
![alt](/src/updateitem.png)

6. Method update_qty()
![alt](/src/updateqty.png)

7. Method update_price()
![alt](/src/updateprice.png)

8. Method delete_item()
![alt](/src/deleteitem.png)

9. Method remove_transaction()
![alt](/src/carbon.png)

10. Method check_order()
![alt](/src/checkorder.png)

11. Method check_out()
![alt](/src/checkout.png)

12. Method crate_uuid()
![alt](/src/uuid.png)


### **db_init.py**
This purpose of this code to create a tables transactions and columns to storing transactions data from **Super Cashier App**. For this project will using sqlite for database server.

![alt](/src/dbinit.png)


### **super_cashier.py**
This script is driver script to running **Super Cashier App**, in this script instanced from Class transaction in main.py. 

![alt](/src/driver.png)


## Test Case

### Python Console/Terminal

1. Running Aplication with command `python super_cashier.py`
![alt](/src/1.png)

2. Add Shopping Item
![alt](/src/2.png)

3. Update Shopping Item Qty
![alt](/src/3.png)

4. Delete Shopping Item
![alt](/src/4.png)

5. Check Shopping Cart
![alt](/src/5.png)

6. Checkout Transaction
![alt](/src/6.png)

7. Exit Application
![alt](/src/7.png)


### Flask App

1. Running the flask app using this command `flask run`
   ![alt](/src/a.png)

2. Open browser and go to [127.0.0.1:5000](127.0.0.1:5000), you will see the interface of Super Cashier App. You can add shopping items by fill the "Tambah Item" form and hit "Tambah Item" Button to submit the order.
    ![alt](/src/b.png)

3. Check shopping chart or order items below the form. 
    ![alt](/src/c.png)

4. You can update/edit the item by hit "Edit" button.
   ![alt](/src/d.png)

   After update item:
   ![alt](/src/e.png)

5. You also can delete the item by hit "Delete" button and befor the item deleted, the system will ask delete confirmation.

    ![alt](/src/f.png)

6. Checkout the transaction by click "Checkout" button.
   ![alt](/src/g.png)
