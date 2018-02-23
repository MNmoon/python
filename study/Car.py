#!/usr/bin/env python
# encoding: utf-8

class Car(object):
  def __init__(self,make,model,year):
    '''describe car attribute'''
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0 

  def get_describe_name(self):
    '''return info of car--usually use'''
    #print 'car name is ',self.make
    #print 'car type is ',self.model
    #print 'generate at ',self.year
    '''convert year to str and print'''
    print  str(self.year) + ' ' + self.make + ' ' + self.model

  def read_odometer(self):
    print 'This car has ' + str(self.odometer_reading) + ' ' + 'miles on it'

  def modify_odometer_reading(self,odometer_reading):
    self.odometer_reading = odometer_reading

  def incremetal_odometer(self,miles):
    '''update odometer_readings'''
    self.odometer_reading += miles

'''创建子类时，父类必须包含在当前文件中，且位于子类前面'''

class ElectricCar(Car):
  def __init__(self,make,model,year):
    #init father class
    super(ElectricCar,self).__init__(make,model,year)



if __name__ == '__main__':
  '''
  car = Car('audi','A4','20170731')
  car.get_describe_name()
  car.read_odometer()
  #use instance method to modify attribute
  car.odometer_reading = 13732
  car.read_odometer()

  #use class method to modify attribute
  car.modify_odometer_reading(22321)
  car.read_odometer() 

  #Use incremental methods to modify attribute
  car.incremetal_odometer(100)
  car.read_odometer() 
  '''
  Ecar = ElectricCar('audi','A4','20170731')
  Ecar.get_describe_name()
  
