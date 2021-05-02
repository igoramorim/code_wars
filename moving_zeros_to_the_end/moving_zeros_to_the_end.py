# https://www.codewars.com/kata/52597aa56021e91c93000cb0

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    for i in array:
        if i == 0:
            array.append(array.pop(array.index(i)))

    return array

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]