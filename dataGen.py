import csv

def getZeroRowMatrix(n) :
      l = []
      i=0 
      while(i<n) :
          l.append(float(0))
          i+=1
      return l




file1 = open('u1.base','r') #file to read train data
file2 = open('u1.test','r') #file to red test data
file3 = open('u.item','r') #file to read movie names

people = [] # to store people
rating_matrix = [] # to store matix i.e rating matrix
movie = {} # to store movie 



count = 0

reader = csv.reader(file3,delimiter='|')

#load all the movie id and its names 
for row in reader :
     l = row
     movie[int(l[0])] =l[1]
     count+=1


N = count #num of movies 


reader = csv.reader(file1,delimiter='	')

for row in reader :
      l = row
      if l[0] not in people : 
              people.append(l[0])
              mat = getZeroRowMatrix(N)
              rating_matrix.append(mat)
      rating_matrix[int(l[0])-1][int(l[1])-1] = float(l[2])
       
#print rating_matrix[0]       

#print "no of movies :",N
