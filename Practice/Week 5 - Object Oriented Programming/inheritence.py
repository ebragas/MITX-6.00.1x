
# # Animal class
# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     def set_age(self, newage):
#         self.age = newage
#     def set_name(self, newname):
#         self.name = newname
#     def __str__(self):
#         return "animal: {}:{}".format(self.name, self.age)

# # Cat class
# class Cat(Animal):
#     def speak(self):
#         print("meow")
#     def __str__(self):
#         return "cat:{}:{}".format(self.name, self.age)


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())