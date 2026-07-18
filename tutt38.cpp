#include<iostream>
using namespace std;

class counter{ 
    private:
    int count;
    public:
    counter()
    {count = 0;}
    counter ( int c)
    {count = c;}
    counter operator++()
    {return counter (++count)
    }
counter operator++(int)
{return counter (count++);
}
int getcount()
{return cout ;}};


int main(){

return 0;
}