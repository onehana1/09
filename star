class Star:

    type = 'Star'
    x = 100

    def change():
        x= 200
        print('x is ', x)

print('x IS ' , Star.x)
Star.change()
print('x IS ', Star.x)

star = Star()
print('x IS ', Star.x)
star.change()

# 파이썬은 생성자가 없어도 된다

class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

print(Player.type)

Player.where()
Player.where(player)


