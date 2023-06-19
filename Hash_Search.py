hash_table = [None] * 10
def hash_func(value):
    return len(value) % 10

def hash_coll(value):
    return 15 % len(value)

def insert (hash_table, value):
    hash_key = hash_func(value)
    if hash_table[hash_key] is None:
        hash_table[hash_key] = value
    else:
        hash_key = hash_coll(value)
        hash_table[hash_key] = value
    
def search(hash_table,value):
    res = hash_func(value)
    if hash_table[res] == value:
        return res
    else:
        res = hash_coll(value)
        return res

insert (hash_table, 'Bali')
insert (hash_table, 'Jawa Tengah')
insert (hash_table, 'Jawa Barat')
insert (hash_table, 'Jawa Timur')
insert (hash_table, 'Jakarta')
print (hash_table)

prov = 'Jawa Timur'
print (search(hash_table,prov))

# prov = 'Jawa Tengah'
# print (search(hash_table,prov), 'berada pada index ke', hash_coll(prov))