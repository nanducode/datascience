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
    key = record[1]
    newlist=[]	
    for x in record[2:]:
#	print x
	k=str(x)
#	print "after",k
	newlist.append(k)
#    print newlist	 
    if(record[0]=="order"):
      elements = ['order'] + newlist
    else:
      elements = ['line_item'] + newlist	
    mr.emit_intermediate(key, elements)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    order=0
    for v in list_of_values:
      if(v[0]=="order"):
        order=total	
      total += 1
    list_of_values[order].insert(1,str(key))
    for v in list_of_values:
	if(v[0]=="line_item"):
	 v.insert(1,str(key))
         new_list=list_of_values[order]+v
	 print new_list
	 mr.emit((new_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
