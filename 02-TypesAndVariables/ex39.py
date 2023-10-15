price = float(input('Enter price: '))
disc = int(input('Enter discount: '))


discamount = price*(disc/100)
pwdisc = price - discamount


print(f"""
      The price is: {pwdisc} 
      The discount is: {discamount}""")