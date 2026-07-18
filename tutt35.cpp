#include<iostream>
using namespace std;

int count = 0;

class num{
    public:
    num(){
        count++;
        cout<<"This is the time when constructor is called for object number"<<count<<endl;
    }

    ~num(){
        cout<<"This is the time when destructor is called for objects number"<<count<<endl;
        count++;
    }
};

int main(){
    cout<<"we are inside our main function"<<endl;
    cout<<"ceating first object n1"<<endl;
    num n1;
    {
        cout<<"Entering this block"<<endl;
        cout<<"creating two or more objects"<<endl;
        num n2, n3;
        cout<<"exiting this block"<<endl;
    }
    cout<<"back to main"<<endl;

return 0;
}