#Name Kaisen
#Date January 7, 2022
#Title list2
#Description prints ages sorted by descending mark, name, and surname
'''
pseudocode
set lists of identities
sort descending mark with sorted function, with lambda key, set sort parameter to index #2 of tuple inside list, reverse it
sort name with sorted function
sort surname with sorted function, with lambda key, set sort parameter to index #1 of tuple inside list
'''

identities = [
    ('Joe','Smith','85'),('Bob','Smith','85'),('Tina','Gray','78'),('John','Kim','67'),('Lisa','Kim','67'),
    ('Chloe','Kim','67'),('Jack','Black','55'),('Laura','Hill','87'),('Tina','Turner','75'),('John','Turner','75'),
    ('Bob','Macgee','55'),('Nancy','Lady','67'),('Lilly','Smith','67')

]
descendsort = sorted(identities, key=lambda a: a[2], reverse=True)
print('--- Sorted by Descending Mark ---')
print(descendsort)

name = sorted(identities)
print('--- Sorted by Name ---')
print(name)

surname = sorted(identities, key=lambda a: a[1])
print('--- Sorted by Surname ---')
print(surname)


