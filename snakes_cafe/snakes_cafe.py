
rest = [
    {
        "name": "Appetizers",
        "menu": [
            "Wings",
            "Cookies",
            "Spring Rolls",
                   ],
    },
    {
        "name": "Entrees",
        "menu": [
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden",
        ],
    },
    {
        "name":"Desserts",
        "menu":[
            "Ice Cream",
             "Cake",
             "Pie",
             ],
    },
    {
        "name": "Drinks",
        "menu": [
            "Coffee",
            "Tea",
            "Unicorn Tears",
                    ],
    },

    

]


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

    for item in range(len(rest)):
        print(rest[item]['name'])
        print('----------')
        for j in range(len(rest[item]['menu'])):
            print(rest[item]['menu'][j])
    print(get_order_question)


def get_order_customer():
    printmenu()
    order = input('> ')
    print(f'your order is : {order}')
    while order !='quit':
          order = input('> ')

   
        
get_order_customer()