#asks quantity of food items for order then delievers the total bill amount
print("Welcome to ESCOBAR");
print("Menu ");
print("Prices(in INR) \n 1. Burger-50 \n 2. Veg Pizza-100 \n 3.Paneer Piza-110\n 4.Chowmein-85 \n 5. Cold coffe-70 \n 6. Dosa- 80");
print("Enter your order quantity for each item: ");
burger = int(input("Burger:"));
veg=int(input("Veg Pizza:"));
paneer=int(input("Paneer Pizza:"));
chowmein=int(input("chowmein:"));
cold=int(input("Cold Coffee:"));
dosa=int(input("Dosa:"));
print("your total bill is: ", burger*50 + veg*100 +paneer*110 + chowmein*85 +cold*70 + dosa*80);
print( "Thanks for visiting us!");
