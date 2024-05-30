import random

# room of 4 * 4

room = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# function to display rooms


def display(room):
    for row in room:
        print(row)


print("Initially all rooms are dirty")
display(room)

# introduce dirt[0] clean[1]

for x in range(8):
    for y in range(8):
        room[x][y] = random.choice([0, 1])

display(room)

# modelling the vaccum cleaner
dirt_rooms = 0
for x in range(8):
    for y in range(8):
        if room[x][y] == 1:
            print("Cleanig the room")
            room[x][y] = 0
            dirt_rooms += 1

performance = (100 - (dirt_rooms / 64))
print(f"Performance: {performance}%")
