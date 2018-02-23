#!/usr/bin/env python
# encoding: utf-8

from car import Car

'''describe electric car battery'''
class Battery(object):
  def __init__(self,battery_size=70):
    self.battery_size = battery_size

  def describe_battery_size(self):
    #describe the info of battery
    print("This car has a " + str(self.battery_size) + "-kwh battery.")
  
  def get_range(self):
    if self.battery_size ==70:
      range = 240
    elif self.battery_size ==85:
      range = 270
    print 'This car can go about ' + str(range) + ' miles'

  def update_battery(self):
    if self.battery_size !=85:
      self.battery_size = 85


'''创建子类时，父类必须包含在当前文件中，且位于子类前面'''
class ElectricCar(Car):
  def __init__(self,make,model,year):
    #init father class
    super(ElectricCar,self).__init__(make,model,year)
    self.battery = Battery()

  def get_describe_name(self):
      print self.make + ' '+ self.model + ' make at ' + self.year


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
  #Ecar.describe_battery_size()
  Ecar.battery.describe_battery_size()
  Ecar.battery.update_battery()
  Ecar.battery.get_range()
  
  
