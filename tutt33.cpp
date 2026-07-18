#include<iostream>
using namespace std;

class Bankdeposit{
    int principal;
    int years;
    float interestRate;
    float returnvalue;

    public:
        Bankdeposit{}{}
        Bankdeposit (int p, int y, float r);
        Bankdeposit (int p, int y, int r);
};
 void Bankdeposit :: Bankdeposit(int p, int y, float r)
 {
    principal = p;
    years = y;
    Interestrate = r;
    returnvalue = 0;
    for (int i = 0; i < y; i++)
    {
        returnvalue = returnvalue * (1+r);
    }
 }

 void Bankdeposit :: Bankdeposit(int p, int y, float r)
 {
    principal = p;
    years = y;
    Interestrate = float(r)/100;
    returnvalue = principal;
    for (int i = 0; i < y; i++)
    {
        returnvalue = returnvalue * (1+r);
    }
 }
 
 Bankdeposit :: show(){
    cout<<endl<<"principal amount was "<<principal<<"Return value after "<<years <<"is"<<returnvalue<<endl;
 }

int main(){
    Bankdeposit bd1, bd2, bd3;
    int p, y;
    float r;
    int R;

    cout<<"Enter the value of p y and r"<<endl;
    cin>>p>>y>>r;
    bd1 = Bankdeposit(p, y, r);
    bd1.show();

    cout<<"Enter the value of p y and r "<<endl;
    cin>>p>>y>>r;
    bd2 = Bankdeposit(p, y, r);
    bd2.show();

return 0;
}