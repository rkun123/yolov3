import time
from colored import fg, attr

class MeasureTime():
  def __init__(self, title = None):
    self.start = time.time()
    self.end = None
    self.title = title if title != None else ''
    self.info('start')
  
  def stop(self):
    self.end = time.time()
    self.print()
  
  def info(self, text):
    print('%s[INFO] %s: %s%s' % (fg(2), self.title, text, attr(0)))

  def error(self, text):
    print('%s[ERROR] %s: %s%s' % (fg(1), self.title, text, attr(0)))

  def print(self):
    if self.end == None:
      self.error("Stopped yet...")
      return
    
    seconds = self.end - self.start
    
    self.info(f'{round(seconds*1000 * 100) / 100}ms')