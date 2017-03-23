from dataGen import rating_matrix,people,movie
from matrixop import matrixTrans,matrixMul,getZeroRowMatrix
from scipy import matmul
from scipy import linalg
from math import sqrt

#for svd we genatare matrix matix(m) = u*sigma*vt
#here sigma = comm_mat in this program
#here vt transpose of v matrix
#her ut = transpose of u matrix

print"wait for 1.5 min "
#scan the person id to recommend :
'''print"enter person id "
per_id = raw_input()
if per_id not in people :
     print" invalid id"
     exit()
'''
mat = rating_matrix #obtain rating matrix

tran = matrixTrans(mat) # find transpose of rating matrix 

# prerequisite for finding matrix u and vt
u_pre = matmul(mat,tran)
vt_pre = matmul(tran,mat)

#finding eigen values and eigen vecotor for the corresponding prerequisite matrix
vt_eigenval,vt_eigenvect = linalg.eig(vt_pre)
u_eigenval,u_eigenvect = linalg.eig(u_pre)

l = [] #temporary variable

#find round off eigen values of vt
for x in vt_eigenval :
    l.append(round(x.real,3))

vt_eigenval = l #store round off values of vt   
l = []

#find round off eigen values of u
for x in u_eigenval :
    l.append(round(x.real,3))

u_eigenval = l  #store round off values of u  
l = []

#find round off values of eigen vector of u
for x in u_eigenvect :
   z = []
   for y in x :
     z.append(round(y.real,3))
   l.append(z)

u_eigenvect = l #store round off eigen vector of u
l=[]

#find round off values of eigen vector of vt
for x in vt_eigenvect :
   z = []
   for y in x :
     z.append(round(y.real,3))
   l.append(z)

vt_eigenvect = l #store round off eigen vector of vt
l = []

# find transpose of eigen vectors to alling the values properly for v, vt matrix
v_eigenvect = vt_eigenvect 
vt_eigenvect = matrixTrans(vt_eigenvect)

# find transpose of eigen vectors to alling the values properly for u, ut matrix
ut_eigenvect = u_eigenvect
u_eigenvect = matrixTrans(u_eigenvect)


common = [] # list to sore common eigen values of intially found vt and u

#find commnon values and add it to common list
for x in u_eigenval :
   if x in vt_eigenval :
       common.append(x)

l = [] # temporary varialbe to find store non negative element

#store all non zero and positive values of common and add it to list
for x in common :
    if not x<=0 :
      l.append(x)

common = l #storing positive values

l.sort() # l is pointing to common and sort the values 

mimize_common = [] #list to store only higher values contibute 90% of total sum of common
total = sum(common) #find total sum of common 
threshold = 0.1*total # threshold value = 10% of total
sum1 = 0.0 #to store sum of values to eliminate threshold
i =0 

#find the index to which threshold counts i.e we are reducing the less important dimension
while(i<len(l)) :
     sum1+=l[i]
     if sum1 > threshold :
         break
     i+=1

minimize = l[i:] # store all the elements from threshold
common = minimize # minimized common values

#this part : store minimized values in descending order "
minimize = []
i = len(common) -1 #last index

while i>=0 :
  minimize.append(common[i])
  i-=1

common = minimize 

#end of this part : 

#temporary varialbes
l  = [] #to store eigen vectors of u coresponting to common
v  = [] #to store eigen values of u coresponting to common
l1 = [] #to store eigen vectors of vt coresponting to common
v1 = [] #to store eigen values of vt coresponting to common

#find all the eigen values and vector of u and vt
for x in common :
     l.append(u_eigenvect[u_eigenval.index(x)])
     v.append(x)
     l1.append(vt_eigenvect[vt_eigenval.index(x)])
     v1.append(x)

#storing values to actual variable
u_eigenvect = l 
vt_eigenvect = l1
u_eigenval =v
vt_eigenval = v1

#find agian the transpose of the matrix as per the definition
ut_eigenvect = u_eigenvect
u_eigenvect = matrixTrans(u_eigenvect)
v_eigenvect = matrixTrans(vt_eigenvect) 
#now genetare matrix sigma here comm_mat is used

i = 0
comm_mat =[] #store sigma matrix

#genetaige diagonal matrix 
for x in common :
     comm_mat.append(getZeroRowMatrix(len(common)))
     comm_mat[i][i] =sqrt(common[i]) #as per the definition of svd
     i+=1
#sigma matrix genrated i.e comm_mat

#now we have found all the  matrix of svd with reduction in dimentionality
#i.e u matix , sigmma(commo_mat) matrix, vt matrix

print u_eigenvect
print coom_mat
print vt_eigenvect



#personid = int(per_id) -1 #integer value of person id and convert to index

'''
#to predict movies for the person get movive rating matrix row of that person

pers_row = mat[personid] #person row from rating matrix

movie_class_matrix = matmul(pers_row,v_eigenvect) #find person intrest in classied movies as per definition

all_movie_rating =matmul(movie_class_matrix,vt_eigenvect) #find person rating of all movies 

movie_recom_lis = [] #variable to store recomended movie list

l = []  #variable stores absolute value of rating

for x in all_movie_rating :
     l.append(abs(x))

max_rating = max(l) #find maximum rating 

#ped = 0.8*max_rating  #find threshold rating

#find the all the movies having rating greater than threshold and not watched
i =0
while(i<len(l)):
  if l[i] >0.9 and pers_row[i] == 0:
     movie_recom_lis.append(movie[i+1])
  i+=1

#print recommended movies
for x in movie_recom_lis :
   print x

#total movies recommended 
print len(movie_recom_lis)
'''
