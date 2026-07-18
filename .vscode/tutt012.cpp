#include<iostream>
using namespace std;

int main(){
    // what is a pointer?---> data type which holdsthe adress of other data types

    int a=3;
    int* b = &a;
    // &---> (adress of) operator
    cout<<"The address of a is "<<&a<<endl;
    cout<<"The address of a is "<<b<<endl;

//*--->(value at) dereference operator
    cout<<"The value of address of a is "<<*b<<endl;

    //pointer to pointer
    int**c = &b;
    cout<<"The address of b is "<<&b<<endl;
    cout<<"The address of b is "<<c<<endl;
    cout<<"The value at address c is "<<*c<<endl;
    cout<<"The value at address value_at(value_at(c)) is "<<**c<<endl;

return 0;
}