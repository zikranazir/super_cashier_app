import sqlite3

# Connect to database
conn = sqlite3.connect('transaction.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             id_transaksi TEXT NOT NULL,
             nama_item TEXT NOT NULL, 
             jumlah_item INTEGER NOT NULL,
             harga INTEGER NOT NULL,
             total_harga INTEGER NOT NULL,
             diskon INTEGER,
             harga_diskon INTEGER,
             created_at DATETIME);''')

print('success crated')

# Commit changes and close connection
conn.commit()
conn.close()
