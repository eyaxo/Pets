from pets2 import Pet 
from ninjas import Ninja

bruno = Pet("Bruno", 'cocker spaniel', 'gives paw', 100, 100) 
eya = Ninja("Eya", "Avila", bruno, 'bone', 'Pedigree')

eya.walk().feed().bathe()
bruno.sleep().eat().play().noise()

# print(bruno.energy)
# print(bruno.health)
# print(bruno.noise)