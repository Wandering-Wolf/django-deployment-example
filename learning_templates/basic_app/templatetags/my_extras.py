from django import template

register = template.Library()

def cutting(value, arg): #cut (used in video example) is already there in the documentation example
    """
    Removes all instances of 'arg' from the string
    """#documentaion not actually needed

    return value.replace(arg,'')

#registering
register.filter('cutting',cutting) #first parameter is what name you're going to use to call the custom filter (ie, what we call the filter)
                           #second parameter is a function itself
