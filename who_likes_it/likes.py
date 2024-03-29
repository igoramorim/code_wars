# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

# You probably know the "like" system from Facebook and other pages. People can
# "like" blog posts, pictures or other items. We want to create the text that
# should be displayed next to such an item.
#
# Implement a function likes :: [String] -> String, which must take in input array,
# containing the names of people who like an item. It must return the display text
# as shown in the examples:
#
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

def likes(names):
    prefix = ''

    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    elif len(names) >= 4:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)


print(likes([]))
print(likes(['igor']))
print(likes(['igor', 'joao']))
print(likes(['igor', 'joao', 'maria']))
print(likes(['igor', 'joao', 'maria', 'miriam']))
print(likes(['igor', 'joao', 'maria', 'miriam', 'beto', 'jose', 'durval']))
