                                                                     
                                                                     
                                                                     
                                             
# StateFile.py  (c) 2013 @whaleygeek

class StateFile(object):
  def trace(self, msg):
    pass # print msg
    
  def __init__(self, filename):
    self.filename = filename
    
  def write(self, map):
    self.trace("write")
    f = open(self.filename, "wt")
    for k in map:
      try:
        v = map[k]
      except IndexError:
        v = ""
      f.write(k + ":" + str(v) + "\n")
    f.close()
  
    
  def read(self):
    self.trace("read")
    try:
      f = open(self.filename, "rt")
    except IOError:
      return None
      
    map = {}
    for line in f:
      if (line == "\n"):
        break # end of map
      else:
        item = line.split(":", 2)
        try:
          key = item[0]
        except IndexError:
          f.close()
          return None # malformed record
        try:
          value = item[1]
          value = value.rstrip('\n').strip()
        except IndexError:
          value = None
        map[key] = value      
    f.close()
    return map
    
def test():
  s = StateFile("test_state.txt")
  m1 = {"id": 1, "name": "david", "age": 45, "test": True}
  s.write(m1)
  
  m2 = s.read()
  for k in m2:
    print k + "=" + m2[k]
    
if __name__ == "__main__":
  test()
  
# END

