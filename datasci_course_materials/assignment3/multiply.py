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
    key=""
    val=[]
    if(record[0]=="a"):
     key = record[1]
     val=[]
     val.append("a")
     val.append(record[2])
     val.append(record[3])
     for i in range(0,5):
      newkey=""
      newkey=str(key) + "c" + str(i)
      #newkey.append(key)
      #newkey.append(i)
      mr.emit_intermediate(newkey, val)
    if(record[0]=="b"):
     key = record[2]
     val=[]
     val.append("b")
     val.append(record[1])
     val.append(record[3])
     for i in range(0,5):
      newkey=""
      newkey=str(i)+"c"+str(key)
      #newkey.append(key)
      #newkey.append(i)
      #print "key",key,i,newkey,val
      mr.emit_intermediate(newkey, val)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mykeys=key.split("c")
    total=0
    for v in list_of_values:
     for k in list_of_values:
      if(v[0] == "a"):
       if(v[0] != k[0]):
        if(v[1] == k[1]):
         #print key,v[2],k[2]
         total += v[2] * k[2]
    mr.emit((int(mykeys[0]),int(mykeys[1]),total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
