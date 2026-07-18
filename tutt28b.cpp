#include<iostream>
using namespace std;

class c2;

class c1{
    int vall1;
    friend void exchange(c1 &, c2 &);
    public:
    void indata(int a){
        vall1 = a;
    }
    void display(void){
        cout<<vall1<<endl;
    }

};

class c2{
    int vall2;
    friend void exchange(c1 &, c2 &);
    public:
    void indata(int a){
        vall2 = a;
    }

    void display(void){
        cout<<vall2<<endl;
    }
};

void exchange(c1 &x, c2 &y){
     int tmp = x.vall1;
     x.vall1 = y.vall2;
     y.vall2 = tmp;
}

int main(){

    c1 oc1;
    c2 oc2;

    oc1.indata(34);
    oc2.indata(67);
    exchange(oc1, oc2);

    cout<<"The value of c1 after exchanging becomes :";
    oc1.display();
    cout<<"The value of c2 after exchanging becomes:";
    oc2.display();

return 0;
}