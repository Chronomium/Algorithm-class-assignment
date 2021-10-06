price = 99

quant = eval(input('Enter the number of packages purchased: '))
before = price * quant

if 10 <= quant <= 19:
    disc = 0.1
    discstr = '10%'
    cut = before * disc
elif 20 <= quant <= 49:
    disc = 0.2
    discstr = '20%'
    cut = before * disc
elif 50 <= quant <= 99:
    disc = 0.3
    discstr = '30%'
    cut = before * disc
elif 100 <= quant:
    disc = 0.4
    discstr = '40%'
    cut = before * disc
elif quant <= 9:
    disc = 1
    discstr = '0%'
    cut = 0

total = before - cut

print(f'Discount amount @ {discstr} : $ {cut}')
print(f'Total amount: $ {total}')
