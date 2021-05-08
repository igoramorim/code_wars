// https://www.codewars.com/kata/57f780909f7e8e3183000078
// Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
// [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

#include <iostream>
#include <vector>
#include <numeric>

int grow(std::vector<int> nums)
{
    int res = 1;
    for (int i = 0; i < nums.size(); i++)
    {
        std::cout << "[i]" << i << " - " << nums[i] << "\n";
        res *= nums[i];
    }
    return res;

    // better solution
    // return std::accumulate(nums.begin(), nums.end(), 1, std::multiplies<>());
}

int main()
{
    std::cout << grow(std::vector<int>{1, 2, 3, 4});
    return 0;
}