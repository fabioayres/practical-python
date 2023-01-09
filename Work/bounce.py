# bounce.py
#
bounces = 1
height = 100
while bounces <= 10:
    height *= 0.6
    print(f'{bounces} {round(height, 4)}')
    bounces += 1
# Exercise 1.5
