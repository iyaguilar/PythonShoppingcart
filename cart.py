# shoppingcart_module.py



def show_cart(cart):
    print("\nyour shopping cart:")
    for item, quantity in cart.items():
        print(f"{item}: {quantity}")

def add_item(cart, item, quantity):
    item= input("Enter your item to add:")
    quantity: int(input("Enter the quantity:"))
    if item in cart: 
        cart[item] +=quantity
    else: 
        cart[item] = quantity

    print(f"{quantity} {item}(s) added to your cart.")



def remove_item(cart, item, quantity_to_remove):
    if item in cart:
        if quantity_to_remove >= cart[item]:
            del cart[item]
        else:
             cart[item] -= quantity_to_remove
             print(f"{quantity_to_remove} {item}(s) removed from your cart.") 
            
    print(f"{item} is not in your cart.")     


def shopping_cart():
     cart = {}
     while True:
          print("\nOptions:")
          print("1. Show Cart")
          print("2. Add Item")
          print("3. Remove item")
          print("4. Quit")

choice= input("Enter your choice (1-4): ")
if choice =="1":
            show_cart(cart)
elif choice == "2":          
            add_item (cart)
elif choice =="3":
            remove_item(cart)
elif choice =="4":
            print("Thank you for shopping with Us!")
            show_cart(cart)

else:

        print("Invalid choice. Please enter a number between 1 and 4.")
        
import cart    
my_cart = {}
cart.add_item(my_cart, "ProductA", 2)
cart.add_item(my_cart, "ProductB", 1)
cart.show_cart(my_cart)


              