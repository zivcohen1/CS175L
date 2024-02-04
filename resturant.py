#CS175
#Ziv Cohen
#resturant
while True:
    vegetarian=input("Is anyone in your party vegetarian? (Please answer by yes/no)").lower()
    vegan=input("Is anyone in your party vegan? ").lower()
    gluten=input("Is anyone in your party gluten-free? ").lower()
    if vegetarian=="yes" and vegan=="no" and gluten=="no":
     print("Here are your resturant choices. \n"
           "Mama's Fine italin\n"
           "Main street pizza company\n"
           "Corner cafe\n"
           "The chef's kitchen")
    elif vegetarian=="no" and vegan=="no" and gluten=="no":
        print("Here are your resturant choices. \n"
              "Joe's Gourmet Burgers\n"
              "Mama's Fine italin\n"
              "Main street pizza company\n"
              "Corner cafe\n"
              "The chef's kitchen")
    elif (vegetarian=="no" and vegan=="no" and gluten=="yes") or (vegetarian=="yes" and vegan=="no" and gluten=="yes"):
        print("Here are your resturant choices. \n"
              "Main street pizza company\n"
              "Corner cafe\n"
              "The chef's kitchen")
              
    else: 
         print("Here are your resturant choices. \n"
               "Corner Cafe\n"
               "The Chef's Kitchen")
    another_round=input("Would you like to enter diffrenet preferences? (yes/no)").lower()
    if another_round!="yes":
        print("Goodbye!")
        break 
