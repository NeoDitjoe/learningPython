prices = [ 200, 187, 120, 199 ]
total_price = 0


for price in prices:
  total_price += price
  
print(f'Total: R {total_price}')
print('Total: R %i' %(total_price))