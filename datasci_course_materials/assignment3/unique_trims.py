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
    if(record[0]=="a"):
     key = record[1]
    if(record[0]=="b"):
     key = record[2]
    val=[]
    val.append(record[0])
    val.append(record[3])
    mr.emit_intermediate(key, val)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for v in list_of_values:
     for k in list_of_values:
      if(v[0] != k[0]):
       total += v[1] * k[1]
     mr.emit(())

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
