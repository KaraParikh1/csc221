"""
  >>> dave = GelCube(2)
  >>> print(dave.hp)
  999999999999999999999999999999
  >>> dave.take_damage(199)
  >>> print(dave.hp)
  999999999999999999999999999800
  >>> bob = victim(self,bob)
  >>> jerry = victim(self, jerry)
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
  >>> garry = victim(self,garry)
  >>> dave.absorb(garry)
  cannot absorb more victims
  >>> print(dave.victims)
  [bob, jerry]

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


class victim:
  def __init__ (self, name):
    self.hp = 1200
    self.name = self

  def __repr__(self):
      return self.name
  
  def take_damage(self, damage):
    self.hp -= damage


if __name__ == '__main__':
    import doctest
    doctest.testmod()

