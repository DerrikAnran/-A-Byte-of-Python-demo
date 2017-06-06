#!/usr/bin/python
#Filename:using_dict.py
#'ab' is short for 'a'ddress 'b'ook
ab = {  'Swaroop':'swaroopch@byteofpython.info',
        'Larry':'larry@wall.org',
        'Matsumoto':'matz@ruby-lang.org',
        'Spammer':'spammer@hotmail.com'
    }
print"Swaroop's address is %s"%ab['Swaroop']
#adding a key/value pair
ab['Guido'] = 'guido@python.org'
#Deleting a key/value pair
del ab['Larry']
print'\nThere are %d contacts in the address-book\n'%len(ab)
for i,j in ab.items():
    print'Contact %s at %s'%(i,j)
if 'Guido' in ab:#OR ab.has_key('Guido')
    print"\nGuido's address is %s"%ab['Guido']
