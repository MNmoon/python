class Restaurant():
  def __init__(self,restaurant_name,cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print 'restaurant name is:', self.restaurant_name
    print 'restaurant type is:', self.cuisine_type

  def open_restaurant(self):
    print self.restaurant_name,' is opening'

  def set_number_served(self,number_served):
    self.number_served += number_served
    print  str(self.number_served) +' ' + 'people have eat in this restaurant'
    

class IceCreamStand(object):
  flavors = []
  def __init__(self,flavors):
    self.flavors = flavors
    super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
'''
  def display_iceCream(self):
    for i in len(flavors[])
      print self.flavors[i]
'''




if __name__ == '__main__':
  '''
  restaurant = Restaurant('sam','west')
  restaurant.describe_restaurant()
  restaurant.open_restaurant()
  print restaurant.number_served
  restaurant.set_number_served(10)
  '''
  #ice = IceCreamStand('Queen','iceCream',[a,b,c,d])
  #ice.diplay_iceCream()
  
  
