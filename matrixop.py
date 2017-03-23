def getZeroRowMatrix(n) :
      l = []
      i=0 
      while(i<n) :
          l.append(float(0))
          i+=1
      return l

def matrixTrans(a) :
      res = []
      m = len(a[0])
      n = len(a)
      i = 0
      while i < m :
          res.append(getZeroRowMatrix(n))
          i+=1
      i=0;j=0
      while i < n :
          j = 0
          while j<m :
              res[j][i] = a[i][j]
              j+=1
          i+=1

      return res 

def matrixMul(a,b):
     m = len(a)
     n = len(a[0])
     n1 =len(b)
     l = len(b[0])
     res = []
     if  n1 != n :
        return res
     else :
        i = 0
        while i < m :
            res.append(getZeroRowMatrix(l))
            i+=1
    
        i = 0
        j = 0
        k = 0
        while(i<m) :
            sum1 = float(0) 
            j = 0
            while(j<l) :
               k = 0
               sum1 = float(0)
               while(k<n) :
                  sum1+=a[i][k]*b[k][j]
                  k+=1
               res[i][j] = sum1 
               j+=1
            i+=1    
        return res


