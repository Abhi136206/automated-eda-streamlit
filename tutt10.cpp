#include<iostream>

using namespace std;

int main(){
    //cout<<"This is tutoraial 9";
    int age;
    cout<<"Tell me your age"<<endl;
    cin>>age;
    if((age<18) && (age>0)){
        cout<<"You cam not come to my party"<<endl;
    }
    else if(age==18){
        cout<<"You are a kid and you will get a kis pass to the party"<<endl;
    }
    else if(age<1){
        cout<<"You are not yet to born"<<endl;
    }

    return 0;
}