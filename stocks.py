#CS175
#Ziv Cohen
#stocks
commission_purchase=float(input("Please enter commision rate percentage (ex 0.03) on stock purchase: "))
commission_sale=float(input("Please enter commission rate percentage (ex 0.03) on stock sale: "))
shares_purchased=float(input("please enter number of shares you purchased: "))
shares_sold=float(input("please enter number of shares you sold: "))
purchase_price=float(input("Please enter purchase price per share : "))
sold_price=float(input("please enter sell price per share: "))
amount_paid= shares_purchased * purchase_price
print("Amount paid for the stock: ", f'${amount_paid:,.2f}')
commission_paid= commission_purchase * amount_paid
print("Commission paid on the purchase: ", f'${commission_paid:,.2f}')
amount_sold= shares_sold * sold_price
print("Amount the stock sold for: ", f'${amount_sold:,.2f}')
commission_sold= commission_sale * amount_sold
print("commission paid on the sale: ", f'${commission_sold:,.2f}')
profit= amount_sold - (amount_paid + commission_sold + commission_paid)
if profit>0:
    print("Congrats! you made profit. this is your profit: ", f'${profit:,.2f}')
else:
    print("You lost money, better luck next time! this is your loss: " , f'${profit:,.2f}' )
