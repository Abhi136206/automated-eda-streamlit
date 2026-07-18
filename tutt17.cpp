#include<iostream>
using namespace std;

int product(int a, int b){
    return a*b;
}
float moneyRecevied(int currentmoney, float factor=1.04){
    return currentmoney *factor;
}

int main(){

    int a, b;
    //cout<<"Enter the value of a and b"<<endl;
    //cin>>a>>b;
    //cout<<"The product of a and b is "<<product(a,b);
    int money = 100000;
    cout<<"if you have"<<money<<" Rs in your bank account, you will recive "<<moneyRecevied(money)<<"Rs after 1 year";
    cout<<"for VIP: if you have "<<money<<" Rs in your bank account, you will recive "<<moneyRecevied(money, 1.1)<<"Rs after 1 year";

return 0;
}