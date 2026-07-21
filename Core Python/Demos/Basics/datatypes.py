### Numeric Category
#1.int 
var = 10

#2.float
var = 10.5

#3.complex
var = 10 + 5j # Real part = 10, Imaginary part = 5j

print(type(var))

###Text
#1. str
var = 'First"bit Solutions'
var = "Firstbit's Solutions"
var = '''This is first line.
This is second line.'''

var = """This is first line.
This is second line."""

print(type(var))

#### Sequentil type
#1. list
var = [10, 20, 30, 40, 50]

#2. tuple
var = (10, 20, 30, 40, 50)
var = 10, 20, 30, 40, 50 #tuple 

#3. range
var = range(10,10000000)

### Set Type
#1. set
var = {10, 20, 30, 40, 50}

#2. frozenset
var = frozenset({10, 20, 30, 40, 50})

#### Mapping Type
#1. dict  
var = {'id': 101, 'name': 'Pratik', 'address': 'Bangalore'}

###other types
#1. bool
var = True

#2. nonetype
var = None

print(type(var))
