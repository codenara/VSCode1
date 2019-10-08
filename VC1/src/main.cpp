// C++11 raw string literal

#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "c:\next\race\folder\test1.xlsx" << endl;
    cout << R"(c:\next\race\folder\test1.xlsx)" << endl;  // raw string literal
}