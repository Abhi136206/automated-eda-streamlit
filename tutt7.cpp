#include<iostream>
using namespace std;

int main()
{ int bill, d=0,ab;

cout<<"enter the bill amount";
cin>>bill;
if(bill>1000)
d=10;
ab=bill-bill*d/100;
cout<<ab;
return 0;
}