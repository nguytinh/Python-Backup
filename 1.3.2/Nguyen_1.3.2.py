def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
    

def hyp(leg1,leg2):
    '''returns the length of the hypotenuse'''
    return ((leg1**2 + leg2**2)**0.5)
    
    
def mean(a,b,c):
    '''Finds the mean of 3 numbers'''
    return ((a+b+c)/3.0)
    
def perimeter(base,height):
    '''Finds the perimeter in a quadrilateral''' 
    return (base*2 + height*2)
    
#1.3.2 Function Test    
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)    