import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    vallist = []
    vallist.append(1)
    vallist.append(key)
    vallist.append(value)
    newkey=""
    if(key > value):
     newkey=key+value
    else:
     newkey=value+key 
    #print key, value, newkey
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(newkey, vallist)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    friend1=""
    friend2=""
    for v in list_of_values:
      total += v[0]
      friend1=v[1]
      friend2=v[2]
    if(total == 1):
     mr.emit((friend1, friend2))
     mr.emit((friend2, friend1))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
