#include<iostream>
using namespace std;

class{
    int a;
    public:
    number(){
        a = 0;
    }
    number(int num){
        a = num;
    }

    number(number &obj){
        cout<<"copy constructor called!!!"<<endl;
        a = obj.a;
    }
    void display(){
        cout<<"The number for this object is "<< a <<endl;
        a = obj.a;
    }
};

int main(){
    number x, y, z(45);
    x.display();
    y.display();
    z.display();

return 0;
}