
restMenu = {
    
         "Appetizers": [ "Wings", "Cookies", "Spring Rolls"],
    
         "Entrees": ["Salmon","Steak", "Meat Tornado", "A Literal Garden"], 
    
        "Desserts":["Ice Cream","Cake", "Pie" ],
    
         "Drinks": ["Coffee","Tea", "Unicorn Tears"], 
}

customer_orders = []

allItems = []

for item in restMenu.values():
    allItems +=item


welcome_msg = """ 
   
***************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""

get_order_question = """ 
***********************************
** What would you like to order? **
***********************************
"""
def printmenu():

    print(welcome_msg)

    for item in restMenu.keys():
        print(item)
        print('----------')
        for j in restMenu[item]:
            print(j)
        


def get_order_customer():
    printmenu()
    print(get_order_question)
    order = ''
    # order = input('> ')
    # print(f'your order is : {order}')
    while order !='quit':
          order = input('> ').capitalize() # capitalize the first character and remain the rest
          if order in allItems:
             customer_orders.append(order)
             # list.count(value)
             # ** 1 order of Wings have been added to your meal **
             count_order = customer_orders.count(order)
             print(f"** {count_order} order of {order} have been added to your meal ** ")
          elif order =='Quit':
              print("Exit of the program...")
              break
          else:
              print("Sorry! order is not in our menu")

def print_order_customer( customer_orders ):
    start = """
    ***********************************
    ** you are welcome! your order is **
    ***********************************
    """
    end = """
    ***********************************
    ************ Thanks ***************
    ***********************************
    """

    print(start)
    for item in customer_orders:
           print(f"     {customer_orders.count(item)} order of {item}")
    print(end)
   
if __name__ == "__main__":
    
 get_order_customer()
 print_order_customer(customer_orders)