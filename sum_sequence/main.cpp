/*
https://www.codewars.com/kata/586f6741c66d18c22800010a

Your task is to make function, which returns the sum of a sequence of integers.
The sequence is defined by 3 non-negative values: begin, end, step.
If begin value is greater than the end, function should returns 0

Examples

sequenceSum (2,2,2); // => 2
sequenceSum (2,6,2); // => 12 -> 2 + 4 + 6
sequenceSum (1,5,1); // => 15 -> 1 + 2 + 3 + 4 + 5
sequenceSum (1,5,3); // => 5 -> 1 + 4
*/

#include <iostream>

int sequenceSum(int start, int end, int step)
{
    if (start > end)
    {
        return 0;
    }

    int sum = 0;
    for (int i = start; i <= end; i += step)
    {
        sum += i;
    }
    std::cout << sum << '\n';
    return sum;
}

int main()
{
    sequenceSum (2,2,2);
    sequenceSum (2,6,2);
    sequenceSum (1,5,1);
    sequenceSum (1,5,3);

    return 0;
}