#include<iostream>
using namespace std;

int main(){
    int a, b, carry;
    cout<<"enter two number:";
    cin>>a>>b;
    while(b!=o)
    
    {
        carry = (a&b)<<1;
        a = (a^b);
        b = carry;

    }
     cout<<a;

return 0;
}