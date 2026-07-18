#include<iostream>
using namespace std;


struct employe;
{
    /* data */
    int eId;
    char favchar;
    float salary;
};

int main(){
    struct employe harry;
    harry.eId = 1;
    harry.favchar = 'c';
    harry.salary = 1200000;
    cout<<harry.salary;  
return 0;
}