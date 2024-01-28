#stocks transaction program
commission=3/100
shares_purchased=float(input("please type in the number of shares you purchased: "))
purchase_price=float(input("please type in the price per share purchased: "))
shares_sold=float(input("please type in the number of shares you sold: "))
sold_price=float(input("please type in the price per share sold: "))
amount_paid= shares_purchased * purchase_price
print("Amount paid for the stock: ", amount_paid)
commission_paid=commission * amount_paid
print("Commission paid on the purchase: ", commission_paid)
amount_sold= shares_sold * sold_price
print("Amount the stock sold for: ", amount_sold)
commission_sold=commission * amount_sold
print("commission paid on the sale: ", commission_sold)
profit=amount_sold - amount_paid
if profit>0:
    print("Congrats! you made profit. this is your profit: ", profit)
else:
    print("You lost money, better luck next time! this is your loss: " , profit )
