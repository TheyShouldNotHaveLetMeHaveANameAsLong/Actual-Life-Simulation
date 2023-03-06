import random, os, math, namemaker
cycles = 0
temp = int(input("What is the temperature? "))
os.system("clear")
animals = []
x = 0
class Animal:
  def __init__(self, mutchance, mutation_severity, lifespan, foodfind, size, diet, opportunity_for_food, basetemp, temprange, id, tag, generation):
    #alive
    self.alive = True
    #mutation chance
    self.mutchance = mutchance
    #mutation severity
    self.mut = mutation_severity
    #life span
    self.lifespan = lifespan
    #age in days
    self.age = 0
    #food find chance
    self.foodfind = foodfind
    #size
    self.size = size
    #energy
    self.energy = 0
    #max energy they can carry
    self.maxenergy = self.size * random.randint(3,6)
    #diet
    self.diet = diet
    #opportunity to find food in a given cycle
    self.oppo = opportunity_for_food
    #minimum temperature
    self.basetemp = basetemp
    #range of temperature they can live in
    self.temprange = temprange
    #energy maintenance
    self.maintenance = math.floor((size + opportunity_for_food)/3.5)
    #reproduction cost
    self.reprodcost = size * random.randint(1,2)
    #id
    self.id = id
    #tag
    self.tag = tag
    #generation
    self.gen = generation
    
    

  def mutate(self):
    chance = random.randint(1,100)
    # if the chance is higher than the mutation chance
    if chance <= self.mutchance:
      # the mutation is random from mutation severity
      mutate = random.randint(-1*self.mut,self.mut)
    # if it isn't
    else:
      # the mutation is nothing
      mutate = 0
    # return the mutation amount
    return mutate

  
  def reproduce(self):
    global x
    x += 1
    newmutchance = self.mutchance + self.mutate()
    if newmutchance < 0:
      newmutchance = 0
    if newmutchance > 100:
      newmutchance = 100
    newmut = self.mut + self.mutate()
    if newmut < 0:
      newmut = 0
    newlifespan = self.lifespan + self.mutate()
    if newlifespan <= 0:
      newlifespan = 1
    newfoodfind = self.foodfind + self.mutate()
    if newfoodfind < 0:
      newfoodfind = 0
    if newfoodfind > 100:
      newfoodfind = 100
    newsize = self.size + self.mutate()
    if newsize <= 0:
      newsize = 0
    change = random.randint(1,100)
    if change == 100:
      if self.diet == "carnivore":
        newdiet = "herbivore"
      if self.diet == "herbivore":
        newdiet = "carnivore"
    else:
      newdiet = self.diet
    newoppo = self.oppo + self.mutate()
    if newoppo < 1:
      newoppo = 1
    newbasetemp = self.basetemp + self.mutate()
    newtemprange = self.temprange + self.mutate()
    newtemprange = abs(newtemprange)
    
    
    
    newtag = self.tag
    newgen = self.gen + 1
    animals.append(Animal(newmutchance, newmut, newlifespan, newfoodfind, newsize, newdiet, newoppo, newbasetemp, newtemprange, x, newtag, newgen))

  def findfood(self):
    if self.diet == "herbivore":
      for i in range(1,self.oppo):
        chance = random.randint(1,100)
        if chance <= self.foodfind:
          self.energy += 1
          if self.energy > self.maxenergy:
            self.energy -= 1
        else:
          pass

    if self.diet == "carnivore":
      for i in range(1,self.oppo):
        chance = random.randint(1,100)
        if chance <= self.foodfind:
          targetnot = True
          h = 0
          while targetnot:
            target = random.choice(animals)
            if target.id == self.id:
              h += 1
              if h > 10:
                animals.remove(self)
              pass
              
          fighting = True
          myhealth = self.size * 3
          enemyhealth = target.size * 3
          while fighting:
            myhealth -= target.size
            enemyhealth -= self.size
            if myhealth <= 0:
              self.alive = False
            if enemyhealth <= 0:
              target.alive = False

            if myhealth <= 0 or enemyhealth <= 0:
              fighting = False
          self.energy += math.floor(target.size * 1.5)
          if self.energy > self.maxenergy:
            self.energy = self.maxenergy
            

  def maintain(self):
    self.energy -= self.maintenance
    if self.energy < 0:
      self.alive = False

    
  def main(self):
    if temp > self.basetemp + self.temprange:
      self.alive = False
      animals.remove(self)
    if temp < self.basetemp - self.temprange:
      self.alive = False
      animals.remove(self)
    if self.alive == True:
      self.age += 1
      if self.age >= self.lifespan:
        self.alive = False
      if self.alive == True:
        self.findfood()
        self.maintain()
    else:
      for i in animals:
        if i.id == self.id:
          animals.remove(i)
    if self.reprodcost <= self.energy:
      self.reproduce()

def creature_creator():
  global x
  x += 1
  newmutchance = int(input("What would you like the mutation chance to be? (Base 1, 10) "))
  if newmutchance > 100:
    newmutchance = 100
  if newmutchance < 0:
    newmutchance = 0
  newmut = int(input("What would you like the mutation severity to be? (Base 1, 20) "))
  if newmut < 0:
    newmut = 0
  newlifespan = int(input("What would you like the lifespan to be? (Base 5,12) "))
  if newlifespan <= 0:
    newlifespan = 0
  newfoodfind = int(input("What would you like the new food finding chance to be? (Base 70, 90) "))
  if newfoodfind > 100:
    newfoodfind = 100
  if newfoodfind < 0:
    newfoodfind = 0
  newsize = int(input("What would you like the new size to be? (Base 3, 5) "))
  if newsize < 1:
    newsize = 1
  newoppo = int(input("What would you like the new food finding opportunities to be? (Base 3, 5) "))
  if newoppo < 0:
    newoppo = 0
  newbasetemp = int(input("What would the base temp of the new creature be? (Base 50,60)"))
  newtemprange = int(input("What is the temperature range of this creature? (Base 4,12)"))
  newdiet = str(input("What would you like the new diet to be? (Choose herbivore or carnivore) "))
  
  newtag = str(input("What would you like the creature's new tag to be? "))
  animals.append(Animal(newmutchance, newmut, newlifespan, newfoodfind, newsize, newdiet, newoppo, newbasetemp, newtemprange, x, newtag, 0))
  


print("How many creatures would you like to start? ")
foo = int(input(""))
for i in range(1,foo+1):
  x += 1
  animals.append(Animal(random.randint(1,10), random.randint(1,20), random.randint(5,12), random.randint(70,90), random.randint(3,5), "herbivore", random.randint(3,5), random.randint(50,60), random.randint(4,12), x, None, 1))
question = input("Randomly generate names? Y/N")
if question.lower() == "y":
  for i in animals:
    i.tag = namemaker.gen_name()
else:
  pass
os.system("clear")

while True:
  print("___________________________\nTEMPERATURE : %i\nCYCLES : %i\n___________________________\n\nCREATURES:\n1 [SHOW CREATURES]\n2 [PROGRESS WITH SIMULATION]\n3 [CREATE CUSTOM CREATURE]\n4 [CHANGE TEMPERATURE]"%(temp, cycles))
  choice = input("___________________________\n\n")
  if choice == "1":
    print("\n|HERBIVORES|\n")
    herbivores = []
    for i in animals:
      if i.diet == "herbivore":
        herbivores.append(i)
        if i.tag == None:
          print("|Creature %i|"% i.id)
        else:
          print("|%s %i|" % (i.tag, i.id))
    print("\n|CARNIVORES|\n")
    carnivores = []
    for i in animals:
      if i.diet == "carnivore":
        carnivores.append(i)
        if i.tag == None:
          print("|Creature %i|"% i.id)
        else:
          print("|%s %i|" % (i.tag, i.id))
    choice = input("")
    
    for i in animals:
      if i.tag == choice or str(i.id) == choice:
        if i.tag == None:
          print("\n\n\n        [%i]\n[Mutation Chance : %i]\n[Mutation Severity : %i]\n[Lifespan : %i]\n[Food Finding Chance : %i]\n[Age : %i]\n[Size : %i]\n[Energy : %i]\n[Max Energy : %i]\n[Diet : %s]\n[Opportunities for eating : %i]\n[Base Survival Temperature : %i]\n[Temperature Variation Range : %i]\n[Energy Maintenance : %i]\n[Reproduction Cost : %i]\n[Generation : %i]\n\n\n" % (i.id, i.mutchance, i.mut, i.lifespan, i.foodfind, i.age, i.size, i.energy, i.maxenergy, i.diet, i.oppo, i.basetemp, i.temprange, i.maintenance, i.reprodcost, i.gen))
        if i.tag == choice:
          print("\n\n|HERBIVORE|\n")
          for i in animals:
            if i.tag == choice:
              if i.diet == "herbivore":
                
                print("|%s %i|"%(i.tag, i.id))
            
          print("\n\n|CARNIVORE|\n")
          for i in animals:
            if i.tag == choice:
              if i.diet == "carnivore":
                print("|%s %i|"%(i.tag, i.id))
                
          newchoice = int(input("\n\n"))
          for i in animals:
            if i.id == newchoice:
              print("\n\n\n        [%s]\n[Mutation Chance : %i]\n[Mutation Severity : %i]\n[Lifespan : %i]\n[Food Finding Chance : %i]\n[Age : %i]\n[Size : %i]\n[Energy : %i]\n[Max Energy : %i]\n[Diet : %s]\n[Opportunities for eating : %i]\n[Base Survival Temperature : %i]\n[Temperature Variation Range : %i]\n[Energy Maintenance : %i]\n[Reproduction Cost : %i]\n[Generation : %i]\n\n\n" % (i.tag, i.mutchance, i.mut, i.lifespan, i.foodfind, i.age, i.size, i.energy, i.maxenergy, i.diet, i.oppo, i.basetemp, i.temprange, i.maintenance, i.reprodcost, i.gen))
        choice = input("\n")
        if choice == "tag":
          newtag = input("CREATURE NAME: ")
          if newtag == "Randomname":
            newtag = namemaker.gen_name()
          for g in animals:
            if g.id == i.id:
              i.tag = newtag
              
        if choice == "kill":
          animals.remove(i)
        
        
        
      
      
  

    
    
    

    


  if choice == "2":
    cycles += 1
    for i in animals:
      i.main()

  if choice == "3":
    creature_creator()
  os.system("clear")

  if choice == "kill all carnivores":
    e = []
    for i in animals:
      if i.diet == "carnivore":
        e.append(i)
    for i in e:
      animals.remove(i)
  if choice == "kill all herbivores":
    e = []
    for i in animals:
      if i.diet == "herbivore":  
        e.append(i)
    for i in e:
      animals.remove(i)

  if choice == "rename all carnivores":
    name = str(input("What do you want to name all the carnivores? "))
    for i in animals:
      if i.diet == "carnivore":
        i.tag = name
  if choice == "rename all herbivores":
    name = str(input("What do you want to name all the herbivores? "))
    for i in animals:
      if i.diet == "herbivore":
        i.tag = name

  if choice == "extinction":
    length = len(animals)
    extpercent = int(input("What percent would you like to extinct? "))
    extnum = int(length * (extpercent/100))
    extincting = True
    while extincting:
      for i in animals:
        y = i
        if len(animals) == length - extnum:
          extincting = False
          break
        chance = random.randint(0,1)
        if chance == 0:
          animals.remove(y)
        if chance == 1:
          pass
        if len(animals) == length - extnum:
          extincting = False
          break
        
  if choice == "4":
    change = int(input("What would you like to change the temperature by? "))
    confirm = input("CHANGE TEMPERATURE TO %i? Y/N\n"% (int(temp)+int(change)))
    if confirm.lower() == "y":
      temp += change
    if confirm.lower() == "n":
      pass