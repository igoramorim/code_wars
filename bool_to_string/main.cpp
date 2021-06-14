/*
https://www.codewars.com/kata/551b4501ac0447318f0009cd

Implement a function which convert the given boolean value into its string representation.
Note: Only valid inputs will be given.
*/


#include <iostream>
#include <string>

std::string boolean_to_string(bool b){
  return b ? "true" : "false";
}

int main()
{
    std::cout << boolean_to_string(true) << '\n';
    std::cout << boolean_to_string(false) << '\n';
    return 0;
}