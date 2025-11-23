"""
  >>> dave = GelCube(2)
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
  cannot absorb more victims
  >>> print(dave.victims)
  [bob, jerry]
  >>> print(dave.is_absorbed(jerry))
  True
  >>> dave.hp = 100
  >>> dave.get_kicked()
  The gelatinous blob dave has been slain.
"""


class GelCube:
  def __init__ (self, size = 1):
    self.hp = 999999999999999999999999999999
    self.size = size
    self.victims = []
  
  def take_damage(self, damage):
    self.hp -= damage
  
  def absorb(self, victim):
    if len (self.victims) < 2:
      self.victims.append(victim)
    else:
      print('cannot absorb more victims')
  def burn(self):
    for v in self.victims:
      victim.take_damage(v, 100)
  
#get_kicked: gets kicked for each character that has been absorbed
      
#die: deletes instance of gelatinous_blob and makes a print statement announcing it
      
#is_absorbed: checks if victim has been absorbed


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

