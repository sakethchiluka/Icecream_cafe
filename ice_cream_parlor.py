import sqlite3
import sys

def init_db():
    try:
        conn = sqlite3.connect('ice_cream_parlor.db')
        cursor = conn.cursor()
        cursor.executescript("""
            DROP TABLE IF EXISTS seasonal_flavors;
            DROP TABLE IF EXISTS ingredients;
            DROP TABLE IF EXISTS customer_suggestions;
            DROP TABLE IF EXISTS cart;
        """)
        
        with open('schema.sql') as f:
            cursor.executescript(f.read())
        with open('sample_data.sql') as f:
            cursor.executescript(f.read())
        
        conn.commit()
        return conn
    except Exception as e:
        print(f"Error initializing database: {e}")
        sys.exit(1)

def display_seasonal_flavors(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description FROM seasonal_flavors")
        flavors = cursor.fetchall()
        if not flavors:
            print("No seasonal flavors available.")
        else:
            for flavor in flavors:
                print(f"{flavor[0]}. {flavor[1]}: {flavor[2]}")
    except Exception as e:
        print(f"Error displaying seasonal flavors: {e}")

def search_flavors(conn, search_term):
    try:
        cursor = conn.cursor()
        query = "SELECT id, name, description FROM seasonal_flavors WHERE name LIKE ? OR description LIKE ?"
        cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
        flavors = cursor.fetchall()
        if not flavors:
            print("No matching flavors found.")
        else:
            for flavor in flavors:
                print(f"{flavor[0]}. {flavor[1]}: {flavor[2]}")
    except Exception as e:
        print(f"Error searching flavors: {e}")

def filter_by_ingredient(conn, ingredient):
    try:
        cursor = conn.cursor()
        query = "SELECT id, name, description FROM seasonal_flavors WHERE ingredients LIKE ?"
        cursor.execute(query, (f'%{ingredient}%',))
        flavors = cursor.fetchall()
        if not flavors:
            print(f"No flavors containing {ingredient} found.")
        else:
            for flavor in flavors:
                print(f"{flavor[0]}. {flavor[1]}: {flavor[2]}")
    except Exception as e:
        print(f"Error filtering flavors by ingredient: {e}")

def add_allergen(conn, ingredient_name):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM ingredients WHERE name = ?", (ingredient_name,))
        ingredient_id = cursor.fetchone()
        if ingredient_id:
            cursor.execute("UPDATE ingredients SET allergen = 1 WHERE name = ?", (ingredient_name,))
            print(f"{ingredient_name} is now marked as an allergen.")
            conn.commit()
        else:
            print(f"{ingredient_name} not found in ingredients list.")
    except Exception as e:
        print(f"Error adding allergen: {e}")

def display_cart(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT sf.id, sf.name, sf.description FROM cart c INNER JOIN seasonal_flavors sf ON c.flavor_id = sf.id")
        cart_items = cursor.fetchall()
        if not cart_items:
            print("Your cart is empty.")
        else:
            print("Your cart:")
            for item in cart_items:
                print(f"{item[0]}. {item[1]}: {item[2]}")
    except Exception as e:
        print(f"Error displaying cart: {e}")

def add_to_cart(conn, flavor_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM seasonal_flavors WHERE id = ?", (flavor_id,))
        flavor = cursor.fetchone()
        if flavor:

            cursor.execute("INSERT INTO cart (flavor_id) VALUES (?)", (flavor_id,))
            print("Flavor added to cart successfully.")
            conn.commit()
        else:
            print("Invalid flavor ID. Flavor does not exist.")
    except Exception as e:
        print(f"Error adding flavor to cart: {e}")

def main():
    conn = init_db()
    print("Welcome to the Ice Cream Parlor Cafe!")
    while True:
        try:
            print("\n1. View Seasonal Flavors")
            print("2. Search Flavors")
            print("3. Filter by Ingredient")
            print("4. Add Allergen")
            print("5. show Cart")
            print("6. Add Flavor to Cart")
            print("7. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                display_seasonal_flavors(conn)
            elif choice == '2':
                search_term = input("Enter search term: ")
                search_flavors(conn, search_term)
            elif choice == '3':
                ingredient = input("Enter an ingredient to filter by: ")
                filter_by_ingredient(conn, ingredient)
            elif choice == '4':
                ingredient_name = input("Enter the name of the allergen ingredient: ")
                add_allergen(conn, ingredient_name)
            elif choice == '5':
                display_cart(conn)
            elif choice == '6':
                flavor_id = input("Enter the flavor ID to add to cart: ")
                if flavor_id.isdigit():
                    add_to_cart(conn, int(flavor_id))
                else:
                    print("Invalid flavor ID. Please enter a numeric value.")
            elif choice == '7':
                print("Exiting the application. Thank You!")
                break
            else:
                print("Invalid option, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Terminating the application due to an error.")
            break

if __name__ == '__main__':
    main()
