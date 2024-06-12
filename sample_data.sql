-- Insert sample data into seasonal_flavors
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

-- Insert sample data into ingredients
INSERT INTO ingredients (name, allergen) VALUES
('mango', 0),
('cream', 1),
('sugar', 0),
('strawberry', 0),
('blueberry', 0),
('vanilla', 0),
('chocolate', 0),
('peach', 0),
('mint', 0),
('chocolate chips', 1),
('pistachio', 1),
('caramel', 0),
('caramel sauce', 0),
('coconut', 0),
('raspberry', 0);

-- Insert sample data into customer_suggestions
INSERT INTO customer_suggestions (name, suggested_flavor, allergens) VALUES
('Alice', 'Chocolate Fudge', 'chocolate'),
('Bob', 'Lemon Sorbet', 'lemon'),
('Carol', 'Salted Caramel', 'caramel'),
('Dave', 'Green Tea', 'green tea'),
('Eve', 'Banana Split', 'banana'),
('Frank', 'Hazelnut Crunch', 'hazelnut'),
('Grace', 'Blackberry Sorbet', 'blackberry'),
('Hank', 'Coffee Delight', 'coffee'),
('Ivy', 'Pumpkin Spice', 'pumpkin'),
('Jack', 'Maple Walnut', 'walnut');

-- Insert sample data into cart (empty for now)
