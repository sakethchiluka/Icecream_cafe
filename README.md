# Icecream_cafe
## Description
This application is made to handle the inventories of ingredients, seasonal flavor selections, client flavor recommendations, and allergy issues for a fictional ice cream shop. Users can add allergies if they don't already exist, search and filter the selections, and keep track of their preferred products in a basket
Features
    view seasonal flavor offerings.
    Search and filter the flavors.
    Add allergens to ingredients.
    Maintain a shopping cart of favorite flavors.
## Setup
Python 3.x
SQLite3

1.Create the Database Schema
Ensure you have the schema.sql and sample_data.sql files in the same directory as app.py.
-- seasonal_flavors table
CREATE TABLE IF NOT EXISTS seasonal_flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    ingredients TEXT
);

-- ingredients table
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    allergen BOOLEAN DEFAULT 0
);

-- customer_suggestions table
CREATE TABLE IF NOT EXISTS customer_suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    suggested_flavor TEXT NOT NULL,
    allergens TEXT
);

-- cart table
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_id INTEGER,
    FOREIGN KEY (flavor_id) REFERENCES seasonal_flavors (id)
);
3.sample_data.sql
INSERT INTO seasonal_flavors (name, description, ingredients) VALUES
('Mango Tango', 'A delightful mango-flavored ice cream', 'mango, cream, sugar'),
('Berry Blast', 'Mixed berries with a hint of vanilla', 'strawberry, blueberry, vanilla, cream, sugar'),
('Chocolate Heaven', 'Rich and creamy chocolate ice cream', 'chocolate, cream, sugar'),
('Vanilla Dream', 'Classic vanilla ice cream', 'vanilla, cream, sugar'),
('Peach Perfection', 'Sweet and tangy peach ice cream', 'peach, cream, sugar'),
('Mint Chocolate Chip', 'Refreshing mint with chocolate chips', 'mint, chocolate chips, cream, sugar'),
('Pistachio Delight', 'Nutty pistachio ice cream', 'pistachio, cream, sugar'),
('Caramel Swirl', 'Creamy caramel with a swirl of caramel sauce', 'caramel, cream, sugar, caramel sauce'),
('Coconut Paradise', 'Tropical coconut ice cream', 'coconut, cream, sugar'),
('Raspberry Ripple', 'Raspberry ice cream with a raspberry ripple', 'raspberry, cream, sugar');
4.Run the Application
In the google colab open new notebook upload the python file in it and also upload database an sample database and schema
and run the application 
## Usage
1.Welcome Screen
On running the application, you will be greeted with a welcome message and a menu of options:
Welcome to the Ice Cream Parlor Cafe!

1. Display Seasonal Offers
2. Search Offers
3. Filter by Stock Item
4. Mark Allergen
5. Display Cart
6. Add Offer to Cart
7. Exit
Choose an Option
Enter the corresponding number to select an option from the menu. For example, to display seasonal offers, enter 1.
Perform Actions
Follow the prompts to search for offers, filter by ingredients, mark allergens, display the cart, or add offers to the cart.
Exit
![image](https://github.com/sakethchiluka/Icecream_cafe/assets/79203064/6bf3a17a-7ec8-47e7-a5ba-638793891ad6)
![image](https://github.com/sakethchiluka/Icecream_cafe/assets/79203064/b7cbcd07-2129-43b3-8b2d-01915b222cb9)
![image](https://github.com/sakethchiluka/Icecream_cafe/assets/79203064/5120a98b-4aee-468f-96d7-91fdc94d3fa5)






