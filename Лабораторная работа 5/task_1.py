from pprint import pprint


def dictionary(number):
    local_dict = {'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)}
    return local_dict


list_dict = [dictionary(i) for i in range(16)]
pprint(list_dict)
#end
