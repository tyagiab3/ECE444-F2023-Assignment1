class utils:
  def reversed(number):
    if num < 0:
        sign = -1
        num = abs(num)
    else:
        sign = 1
      
    revNumString = str(number)[::-1]
    revNum = int(revNumString)
    revNum *= sign
    
    return revNum

  
  def formatter(number):
    binaryNumber = bin(number)
    octalNumber = oct(number)
    
    return binaryNumber, octalNumber
