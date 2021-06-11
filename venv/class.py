import random

class Person:
    def __int__(self,firstName,lastName,health,status):
        "Help to describ class"
        self.firstname=firstName
        self.lastname=lastName
        self.health=health
        self.status=status


    def introduce(self):
        print("Hello, my name is {} {}".format(self.firstname,self.lastname))

    def emote(self):
        emotion=random.randrange(1,3)
        if emotion==1:
            print("{} is happy today".format(self.firstname))
        elif emotion==2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health==100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health<=76:
            print("{} feels unwell.".format(self.firstname))
        elif self.health <=50:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))

class Enemy(Person):
    def __inti__(self,weapon,firstName,lastName,health,status):
        super.__init__(firstName,lastName,health,status)
        self.weapon=weapon

    def hurt(self,other):
        other.health-=10

Chanuka=Person("Chanuka","Dinuwan",95,status=True)
Dinuwan=Person("Dinuwan","Chanuka",88,status=False)

print("{} is my friend? {}".format(Chanuka.firstname,Chanuka.status))