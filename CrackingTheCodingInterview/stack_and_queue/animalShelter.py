import random

class Animal:
    def __init__(self, atype, serial):
        self.atype = atype
        self.serial = serial

class AnimalShelter:
    def __init__(self):
        self.dogList = []
        self.catList = []
        self.serialIds = 0

    def enqueue(self, atype):
        self.serialIds += 1
        animal = Animal(atype, self.serialIds)
        if atype == 'dog':
            self.dogList.append(animal)
        elif atype == 'cat':
            self.catList.append(animal)
        else:
            print("Incorrect animal type. Choose `dog` or `cat`.")

    def dequeueAny(self):
        print("Bbye the oldest animal:")
        if self.dogList[0].serial < self.catList[0].serial:
            return self.dogList.pop(0)
        else:
            return self.catList.pop(0)

    def dequeueDog(self):
        print("Bbye the oldest dog:")
        if len(self.dogList) == 0:
            print("List Empty")
        return self.dogList.pop(0)

    def dequeueCat(self):
        print("Bbye the oldest cat:")
        if len(self.dogList) == 0:
            print("List Empty")
        return self.catList.pop(0)

    def printList(self):
        print("Dog list:", [(item.atype,item.serial) for item in self.dogList])
        print("Cat list:", [(item.atype,item.serial) for item in self.catList])

if __name__ == '__main__':
    shelter = AnimalShelter()
    atypes = {
        0: 'cat',
        1: 'dog'
    }
    for _ in range(10):
        shelter.enqueue(atypes[random.randint(0,1)])
    shelter.printList()
    shelter.dequeueAny()
    shelter.printList()
    shelter.dequeueDog()
    shelter.printList()
    shelter.dequeueCat()
    shelter.printList()

