#-----------------SUPERMARKET SYSTEM--------------------
#-----------------PREPARED BY RAVISANKAR S--------------
#-----------------CUCEK, CSE, FIRST YEAR----------------
#-----------------PYTHON BOOTCAMP PROJECT---------------
items = []
while True:
    display = input('Press enter to continue.')
    print('--------------------Welcome to TinkerZ Supermarket--------------------')
    print('1. Add items to list\n2. Delete items\n3. View items\n4. Exit')
    choice = input('Enter the number of your choice : ')

    
    if choice == '1' :
        print('--------------------Add items--------------------')
        print('To add an item fill in the form')
       
        item = {}
        item['name'] = input('Item name : ')
        while True:
            try:
                item['quantity'] = int(input('Item quantity : '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        while True:
            try:
                item['price'] = int(input('Price ₹ : '))
                break
            except ValueError:
                print('Price should only be in digits')
        print('Item has been successfully added.')
        items.append(item)

    

    elif choice == '2' :
        print('--------------------Delete items--------------------')
        item_name = input('Enter the name of the item that you want to delete : ')
        for item in items:
            if item_name.lower() == item['name'].lower():
        
                print('Item has been successfully deleted.')
                items.remove(item)
   
    elif choice == '3' :
        print('--------------------View Items--------------------')
        print('The number of items in the inventory are : ',len(items))
        while len(items) != 0:
            print('Here are all the items available in the supermarket.')
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)
            break
                
    elif choice == '4' :
        print('---------------------Thank You. Visit Again---------------------')
        break

    else: 
         print('You entered an invalid option')


#  ------------------Prepared for TinkerHub CUCEK---------------------------