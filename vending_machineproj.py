print("----- Welcome to the vending machine -----")

hd1 = {
  "item" : "Hot Chocolate", "item_price" : 4, "item_id" : "A1"
}
hd2 = { 
  "item" : "Green Tea", "item_price" : 3, "item_id" : "A2"
}
hd3 = {
  "item" : "Karak Tea", "item_price" : 2, "item_id" : "A3"
}
hd4 = {
  "item" : "Cappuccino", "item_price" : 5, "item_id" : "A4"
}


cd1 = { 
  "item" : "Iced Latte", "item_price" : 15, "item_id" : "B1"
}
cd2 = {
  "item" : "Caramel Macchiato", "item_price" : 17, "item_id" : "B2"
}
cd3 = {
  "item" : "Iced Tea", "item_price" : 13, "item_id" : "B3"
}
cd4 = {
  "item" : "Lime Soda", "item_price" : 9, "item_id" : "B4"
}


c1 = {
  "item" : "Lays Chilli Chips", "item_price" : 3, "item_id" : "C1",
}  
c2 = {
  "item" : "Takis", "item_price" : 6, "item_id" : "C2",
}
c3 = {
  "item" : "Oman Chips", "item_price" : 2, "item_id" : "C3",    
} 
c4 = {
  "item" : "BBQ Pringles", "item_price" : 5, "item_id" : "C4",   
}


ch1 = {
  "item" : "Galaxy Smooth", "item_price" : 3, "item_id" : "D1",
}
ch2 = {
  "item" : "Twix", "item_price" : 3, "item_id" : "D2",
} 
ch3 = {
  "item" : "Kitkat", "item_price" : 2, "item_id" : "D3",
}

hot_drinks = [hd1,hd2,hd3,hd4]
cold_drinks = [cd1,cd2,cd3,cd4]
chips = [c1,c2,c3,c4]
chocolate = [ch1,ch2,ch3]
vending = ["Hot drinks", "Cold drinks", "Chips", "Chocolate"]
vending_machine = [hot_drinks,cold_drinks,chips,chocolate]
coins = 10,20,30,40,50


def add_hdrink():
  hd = (input("Would you like to add another drink? Enter 'Y' or else 'N' : "))
  if (hd == 'Y'):
    print(hot_drinksfunc())
  else:
    print(vendyfunc())

def add_cdrink():
  cd = (input("Would you like to add another drink? Enter 'Y' or else 'N' : "))
  if (cd == 'Y'):
    print(cold_drinksfunc())
  else:
    print(vendyfunc())

def add_chips():
  cd = (input("Would you like to add another Chips? Enter 'Y' or else 'N' : "))
  if (cd == 'Y'):
    print(chips_func)
  else:
    print(vendyfunc())

def add_choco():
  choco = (input("Would you like to add another Chocolate? Enter 'Y' or else 'N' : "))
  if (choco == 'Y'):
    print(choco_func())
  else:
    print(vendyfunc())

currency = (str(input("This machine can only take in AED/Dirhams. Are you sure you want to continue. (yes/no): ")))



def vendyfunc():
  print(vending)
  v = str(input("Choose from the following category, 'N' to quit: "))
  if(v == 'Hot drinks'):
    print(hot_drinksfunc())
  elif( v == 'Cold drinks'):
    print(cold_drinksfunc())
  elif (v == 'Chips'):
    print(chips_func())
  elif(v == 'Chocolate'):
    print(choco_func())
  else:
    print(change_func())



def hot_drinksfunc():
 print("\n**********************************\n")
 for i in hot_drinks:
    print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
    print("--------------------------------------------\n")
 user_input = print("Enter the Item ID for your wanted product, or 'Finish' to quit: ")
 items_id = str(input())
 if (items_id == 'A1'):
    hot_choco = 4
    print(add_hdrink())
 elif (items_id == 'A2'):
   green_tea = 3
   print(add_hdrink())
 elif (items_id == 'A3'):
   karak = 2
   print(add_hdrink())
 elif (items_id == 'A4'):
   cappu = 5
   print(add_hdrink())
 elif (items_id == "Finish"):
   print(change_func())
 else:
  print("Please enter a valid response")
  print(hot_drinksfunc())

def cold_drinksfunc():
 for i in cold_drinks:
   print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
   print(print("--------------------------------------------\n"))
 print("Enter the Item ID for your wanted product: ")
 cditems_id = str(input())
 if (cditems_id == 'B1'):
    iced_latte = 15
    print(add_cdrink())
 elif (cditems_id == 'B2'):
    Caramel_Macchiato = 17
    print(add_cdrink())
 elif (cditems_id == 'B3'):
    Iced_Tea = 13
    print(add_cdrink())
 elif (cditems_id == 'B4'):
    Lime_Soda = 9
    print(add_cdrink())
 elif (cditems_id == "Finish"):
   print(change_func())
 else:
  print("Please enter a valid response")
  print(cold_drinksfunc())



def chips_func():
 for i in chips:
   print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
   print("--------------------------------------------\n")
 print("Enter the item ID for your wanted product: ")
 chitem_id = str(input())
 if (chitem_id == 'C1'):
   lays_chilli = 3
   print(add_choco())
 elif (chitem_id == 'C2'):
    takis = 6
    print(add_chips())
 elif (chitem_id == 'C3'):
    oman = 2
    print(add_chips())
 elif (chitem_id == 'C4'):
    bbq = 5
    print(add_chips())
 elif (chitem_id == "Finish"):
   print(change_func())
 else:
  print("Please enter a valid response")
  print(chips_func())


def choco_func():
 for i in chocolate:
   print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
   print("--------------------------------------------\n")
 print("Enter the item ID for your wanted product: ")
 citem_id = str(input())
 if (citem_id == 'D1'):
     galaxy_smooth = 3
     print(add_choco())
 elif (citem_id == 'D2'):
    twix = 3
    print(add_choco())
 elif (citem_id == 'D3'):
    kitkat = 2
    print(add_choco())
 elif (citem_id == "Finish"):
   print(change_func())
 else:
  print("Please enter a valid response")
  print(choco_func())



print("The maximum number of coins that can be inputted is 10-50.")
print("\n**********************************\n")

def stock():
    stock = hot_drinks, cold_drinks, chips, chocolate.values
    i = 0
    for amount in stock:
        i += amount
    print(i)




def change_func():
     coins = hd1["item_price"]
     coins = hd2["item_price"]
     coins = hd3["item_price"]
     coins = hd4["item_price"]
     coins = cd1["item_price"]
     coins = cd2["item_price"]
     coins = cd3["item_price"]
     coins = cd4["item_price"]
     coins = c1["item_price"]
     coins = c2["item_price"]
     coins = c3["item_price"]
     coins = c4["item_price"]
     coins = ch1["item_price"]
     coins = ch2["item_price"]
     coins = ch3["item_price"]

     total = 0
     while True:
        total += int(input("Insert money amount: ").strip())
        
        print(total)
        if total > coins:
            print("Here's your change =", total - coins)
            print("\n**********************************\n")
            print("Thank you for using our vending machine!")
            return
        elif total == coins:
            print("No Change Owed")
            return
        else:
            print("Amount Due =", coins-total)



if (currency == 'yes'):
  print("Choose from the following category you want.")
  print(vending)
print("Enter your selected category: ")
selection = str(input())
if (selection == 'Hot drinks'):
  print("\n**********************************\n")
  print(hot_drinksfunc())
  
elif (selection == 'Cold drinks'):
  print(cold_drinksfunc())
elif (selection == 'Chips'):
  print(chips_func())
elif (selection == 'Chocolate'):
  print(choco_func())
else:
  print("INVALID RESPONSE")


  