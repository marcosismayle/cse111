from datetime import datetime

discount_rate = .10
sales_tax = .06

subtotal = float(input("Please enter the subtotal: "))

current_date_time = datetime.now()
day_of_week = current_date_time.weekday()

if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discount = subtotal * discount_rate
        subtotal = subtotal - discount
        print(f'Discount amount: {discount:.2f}')

sales_tax_amount = subtotal * sales_tax
print(f'Sales tax amount: {sales_tax_amount:.2f}')

total_amount = subtotal + sales_tax_amount
print(f'Tottal: {total_amount:.2f}')
