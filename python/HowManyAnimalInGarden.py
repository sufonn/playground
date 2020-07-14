""" Question ::
In a garden, have birds and dogs.
The head count of the two species together is 12, and the leg count is 32. 
How many birds and how many dogs are there in the garden? """

import sys

def countAnimal(heads, legs):
    """ each bird has 2 legs, and each dog has 4 legs.
        1) bird + dog = heads
        2) 2bird + 4dog = leg

        ...
        bird = heads - dog
        2(heads - dog) + 4dog = legs
        2heads - 2dog + 4dog = legs
            >> dog = (legs - 2heads) / 2
    """
    print("----------")
    dog = (legs - (2 * heads)) / 2
    print("Dogs: ", dog)

    bird = heads - dog
    print("Birds: ", bird)
    print("----------")

try:
    head = int(input("Enter Head: "))
    leg = int(input("Enter Leg: "))
    countAnimal(head, leg)
except:
    print("Oops!", sys.exc_info()[0])