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

  def fill_gas_tank():
    """电动汽车没有油箱"""
    print("This car doesn't need a gas tank!")


