# Write a program that ocunts from 1 to 20 in fizzbuzz fashion.
# Loop from 1 to 20. Each time through, if number is divisible by 3, 
# say 'fizz'. If divisible by 5, say 'buzz'. If number is evenly
# divisibe by both 3 and 5, say 'fizzbuzz'. Otherwise, say number."""

# for numbers in range(20):

#   conditional that says, if divisible by 3:
#       print('fizz')
#   elif that says, if divisible by 5:
#       print('buzz')
#   elif that says, if divisible by 5 and divisible by 3:
#       print('fizzbuzz')

# def fizzbuzz():
#     for x in range(20):
#        if x / 3 != float(x):
#            print('fizz')
#        elif x / 5 != float(x):
#            print('buzz')
#        elif x / 5 and x / 3 != float(x):
#            print('fizzbuzz')
#    return none

def fizzbuzz():
    """ Count from 1 to 20 in fizzbuzz fashion."""
    for x in range(20):
        if x / 3 != float(x):
            print('fizz')
        elif x / 5 != float(x):
            print('buzz')
        elif x / 5 and x / 3 != float(x):
            print('fizzbuzz')
        else:
            return none