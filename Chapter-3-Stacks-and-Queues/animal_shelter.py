'''
3.6
Animal Shelter

An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
You may use the built-in LinkedList data strucutre.
'''

from collections import deque

# define an Animal, then insert these animals into queues (found in the AnimalShelter)
class Animal:
    def __init__(self, name, species, arrival_time):
        self.name = name
        self.species = species
        self.arrival_time = arrival_time

# The actual animal shelter, which will consist of two queues, one for dogs and one for cats.
class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.arrival_order = 0  
    # add an animal to the shelter, stamping a relative arrival_order to their arrival_time
    def enqueue(self, name, species):
        if species not in ('dog', 'cat'):
            raise ValueError("Animal must be either 'dog' or 'cat'")
        animal = Animal(name, species, self.arrival_order)
        if species == 'dog':
            self.dogs.append(animal)
        else:
            self.cats.append(animal)
        self.arrival_order += 1 
    # dequeue any animal, dependent on the arrival_time of either the smallest arrival time (which increments every time an animal is added)
    def dequeueAny(self):
        if not self.dogs and not self.cats:
            return None 
        if not self.dogs:
            return self.dequeueCat()
        if not self.cats:
            return self.dequeueDog()

        if self.dogs[0].arrival_time < self.cats[0].arrival_time:
            return self.dequeueDog()
        else:
            return self.dequeueCat()
    # dequeue the first dog
    def dequeueDog(self):
        if self.dogs:
            return self.dogs.popleft()
        return None 
    # dequeue the first cat
    def dequeueCat(self):
        if self.cats:
            return self.cats.popleft()
        return None 
    # return current state of the Animal Shelter
    def __str__(self):
        dogs_list = [f"{dog.name} (dog)" for dog in self.dogs]
        cats_list = [f"{cat.name} (cat)" for cat in self.cats]
        return f"Dogs: {dogs_list}\nCats: {cats_list}"

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("Buddy", "dog")
    shelter.enqueue("Mittens", "cat")
    shelter.enqueue("Rex", "dog")
    shelter.enqueue("Whiskers", "cat")
    print(shelter)

    print(shelter.dequeueAny().name)  
    print(shelter.dequeueCat().name) 
    print(shelter.dequeueDog().name) 
    print(shelter)  

# dogs :[buddy (1), rex(3), ]

# cats: [mittens (2), whiskers(4)]
