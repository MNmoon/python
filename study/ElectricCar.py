
class ElectricCar():
  def __init__(self,make,model,year):
    '''init father class'''
    super().__init__(make,model,year)

  

if __name__ == '__main__':

  Ecar = ElectricCar('audi','A4','20170731')
  print Ecar.get_describe_name()

  
