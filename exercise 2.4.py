price = 99

quant = eval(input('Enter the number of packages purchased: '))

if 10 <= quant <= 19:
    disc = 0.1
    discstr = '10%'
    before = price * quant
elif 20 <= quant <= 49:
    disc = 0.2
    discstr = '20%'
    before = price * quant
elif 50 <= quant <= 99:
    disc = 0.3
    discstr = '30%'
    before = price * quant
elif 100 <= quant:
    disc = 0.4
    discstr = '40%'
    before = price * quant
elif quant <= 9:
    disc = 1
    discstr = '0%'
    before = 0

cut = before * disc
total = before - cut

print(f'Discount amount @ {discstr} : $ {cut}')
print(f'Total amount: $ {total}')
