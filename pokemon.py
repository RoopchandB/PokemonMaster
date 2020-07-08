class Pokemon:
  def __init__(self,name,pokemon_type,level = 5):
    self.name = name
    self.level = level
    self.pokemon_type = pokemon_type
    self.current_health = level * 10
    self.max_health = level * 10
    self.knocked_down = False

  def __repr__(self):
    return "{} is a level {} .The type of pokemon are {} Pokemon with {} health.".format(self.name, self.level,self.pokemon_type,self.current_health)
  
  def knocked_out(self):
    self.knocked_down = True
    if(self.current_health != 0):
      self.current_health = 0
    print("{} is knocked down.".format(self.name))

  def revive(self):
    self.knocked_down == False
    if self.current_health == 0:
      self.current_health = 1
    print("{} is revived!".format(self.name))

  def health_lost(self,total_health):
    self.current_health -= total_health
    print("{} lost {} health from current_health".format(self.name,self.total_health))
    if(self.current_health <=0):
      self.current_health = 0
      self.knocked_out()
    else:
      print("The left over health of {} is {}".format(self.name,self.current_health)) 
  

  def health_gained(self, total_health):
    if self.current_health == 0:
      self.revive()
    self.current_health += total_health
    if self.current_health > self.max_health:
      self.current_health = self.max_health
    print("{} has gained health of {}.".format(self.name,self.current_health))
    print("{}'s current health is {}".format(self.name, self.current_health))

  def attack(self, enemy_pokemon):
    if self.knocked_down:
      print("{} is currently knocked out and cannot attack.".format(self.name))
    return
    if (self.pokemon_type == "Fire" and enemy_pokemon.pokemon_type == "Water") or (self.pokemon_type == "Water" and enemy_pokemon.pokemon_type == "Grass") or (self.pokemon_type == "Grass" and enemy_pokemon.pokemon_type == "Fire"):
      print("{} attacked {} for {} damage.".format(self.name, enemy_pokemon.name, damage = round(self.level * 0.5)))
      print("It's not very effective")
      enemy_pokemon.lose_health(round(self.level * 0.5))

    if (self.pokemon_type == enemy_pokemon.pokemon_type):
      print("{} attacked {} for {} damage.".format(self.name, enemy_pokemon.name, damage = self.level))
      enemy_pokemon.lose_health(self.level)

    if (self.pokemon_type == "Fire" and enemy_pokemon.pokemon_type == "Grass") or (self.pokemon_type == "Water" and enemy_pokemon.pokemon_type == "Fire") or (self.pokemon_type == "Grass" and enemy_pokemon.pokemon_type == "Water"):
      print("{} attacked {} for {} damage.".format(self.name, enemy_pokemon.name, damage = self.level * 2))
      print("It's super effective")
      enemy_pokemon.lose_health(self.level * 2)


class Trainer:
  def __init__(self, pokemon_list, name, num_potions = 3):
    self.pokemons = pokemon_list
    self.name = name
    self.potions = num_potions
    self.current_pokemon = 0

#Check Trainer's Pokemon, current Pokemon, and potions
  def __repr__(self):
    print('Trainer {} has the following Pokemon and potions:'.format(self.name))
    for pokemon in self.pokemons:
      print(pokemon)
    print('Potions - {}'.format(self.potions))
    return 'Their current active pokemon is {}.'.format(self.pokemons[self.current_pokemon].name)

#Use potion and revive a knocked out Pokemon
  def use_potion(self, potion):
    if self.potions > 0:
      self.potions -= potion
      print('You used a potion on {}.'.format(self.pokemons[self.current_pokemon].name))
      #Revive Pokemon if it's health was 0
      if self.pokemons[self.current_pokemon].current_health == 0:
        self.pokemons[self.current_pokemon].revive()
      self.pokemons[self.current_pokemon].health_gained(10)
      #Potion cannot increase health beyond health max
      if self.pokemons[self.current_pokemon].current_health > self.pokemons[self.current_pokemon].max_health:
        self.pokemons[self.current_pokemon].current_health = self.pokemons[self.current_pokemon].max_health
    else:
      print('You have no potions to use.')

  #Attack another trainer's Pokemon
  def attack_opponent(self, opp_trainer):
    self.pokemons[self.current_pokemon].attack(opp_trainer.pokemons[opp_trainer.current_pokemon])

  #Switch current pokemon to another in your list
  def switch_current_pokemon(self, new_pokemon):
    if new_pokemon <= len(self.pokemons) and new_pokemon >= 0:
      #You cannot switch to a knocked out Pokemon
      if self.pokemons[new_pokemon].knocked_out:
        print('{} is knocked out. Choose another Pokemon.'.format(self.pokemons[new_pokemon].name))
      #You cannot switch to your current Pokemon
      elif self.pokemons[new_pokemon] == self.pokemons[self.current_pokemon]:
        print('Choose another Pokemon. {} is already your current Pokemon.'.format(self.pokemons[new_pokemon].name))
      #Switch to a new Pokemon in your list
      elif self.pokemons[new_pokemon] != self.pokemons[self.current_pokemon]:
        self.current_pokemon = new_pokemon
        print('Go {}, you\'re up!'.format(self.pokemons[self.current_pokemon].name))

#POKEMON TO PLAY
Charmander = Pokemon('Charmander', 'Fire', level = 8)
Scorbunny = Pokemon('Scorbunny', 'Fire', level = 5)
Squirtle = Pokemon('Squirtle', 'Water', level = 6)
Blastoise = Pokemon('Blastoise', 'Water', level = 4)
Bulbasaur = Pokemon('Bulbasaur', 'Grass', level = 1)
Lotad = Pokemon('Lotad', 'Grass', level = 7)

#TRAINERS TO PLAY
Ash = Trainer([Charmander, Bulbasaur], 'Ash', num_potions = 10)
Blaine = Trainer([Squirtle, Lotad], 'Blaine', num_potions = 7)
Misty = Trainer([Scorbunny, Blastoise], 'Misty', num_potions = 8)

print(Ash)
print(Blaine)
print(Misty)

Ash.attack_opponent(Blaine)
Misty.attack_opponent(Ash)
Blaine.attack_opponent(Misty)


Charmander.knocked_out()
print(Ash)
Ash.use_potion(1)
print(Ash)


Lotad.knocked_out()
Blaine.switch_current_pokemon(0)
Blaine.switch_current_pokemon(1)




