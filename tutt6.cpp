
// There are two types of header files:
// 1. System header files: It comes with compiler 
#include<iostream>
// 2. User defined header files: It is writen by the programmer
// #include "this.h"  //--> this will produce an error if this.h is no present in the current directory

#include"this.h"

using namespace std;

int main(){
    int a=4, b=5;
cout<<"This is hello world program:"<<endl;
cout<<"Followings are the types of operators in c++"<<endl;
//Arithmatic operators
cout<<"the value of a + b is"<<a+b<<endl;
cout<<"the value of a - b is"<<a-b<<endl;
cout<<"the value of a * b is"<<a*b<<endl;
cout<<"the value of a / b is"<<a/b<<endl;
cout<<"the value of a % b is"<<a%b<<endl;
cout<<"the value of a++ is"<<a++<<endl;
cout<<"the value of a-- is"<<a--<<endl;
cout<<"the value of ++a is "<<++a<<endl;
cout<<"the value of --a is "<<--a<<endl;
cout<<endl;

//Assignment operators --> used to assign values to variables
// int a =3, b =9;
//char d ='d';

// comparison operators
cout<<"Following are the types of comparison operators in c++"<<endl; 
cout<<"The value of a == b is "<<(a==b)<<endl;
cout<<"The value of a != b is "<<(a!=b)<<endl;
cout<<"The value of a >= b is "<<(a>=b)<<endl;
cout<<"The value of a <= b is "<<(a<=b)<<endl;
cout<<"The value of a > b is "<<(a>b)<<endl;
cout<<"The value of a < b is "(a<b)<<endl;

return 0;
} 