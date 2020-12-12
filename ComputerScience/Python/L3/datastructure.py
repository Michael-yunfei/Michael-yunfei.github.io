symbols = "$%*_(*)"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

codes = [ord(symbol) for symbol in symbols]  # list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# [('black', 'S'),
#  ('black', 'M'),
#  ('black', 'L'),
#  ('white', 'S'),
#  ('white', 'M'),
#  ('white', 'L')]

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
print(((c, s) for c in colors for s in sizes))
# <generator object <genexpr> at 0x7fdaad15f480>

for tshirts in ('{} {}'.format(c, s) for c in colors for s in sizes):
    print(tshirts)

# black S
# black M
# black L
# white S
# white M
# white L















#
