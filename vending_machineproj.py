print("\n                 ** ----- Welcome to the vending machine ----- **\n") #Welcome message

#Items dictionaries
hd1 = {
  "item" : "Hot Chocolate", "item_price" : 4, "item_id" : "A1", 
}
hd2 = { 
  "item" : "Green Tea", "item_price" : 3, "item_id" : "A2",
}
hd3 = {
  "item" : "Karak Tea", "item_price" : 2, "item_id" : "A3",
}
hd4 = {
  "item" : "Cappuccino", "item_price" : 5, "item_id" : "A4", 
}


cd1 = { 
  "item" : "Iced Latte", "item_price" : 15, "item_id" : "B1",
}
cd2 = {
  "item" : "Caramel Macchiato", "item_price" : 17, "item_id" : "B2",
}
cd3 = {
  "item" : "Iced Tea", "item_price" : 13, "item_id" : "B3",
}
cd4 = {
  "item" : "Lime Soda", "item_price" : 9, "item_id" : "B4",
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
  "item" : "Twix", "item_price" : 5, "item_id" : "D2",
} 
ch3 = {
  "item" : "Kitkat", "item_price" : 2, "item_id" : "D3",
}

#Variables
hot_drinks = [hd1,hd2,hd3,hd4]
cold_drinks = [cd1,cd2,cd3,cd4]
chips = [c1,c2,c3,c4]
chocolate = [ch1,ch2,ch3]
vending = ["Hot drinks", "Cold drinks", "Chips", "Chocolate"]
currency = (str(input("This machine can only take in AED/Dirhams. Are you sure you want to continue. (yes/no): ")))
item_list = []
total=0
m=1
dispensed=[]

#Using Function for the change feature
def change_func(tt):
  coins=tt
  balance = int(input("Please enter amount: "))
  if balance >= coins:
    change = balance - coins
    print("Your change is: ", change)
  elif balance == coins:
    print("No amount due.")
  else:
    balance <= coins
    print("Invalid amount. Error")



#----------------MAIN BODY-------------------
#Using the IF-ELIF nested conditions
print(vending)
v = str(input("\nChoose from the following category, 'N' to quit: \n"))
if(v == 'Hot drinks'):
   while m<=1:
    print("\n**********************************\n")
    for i in hot_drinks:
     #Prints menu
     print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
     print("--------------------------------------------\n")
    print("**********************************\n")
    #Compares the users entered "Item id", product code
    print("Enter the item ID for your wanted product or 'Finish' to quit: ")
    chitem_id = str(input())
    if (chitem_id == 'A1'):
      j=hd1
      total+=hd1["item_price"]   
      dispensed.append(hd1["item"]) #Adding user's selected item's  
      hotd = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      if (hotd == 'Y'):
        continue
      else:
         change_func(total)
         break
    elif (chitem_id == 'A2'):
      total+=hd2["item_price"]
      dispensed.append(hd2["item"])
      hotd = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      if (hotd == 'Y'):
        continue
      else:
        change_func(total)
        break  
      print("\nYour products are: ")
      print(f"Item: {hd2['item']} --- Price: {hd2['item_price']}")
    elif (chitem_id == 'A3'):
      total+=hd3["item_price"]
      hotd = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      dispensed.append(hd3["item"])
      if (hotd == 'Y'):
        continue
      else:
        change_func(total) 
        break 
    elif (chitem_id == 'A4'):
      total+=hd4["item_price"]
      hotd = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      dispensed.append(hd4["item"])
      if (hotd == 'Y'):
        continue
      else:
        change_func(total) 
        break 
    elif (chitem_id == "Finish"):
      print(total)
    else:
      print("\nPlease enter a valid response\n")
   else:
     print("INVALID RESPONSE")

     print("The products dispensed are: ", dispensed) #Dispensing user's selected item's
     print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
   selection = str(input("Press 'C' to continue buying, 'Q' to quit: ")) #Variable for user if they would like to continue or quit
   if selection == 'C':
     vm = (vending(v))
     print(vm)
   else:
    print("Have a good day!\n")

     

    
elif(v == 'Cold drinks'):
  while m<=1:
    print("\n**********************************\n")
    for i in cold_drinks:
     #Prints menu
      print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
      print("--------------------------------------------\n")
    print("**********************************\n")
    #Compares the users entered "Item id", product code
    print("Enter the item ID for your wanted product or 'Finish' to quit: ") 
    cditem_id = str(input())
    if (cditem_id == 'B1'):
      j=cd1
      total+=cd1["item_price"]   
      dispensed.append(cd1["item"]) #Adding user's selected item's  
      cold = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      if (cold == 'Y'):
        continue
      else:
        change_func(total)
        break
    elif (cditem_id == 'B2'):
      total+=cd2["item_price"]
      dispensed.append(cd2["item"])
      cold = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      if (cold == 'Y'):
        continue
      else:
        change_func(total)
        break  
      print("\nYour products are: ")
      print(f"Item: {cd2['item']} --- Price: {cd2['item_price']}")
    elif (cditem_id == 'B3'):
      total+=cd3["item_price"]
      cold = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      dispensed.append(cd3["item"])
      if (cold == 'Y'):
        continue
      else:
        change_func(total) 
        break 
    elif (cditem_id == 'B4'):
      total+= cd4["item_price"]
      cold = (input("\nWould you like to add another Drink? Enter 'Y' or else 'N' : \n"))
      dispensed.append(hd4["item"])
      if (cold == 'Y'):
        continue
      else:
        change_func(total) 
        break 
    elif (cditem_id == "Finish"):
      print(total)
    else:
      print("\nPlease enter a valid response\n")
  else:
     print("INVALID RESPONSE")

     print("The products dispensed are: ", dispensed) #Dispensing user's selected item's
     print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  selection = str(input("Press 'C' to continue buying, 'Q' to quit: ")) #Variable for user if they would like to continue or quit
  if selection == 'C':
       vm = (vending(v))
       print(vm)
  else:
    print("Have a good day!\n")


elif(v == 'Chips'):
  while m<=1:
    print("\n**********************************\n")
    for i in chips:
      #Prints menu
      print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
      print("--------------------------------------------\n")
    print("**********************************\n")
    #Compares the users entered "Item id", product code
    print("Enter the item ID for your wanted product or 'Finish' to quit: ")
    cpitem_id = str(input())
    if (cpitem_id == 'C1'):
      j=c1
      total+=c1["item_price"]   
      dispensed.append(c1["item"]) #Adding user's selected item's 
      chip = (input("\nWould you like to add another Chips? Enter 'Y' or else 'N' : \n"))
      if (chip == 'Y'):
        continue
      else:
        change_func(total)
        break
    elif (cpitem_id == 'C2'):
      total+=c2["item_price"]
      dispensed.append(c2["item"])
      chip = (input("\nWould you like to add another Chips? Enter 'Y' or else 'N' : \n"))
      if (chip == 'Y'):
        continue
      else:
        change_func(total)
        break  
      print("\nYour products are: ")
      print(f"Item: {c2['item']} --- Price: {c2['item_price']}")
    elif (cpitem_id == 'C3'):
      total+=c3["item_price"]
      cold = (input("\nWould you like to add another Chips? Enter 'Y' or else 'N' : \n"))
      dispensed.append(c3["item"])
      if (cold == 'Y'):
        continue
      else:
        change_func(total) 
        break 
    elif (cpitem_id == 'C4'):
      total+= c4["item_price"]
      chip = (input("\nWould you like to add another Chips? Enter 'Y' or else 'N' : \n"))
      dispensed.append(c4["item"])
      if (chip == 'Y'):
        continue
      else:
        change_func(total) 
        break 
    elif (cpitem_id == "Finish"):
       print(total)
    else:
      print("\nPlease enter a valid response\n")
  else:
     print("INVALID RESPONSE")

     print("The products dispensed are: ", dispensed) #Dispensing user's selected item's
     print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  selection = str(input("Press 'C' to continue buying, 'Q' to quit: ")) #Variable for user if they would like to continue or quit
  if selection == 'C':
     vm = (vending(v))
     print(vm)
  else:
      print("Have a good day!\n")

elif(v == 'Chocolate'):
  while m<=1:
    print("\n**********************************\n")
    for i in chocolate:
     #Prints menu
      print(f"Item: {i['item']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")
      print("--------------------------------------------\n")
    print("**********************************\n")
    #Compares the users entered "Item id", product code
    print("Enter the item ID for your wanted product or 'Finish' to quit: ")
    citem_id = str(input())
    if (citem_id == 'D1'):
      j=ch1
      total+=ch1["item_price"]   
      dispensed.append(ch1["item"]) #Adding user's selected item's 
      choco = (input("\nWould you like to add another Chocolate? Enter 'Y' or else 'N' : \n"))
      if (choco == 'Y'):
        continue
      else:
        change_func(total)
        break
    elif (citem_id == 'D2'):
      total+=ch2["item_price"]
      dispensed.append(ch2["item"])
      choco = (input("\nWould you like to add another Chocolate? Enter 'Y' or else 'N' : \n"))
      if (choco == 'Y'):
        continue
      else:
        change_func(total)
        break  
      print("\nYour products are: ")
      print(f"Item: {ch2['item']} --- Price: {ch2['item_price']}")
    elif (citem_id == 'D3'):
      total+=ch3["item_price"]
      choco = (input("\nWould you like to add another Chocolate? Enter 'Y' or else 'N' : \n"))
      dispensed.append(ch3["item"]) #Dispensing user's selected item's
      if (choco == 'Y'):
        continue
      else:
        change_func(total) 
        break 
      
    elif (citem_id == "Finish"):
      print(total)
    else:
      print("\nPlease enter a valid response\n")
else:
  print("INVALID RESPONSE")

  print("The products dispensed are: ", dispensed)
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
  print("Thank you for using our vending machine!\n")
selection = str(input("Press 'C' to continue buying, 'Q' to quit: ")) #Variable for user if they would like to continue or quit
if selection == 'C':
    vm = (vending(v))
    print(vm)
else:
    print("Have a good day!\n")

 