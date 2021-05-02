# https://www.codewars.com/kata/520b9d2ad5c005041100000f

# Move the first letter of each word to the end of it, then add "ay" to the end
# of the word. Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldWay !


def pig_it(text):
    out = []
    for word in text.split():
        if word.isalpha():
            out.append(word[1:]+word[0]+'ay')
        else:
            out.append(word)

    return ' '.join(out)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
