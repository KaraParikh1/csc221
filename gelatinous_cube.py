from datetime import datetime
"""
  >>> dave = GelCube("dave", 2)
  >>> print(dave.hp)
  999999999999999999999999999999
  >>> dave.take_damage(199)
  >>> print(dave.hp)
  999999999999999999999999999800
  >>> bob = victim("bob")
  >>> jerry = victim("jerry")
  >>> print(bob.hp)
  1200
  >>> print(jerry.hp)
  1200
  >>> dave.absorb(bob)
  >>> print(dave.victims)
  [bob]
  >>> dave.burn()
  >>> print(bob.hp)
  1100
  >>> dave.absorb(jerry)
  >>> print(dave.victims)
  [bob, jerry]
  >>> dave.burn()
  >>> print(bob.hp)
  1000
  >>> print(jerry.hp)
  1100
  >>> garry = victim("garry")
  >>> dave.absorb(garry)
  cannot absorb more victims at this time
  >>> print(dave.victims)
  [bob, jerry]
  >>> print(dave.is_absorbed(jerry))
  True
  >>> dave.hp = 100
  >>> dave.get_kicked()
  The gelatinous cube dave has been slain.
"""


class GelCube:
  def __init__ (self, name, size = 1):
    self.hp = 999999999999999999999999999999
    self.size = size
    self.victims = []
    self.name = name
    self.absorbtion_times = []
  
  def take_damage(self, damage):
    self.hp -= damage
  
  def absorb(self, victim):
    if self.can_absorb():
      dt = datetime.now()
      self.victims.append(victim)
      self.absorbtion_times.append(dt.timestamp())
      print(f"The gelatinous cube {self.name} has absorbed {victim}.")
  def burn(self):
    for v in self.victims:
      victim.take_damage(v, 100)
  
  def get_kicked(self):
    for v in self.victims:
      self.hp -= 100
    if self.hp <= 0:
      self.die()
      
  def die(self):
    print(f"The gelatinous cube {self.name} has been slain.")
    del self
        
  def is_absorbed(self, victim):
    if victim in self.victims:
      return True
    else:
      return False
  
  def can_absorb(self):
    dt = datetime.now()
    if len (self.victims) < self.size:
      if len(self.absorbtion_times) >= 1:
        if dt.timestamp()-self.absorbtion_times[len(self.absorbtion_times)-1] >= 60:
          return True
        else:
          print("you must wait 1 minute between absorptions")
          return False
      else:
        return True
    else:
      print("you are full of people")
      



class victim:
  def __init__ (self, name):
    self.hp = 1200
    self.name = name

  def __str__(self):
      return str(self.name)
      
  def __repr__(self):
    return str(self.name)
  
  def take_damage(self, damage):
    self.hp -= damage


if __name__ == '__main__':
    import doctest
    doctest.testmod()

dave = GelCube("dave",2)
bob = victim("bob")
joe = victim("joe")
yn = "yes"
while yn == "yes":
  yn = input("Do you want to absorb someone: ")
  if yn == "yes" and not dave.is_absorbed(bob):
    dave.absorb(bob)
  else:
    dave.absorb(joe)