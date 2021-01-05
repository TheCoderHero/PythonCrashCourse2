# Import functions from other files that are located in the same directory
import pizza
# This allows you to use the functions like make best pizza
pizza.make_best_pizza('small', 'pep', 'mush')

# Import Specific Functions
from pizza import make_best_pizza

# import multiple functions by separating them with a comma
# from pizza import make_best_pizza, pizza_inventory, shipped_toppings, received_toppings

# using as to give a function an alias
# from pizza import make_best_pizza as mbp
# from module_name import function_name as alias

# Using as to give a module an alias
# import pizza as p
# import module_name as alias

# Import all functions from a module
# from pizza import *
# no need to use module name when calling function
# pizza.make_best_pizza VS make_best_pizza

