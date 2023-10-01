# opdracht 1 
 
import random

bingo_card = []
bingo_card_rows = 4
bingo_numbers_total = bingo_card_rows ** 2

all_bingo_numbers = list(range(1,100))
random.shuffle(all_bingo_numbers)

bingo_card_numbers = all_bingo_numbers[:bingo_numbers_total]

for line in range(bingo_card_rows):
    bingo_row = []

    for column in range(bingo_card_rows):
        bingo_row.append(bingo_card_numbers.pop())
    bingo_card.append(bingo_row)

print(bingo_card)


draw_number = 50
bingo_balls = list(range(1,100))
random.shuffle(bingo_balls)

draw_balls = bingo_balls[:draw_number]

