
from pprint import pprint
list_ = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]


pprint(list_)
