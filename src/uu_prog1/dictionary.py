
import random
import time
"""
    Dictionaries are mappings from a set of keys (of almost any type) to a set of values.
    Here, a dictionary from strings, to floating point numbers
    'pi' -> 3.141592653589793
    'e'  -> 2.718281828459045
    'r'  -> 1.0
    'x'  -> -5.0
    'y'  -> 7.5

    Remember, lists are mappings from positive integers [0, ..., len) to a set of values.
    [3.141592653589793, 2.718281828459045, 1.0, -5.0, 7.5]
    
    Here we need to remember / keep track of which number is stored in which position.
    We can solve this by storing two lists.
    keys = ['pi', 'e', 'r', 'x', 'y']
    values = [3.141592653589793, 2.718281828459045, 1.0, -5.0, 7.5]

    Now if we need to look up what the value of 'r' is, we just search the list of keys until we find
    the key 'r' and then inspect the value (1.0) in the same position in the value-list.

    This is a way of making a dictionary.

    Add values to the dictionary by appending them to the list (or replacing the value if it already exists)
    Retrieve values from the dictionary by searching the key-list for a matching key and read out the value.
"""

# A dictionary built with a list

def list_dict_find(lst, key):
    for i in range(len(lst)):
        (key_i, _) = lst[i]
        if key_i == key:
            return i
    return -1

def list_dict_contains(lst, key):
    return list_dict_find(lst, key) >= 0

def list_dict_set(lst, key, value):
    ind = list_dict_find(lst, key)
    if ind >= 0:
        lst[ind] = (key, value)
    else:
        lst.append((key, value))

def list_dict_get(lst, key):
    ind = list_dict_find(lst, key)
    if ind >= 0:
        return lst[ind][1]
    else:
        raise IndexError(f'Key {key} not in dictionary.')

def list_dict_create(keys, values):
    lst = []
    for i in range(len(keys)):
        list_dict_set(lst, keys[i], values[i])
    return lst


"""
    Unfortunately, this is often quite inefficiently. Every time we need to look-up from the
    dictionary or add a new key-value pair, we need to search a list. As this list grows,
    the time required for these searches grow accordingly.
    
    Fortunately, Python has built-in, efficient, dictionaries that don't become much slower
    as we add more elements. In fact they are approximately as fast with many elements as
    with few elements. They even have their own dedicated syntax in the language!
"""

# With built-in dictionary

def dict_contains(d, key):
    return key in d

def dict_set(d, key, value):
    d[key] = value

def dict_get(d, key):
    return d[key]

def dict_create(keys, values):
    # zip takes two lists and merges them into one
    # [x1, x2, x3] [y1, y2, y3] -> [(x1, y1), (x2, y2), (x3, y3)]
    return dict(zip(keys, values))

"""
    To gain some insight into how these efficient dictionaries can be implemented,
    we shall look at a simple but illustrative implementation that gives the basic idea.

    Instead of letting our keys and values be stored in a long unordered sequence, we
    make a clever little scheme: use a hash-table. A hash is an integer number that
    can be generated from values of any data-types. Typically we want some function
    hash(x) that maps values to almost random integers, such that even very similar values
    'abc' (6686104688033894741) and 'abd' (4929586095262690859) would map to very different values.

    Then we take that value, and (using the modulo operator %) map it back into the length a fixed size
    list: hash(key) % len(lst). Then we can store all the key-value pairs that fall into the same
    position in this fixed size list in an inner list. If the number of slots in the hash-table
    is large enough, on average, there will never be too many elements in each sub-list.

    Therefore we can obtain fast addition and look-ups.
"""

# With manually constructed hash-table

def hash_dict_contains(lst, key):
    h = hash(key) % len(lst)
    return list_dict_contains(lst[h], key)

def hash_dict_set(lst, key, value):
    h = hash(key) % len(lst)
    list_dict_set(lst[h], key, value)

def hash_dict_get(lst, key):
    h = hash(key) % len(lst)
    return list_dict_get(lst[h], key)

def hash_dict_create(slots, keys = None, values = None):
    lst = [[] for _ in range(slots)]
    if keys is not None:
        for i in range(len(keys)):
            hash_dict_set(lst, keys[i], values[i])
    return lst

# Other functions

def random_name():
    s = ''
    s += chr(random.randint(ord('A'), ord('Z')))

    first_len = random.randint(1, 9)

    for _ in range(first_len):
        s += chr(random.randint(ord('a'), ord('z')))

    s += ' '
    s += chr(random.randint(ord('A'), ord('Z')))

    second_len = random.randint(4, 11)

    for _ in range(second_len):
        s += chr(random.randint(ord('a'), ord('z')))
    
    return s

def random_license_plate():
    s = ''
    for _ in range(3):
        s += chr(random.randint(ord('a'), ord('z')))
    for _ in range(3):
        s += chr(random.randint(ord('0'), ord('0') + 9))
    return s

def generate_entries(n, d, add_func):
    for i in range(n):
        key = random_license_plate()
        value = random_name()

        add_func(d, key, value)

def part1():
    # Test input

    test_keys = ['abc123', 'def456', 'ghi789', 'jkl321', 'mno123', 'pqr765', 'stu457', 'vwx245', 'xyz984']
    test_values = ['Edgar Allan Poe', 'J.R.R. Tolkien', 'Nassim Taleb', 'Thomas Harris', 'Stephen King', 'George R.R. Martin', 'David Lynch', 'Stanley Kubrick', 'Ronnie James Dio']

    # Create dictionaries

    list_dict = list_dict_create(test_keys, test_values)
    py_dict = dict_create(test_keys, test_values)
    hash_dict = hash_dict_create(1024, test_keys, test_values)

    #Test code

    print(f'Look-up def456 from list_dict:     {list_dict_get(list_dict, "def456")}')
    print(f'Look-up def456 from built-in dict: {dict_get(py_dict, "def456")}')
    print(f'Look-up def456 from hash_dict:     {hash_dict_get(hash_dict, "def456")}')

    # Add another item

    list_dict_set(list_dict, 'adg147', 'Mick Jagger')
    dict_set(py_dict, 'adg147', 'Mick Jagger')
    hash_dict_set(hash_dict, 'adg147', 'Mick Jagger')

    print(f'Look-up adg147 from list_dict:     {list_dict_get(list_dict, "adg147")}')
    print(f'Look-up adg147 from built-in dict: {dict_get(py_dict, "adg147")}')
    print(f'Look-up adg147 from hash_dict:     {hash_dict_get(hash_dict, "adg147")}')

    random.seed(1000)

    print(random_license_plate())
    print(random_name())
    print(random_license_plate())
    print(random_name())

    random.seed(1000)

    print(random_license_plate())
    print(random_name())

    N = 20000
    random.seed(1000)
    first_time = time.time()
    generate_entries(N, list_dict, list_dict_set)
    second_time = time.time()

    print(f'Time elapsed: {second_time-first_time}')

    random.seed(1000)
    first_time = time.time()
    generate_entries(N, py_dict, dict_set)
    second_time = time.time()

    print(f'Time elapsed: {second_time-first_time}')

    random.seed(1000)
    first_time = time.time()
    generate_entries(N, hash_dict, hash_dict_set)
    second_time = time.time()

    print(f'Time elapsed: {second_time-first_time}')

def part2():
    d = {'abc123': 'Edgar Allan Poe', 'def456': 'J.R.R. Tolkien'}
    print(d)

    keys = list(d.keys())
    values = list(d.values())

    print(keys)
    print(values)

    for k, v in zip(d.keys(), d.values()):
        print(f'This is a key {k} and this is a value {v}.')

    print(f'Key abc123 in dictionary: {"abc123" in d}')
    print(f'Key cba321 in dictionary: {"cba321" in d}')

def part3():
    s = set(('abc123', 'def456', 'ghi789'))

    print(s)

    for key in s:
        print(key)

    if 'ghi789' in s:
        print('Key ghi789 is in s')
    if 'cba321' in s:
        print('Key cba321 is in s')

#part1()
#part2()
part3()
