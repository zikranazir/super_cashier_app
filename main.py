from prettytable import PrettyTable
from datetime import datetime
import sqlite3
import uuid


class Transaction:
    def __init__(self):
        """
        Constructor method for the Transaction class.

        Initializes an empty list for items and sets total_price to zero.
        """
        self.items = []  # definisi properti items sebagai list kosong
        self.total_price = 0
        

    def add_item(self, item):
        """
        Method to add an item to the transaction.

        Args:
            item: A tuple consisting of (name, quantity, price) of the item to be added.

        Returns:
            None
        """
        self.items.append(item)
        self.total_price += item[1] * item[2]


    def check_item(self, item_name):
        """
        Method to check if an item with a certain name is in the transaction.

        Args:
            item_name: A string representing the name of the item to be checked.

        Returns:
            True if the item exists in the transaction, raises ValueError with an error message otherwise.
        """
        try:
            for i, item in enumerate(self.items):
                if item[0] == item_name:
                    return True
            raise ValueError("Item tidak ada, periksa kembali nama item")
        except ValueError as e:
            print(e)



    def update_item(self,  item_name, qty, price):
        """
        Method to update an item in the transaction.

        Args:
            item_name: A string representing the name of the item to be updated.
            qty: An integer representing the new quantity of the item.
            price: A float representing the new price of the item.

        Returns:
            None
        """
        for i, old_item in enumerate(self.items):
            if old_item[0] != item_name or old_item[1] != qty or old_item[2] != price:
                self.total_price -= old_item[1] * old_item[2]
                self.items[i] = [item_name, qty, price]
                self.total_price += qty * price
                break    
            else:
                print("Tidak ada perubahan")

    def update_item_qty(self, name, qty):
        """
        Method to update the quantity of an item in the transaction.

        Args:
            name: A string representing the name of the item to be updated.
            qty: An integer representing the new quantity of the item.

        Returns:
            None
        """
        for item in self.items:
            if item[0] == name:
                item[1] = qty
                self.total_price = sum(map(lambda x: x[1]*x[2], self.items))
                break

    def update_item_price(self, name, price):
        """
        Method to update the price of an item in the transaction.

        Args:
            name: A string representing the name of the item to be updated.
            price: A float representing the new price of the item.

        Returns:
            None
        """

        for item in self.items:
            if item[0] == name:
                item[2] = price
                self.total_price = sum(map(lambda x: x[1]*x[2], self.items))
                break

    def delete_item(self, name):
        """
        Method to delete an item from the transaction.

        Args:
            name: A string representing the name of the item to be deleted.

        Returns:
            None
        """
        for item in self.items:
            if item[0] == name:
                self.total_price -= item[1] * item[2]
                self.items.remove(item)
                break

    def remove_transaction(self):
        items = self.items
        items.clear()
        print("Semua Transaksi berhasil dihapus")

    def check_order(self):
        """
        This method checks the order data in the instance and returns a table, item data list, and total price in formatted string.

        Returns:
        table (PrettyTable): A table with columns 'No', 'Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga'.
        item_data (list): A list of lists with data of each item in the order.
        formated_total_harga (str): The total price of the order in formatted string.

        Raises:
        ValueError: If there is an error in the input data such as empty item name, non-positive quantity or non-positive price.
        """
        for item in self.items:
            if item[0] == "" or item[1] <= 0 or item[2] <= 0:
                raise ValueError("Terdapat kesalahan input data")
            
        item_data = []
        total_harga = self.total_price
        formated_total_harga = "Rp. {:,.0f},-".format(total_harga).replace(",", ".")
        table = PrettyTable()
        table.field_names = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        for i, item in enumerate(self.items):
            data = [i+1, item[0], item[1], item[2], item[1]*item[2]]
            item_data.append(data)
            table.add_row(data)

        return table, item_data, formated_total_harga

        

    def check_out(self):
        """
        Calculates the total price of all items in the shopping cart and applies the applicable discount based on the total price.
        Prints the formatted order details, including any applicable discount, and saves the transaction data to a SQLite database.
        Returns a tuple containing the formatted item data, formatted total price, and, if applicable, the total price after discount and the discount percentage.

        Returns:
            If discount is applicable:
            Tuple[str, str, int, float]: A tuple containing formatted item data, formatted total price, total price after discount and discount percentage.
            If discount is not applicable:
            Tuple[str, str]: A tuple containing formatted item data and formatted total price.

        Raises:
            No exceptions are raised.
        """
        if self.total_price >= 500000:
            diskon = 0.07
        elif self.total_price >= 300000:
            diskon = 0.06
        elif self.total_price >= 200000:
            diskon = 0.05
        else:
            diskon = 0

        
        table, item_data, formated_total_harga = self.check_order()
        print(table)
        persen_diskon = diskon * 100
        total_harga_setelah_diskon = round(self.total_price * (1 - diskon))
        
        if diskon > 0:
            print(formated_total_harga)
            print("Diskon {}%: Rp {:,.0f},-".format(round(persen_diskon), round(self.total_price*diskon)))
            print("Total Harga Setelah Diskon: Rp. {:,.0f},-".format(total_harga_setelah_diskon).replace(",", "."))
        else:
            print(formated_total_harga)


        #Save Transaksi To Database
        id_transaksi = self.create_uuid()

        transaction_data = []
        for item in self.items:
            nama_item = item[0]
            jumlah_item = item[1]
            harga = item[2]
            total_harga = jumlah_item * harga
            diskon_harga = round(total_harga * diskon / 100)
            harga_diskon = round(total_harga - diskon_harga)
            created_at = datetime.utcnow()
            transaction_data.append((id_transaksi, nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon, created_at))

        # Open connection to database
        conn = sqlite3.connect('transaction.db')
        cursor = conn.cursor()

        # Insert transaction data to database
        cursor.executemany("INSERT INTO transactions (id_transaksi, nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ? )", transaction_data)

        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()

        if diskon > 0:
            return item_data, formated_total_harga, total_harga_setelah_diskon, persen_diskon
        else:
            return item_data, formated_total_harga

    def create_uuid(self):
        '''
        This method generates a unique identifier for a transaction using the uuid library. The generated UUID is then truncated to the first 8 characters to create a shorter ID.

        The method takes no arguments and returns a string representing the short UUID.
        '''
        id_transaksi = str(uuid.uuid1())
        short = id_transaksi[:8]
        return short
