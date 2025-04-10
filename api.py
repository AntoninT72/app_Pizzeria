# api.py

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',  # modifie ici si besoin
    'host': 'localhost',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'pizzeria',
    'raise_on_warnings': True
}

def get_connection():
    return mysql.connector.connect(**config)

def get_all_products():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pizzas")
    results = cursor.fetchall()
    cnx.close()
    return results

def add_product(nom, prix):
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO pizzas (nom, prix) VALUES (%s, %s)", (nom, prix))
    cnx.commit()
    cnx.close()

def delete_product(product_id):
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM pizzas WHERE id = %s", (product_id,))
    cnx.commit()
    cnx.close()
