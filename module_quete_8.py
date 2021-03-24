###Square of a number
def square (number):
  return(number*number)

def cube (number):
  return(number**3)

def absoluteNumber(number):
  if number<0:
    return(number*(-1))
  else:
    return(number)

def factcotrail(number):
  factorial=1
  if number < 0:
    return("Sorry, factorial does not exist for negative numbers")
  elif number == 0:
    return("The factorial of 0 is 1")
  else:
    for i in range(1,number + 1):
       factorial = factorial*i²
    return("The factorial of",number,"is",factorial)


from collections import Counter
def modeFunction(liste):
  data = Counter(liste)
  allData=data.most_common()# Returns all unique items and their counts   
  theMode=data.most_common(1) # Returns the highest occurring item
  return("the moste seen data is ",theMode[0])


def avereage (liste):
  nombreElement=len(liste)
  totalListe=sum(liste)
  avg=sum(liste)/nombreElement
  return(avg)


def maximum(liste):
  return(max(liste))


def Minimum(liste):
  return(min(liste))