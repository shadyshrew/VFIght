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


Rad= enemy(5)
Fag= enemy(6)
GreyWind= enemy(7)

Rad.status()
Fag.status()
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
        Fag.light()

    if r is 'b':
        Fag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()



Rad.status()
Fag.status()
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
        Fag.light()

    if r is 'b':
        Fag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()


Rad.status()
Fag.status()
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
        Fag.light()

    if r is 'b':
        Fag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()


Rad.status()
Fag.status()
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
        Fag.light()

    if r is 'b':
        Fag.heavy()
else:

    if r is 'a':
        GreyWind.light()
    if r is 'b':
        GreyWind.heavy()
Rad.status()
Fag.status()
GreyWind.status()


if (Rad.rety() is 1) & (Fag.rety() is 6) & (GreyWind.rety() is 7):
    print("You did it!")
else:
    print("Sad,Try it again")
