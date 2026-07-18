#include <iostream>
using namespace std;

// forward declaration
class complex;

class calculator
{
public:
    int add(int a, int b)
    {
        return (a + b);
    }
    int sumRealcomplex(complex, coomplex);  
};

class complex
{
    int a, b;
    friend int calculator ::sumRealcomplex(complex, complex);

public:
    void setnumber(int n1, int n2)
    {
        a = n1;
        b = n2;
    }

    void printnumber()
    {
        cout << "Your number is " << a << "+ " << b << "i" << endl;
    }
};

int main()
{
    complex o1, o2;
    o1.setnumber(1, 4);
    o2.setnumber(5, 7);
    calculator calc;
    int res = calc.sumRealcomplex(o1, o2);
    cout << "The sum of real part of o1 and o2 is " << res << endl;

    return 0;
}