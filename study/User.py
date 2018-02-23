class User():
  def __init__(self,first_name,last_name,age,sex):
    '''describe car attribute'''
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.sex = sex
    self.login_attempts = 0

  def describe_user(self):
    '''print info of user'''
    print  self.first_name + ' ' + self.last_name + ' age is  ' + ' ' + self.age + ' and sex is ' + self.sex 

  def greet_user(self):
    if self.age < 18:
      print 'hello'
    if self.age < 18 and self.sex == 'women':
      print 'Welcome young girls'
    if self.age < 18 and self.sex == 'men':
      print 'Welcome young boys'

  def increment_login_attempts(self):
    self.login_attempts +=1
    print 'the vaule of login_attempts is ',self.login_attempts

  def reset_login_attempts(self):
    self.login_attempts = 0
    print 'the vaule of login_attempts is ',self.login_attempts

if __name__ == '__main__':

  user = User('zhang','yanxi','1','men')
  user.describe_user()
  user.greet_user()
  user.increment_login_attempts()
  user.increment_login_attempts()
  user.increment_login_attempts()
  user.reset_login_attempts()
  
