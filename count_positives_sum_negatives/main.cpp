/*
https://www.codewars.com/kata/576bb71bbbcf0951d5000044

Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
*/

#include <iostream>
#include <vector>

void printElem(std::vector<int> vec)
{
    for (int i : vec)
        std::cout << i << ' ';
    
    std::cout << '\n';
}

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if (input.empty())
        return {};

    int countPositives {};
    int sumNegatives {};

    for (int i : input)
    {
        i > 0 ? countPositives++ : sumNegatives += i; 
    }

    return { countPositives, sumNegatives };
}

int main()
{

    std::vector<int> r1 = countPositivesSumNegatives({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15}); // expected {10, -65}
    printElem(r1);

    std::vector<int> r2 = countPositivesSumNegatives({0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14}); // expected {8, -50}
    printElem(r2);

    std::vector<int> r3 = countPositivesSumNegatives({ }); // expected {}
    printElem(r3);

    return 0;
}