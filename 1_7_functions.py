def sayOuch(num_times):
    """This function says OUCH! the given number of times
    """
    for i in range(0, num_times):
        print "OUCH!!"

sayOuch(3)

def sayOuch(num_times=1):
    """This function says OUCH! the given number of times
    """
    for i in range(0, num_times):
        print "OUCH!!"

sayOuch()
