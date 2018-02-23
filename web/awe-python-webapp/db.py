#create db engine
class Engine(object):
  def __init__(self,connect):
    self.connect = connect
  def connect(self):
    return self._connect()

engine =  None

#持有数据库连接的上下文对象
class _DbCtx(threading.local):
  def __init_(self):
    self.connection = none
    self.transactions = 0 

  def is_init(self):
    return not self.connetion is None

  def init(self):
    self.connection = _LasyConnection()
    self.transactions = 0 

  def cleanup(self):
    self.connection.cleanup()
    self.connection = None

  def cursor(self):
    return self.connection.cursor()

_db_ctx = _DbCtx

#定义了__enter__()和__exit__()的对象可以用于with语句，确保任何情况下__exit__()方法可以被调用
class _ConnercionCtx(object):
  def __enter__(self):
    global _db_ctx
    self.should_cleanup = False
    if not _db_ctx.is_init():
      _db_ctx.init()
      self.should_cleanup =  True
    return self

  def __exit__(self,exctype,excvalue,ttraceback):
    global _db_ctx
    if self.should_cleanup:
      _db_ctx.cleanup()

  def connection():
    return _ConnectionCtx()

#注意到Connection对象是存储在_DbCtx这个threadlocal对象里的，因此，嵌套使用with connection()也没有问题。_DbCtx永远检测当前是否已存在Connection，如果存在，直接使用，如果不存在，则打开一个新的Connection

@with_connection
def select(sql, *args):
    pass

@with_connection
def update(sql, *args):
    pass









