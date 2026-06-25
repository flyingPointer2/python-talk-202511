#include <iostream>

int main()
{
    int year = 2024;

    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
    {
        std::cout << year << " is a gap year." << std::endl;
    }
    else
    {
std::cout << year << " is NOT a gap year." << std::endl;        
    } // C++语言中 通过花括号{}确定层次结构 对缩进无强制要求 

    return 0;
}