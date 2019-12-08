class enemy:


    def __init__(self,n):
        self.health=n
    def light(self):
        self.health-=1
    def heavy(self):
        self.health-=2
    def status(self):
        print("The health is: ")
        print(str(self.health))
    def rety(self):
        return self.health


print("RULES: There are three people.Rad, Tag and GreyWind\n Their health will be as shown, in the order of \n")
print("Rad Tag GreyWind\n")
print("These people pissed you off so obviously you need to beat them into a pulp\n")
print("A light attack does 1 damage and a heavy one does 2\n")
print("But, you cant kill them or you go to jail.\n")
print("Your mission thus is to get all their healths down to 4.\n")
print("But, you get only 4 turns to do so.")
print("Hope you fail,DUMBASS!")


Rad= enemy(5)
Tag= enemy(6)
GreyWind= enemy(7)

Rad.status()
Tag.status()
GreyWind.status()


l=input('Whom do you want to attack? \n a):Rad \n b):Tag \n c):GreyWind')
r=input('\n \n \n a):Light \n  b):Heavy \n')

if l is 'a':
    if r is 'a':
        Rad.light()
    if r is 'b':
        Rad.heavy()

elif l is 'b':
    if r is 'a':
        Tag.light()

    if r is 'b':
        Tag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()



Rad.status()
Tag.status()
GreyWind.status()


l=input('Whom do you want to attack? \n a):Rad \n b):Tag \n c):GreyWind')
r=input('\n \n \n a):Light \n  b):Heavy \n')
if l is 'a':
    if r is 'a':
        Rad.light()
    if r is 'b':
        Rad.heavy()

elif l is 'b':
    if r is 'a':
        Tag.light()

    if r is 'b':
        Tag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()


Rad.status()
Tag.status()
GreyWind.status()

l=input('Whom do you want to attack? \n a):Rad \n b):Tag \n c):GreyWind')
r=input('\n \n \n a):Light \n  b):Heavy \n')
if l is 'a':
    if r is 'a':
        Rad.light()
    if r is 'b':
        Rad.heavy()

elif l is 'b':
    if r is 'a':
        Tag.light()

    if r is 'b':
        Tag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()


Rad.status()
Tag.status()
GreyWind.status()

l=input('Whom do you want to attack? \n a):Rad \n b):Fag \n c):GreyWind')
r=input('\n \n \n a):Light \n  b):Heavy \n')
if l is 'a':
    if r is 'a':
        Rad.light()
    if r is 'b':
        Rad.heavy()

elif l is 'b':
    if r is 'a':
        Tag.light()

    if r is 'b':
        Tag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()
Rad.status()
Tag.status()
GreyWind.status()


if (Rad.rety() is 4) & (Tag.rety() is 4) & (GreyWind.rety() is 4):
    print("You did it!You are'nt stupid")
else:
    print("Lol, you're stupid")
