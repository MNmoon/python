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
    


class Car():
  def __init__(self,make,model,year):
    '''describe car attribute'''
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0 

  def get_describe_name(self):
    '''return info of car--usually use'''
    print 'car name is ',self.make
    print 'car type is ',self.model
    print 'generate at ',self.year
    '''convert year to str and print'''
    print  str(self.year) + ' ' + self.make + ' ' + self.model

  def read_odometer(self):
    print 'This car has ' + str(self.odometer_reading) + ' ' + 'miles on it'

  def modify_odometer_reading(self,odometer_reading):
    self.odometer_reading = odometer_reading

  def incremetal_odometer(self,miles):
    '''update odometer_readings'''
    self.odometer_reading += miles


if __name__ == '__main__':
  '''
  restaurant = Restaurant('sam','west')
  restaurant.describe_restaurant()
  restaurant.open_restaurant()
  print restaurant.number_served
  restaurant.set_number_served(10)
  '''
  car = Car('audi','A4','20170731')
  car.get_describe_name()
  car.read_odometer()
  '''use instance method to modify attribute '''
  car.odometer_reading = 13732
  car.read_odometer()

  '''use class method to modify attribute'''
  car.modify_odometer_reading(22321)
  car.read_odometer() 

  '''Use incremental methods to modify attribute'''
  car.incremetal_odometer(100)
  car.read_odometer() 
  
  
