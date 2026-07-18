#include<iostream>

using namespace std;

int c = 45;

int main(){
    int a, b, c;
    float d = 34.4;
    // ***********Build in data types***********
    //cout<<"Enter the value of a:"<<endl;
    //cin>>a;
    // cout<<"Enter the value of b:"<<endl;
    // cin>>b;

    //cout<<"The sum is "<<c<<endl;
    //cout<<"The global c is "<<::c;

    // ***********float, double and long double literals***********
    // float d = 34.4f;
   // long double e = 34.4;
   // cout<<"The size of 34.4 is "<<sizeof(34.4)<<endl;
    //cout<<"The size of 34.4f is "<<sizeof(34.4f)<<endl;
    //cout<<"The size of 34.4F is "<<sizeof(34.4F)<<endl;
    //cout<<"The size of 34.4l is "<<sizeof(34.4l)<<endl;
    //cout<<"The size of 34.4L is "<<sizeof(34.4L)<<endl; 

     // ***********Reference variables***********
     // Rphan das ---> Monty ----> rohu -----> Dangerous coder  
    // float x = 455;
    // float & y = x;
    // cout<<x<<endl;
     //cout<<y<<endl; 
     int a = 45;
     float b = 45.46;
     cout<<"The value of a is "<<(float)a<<endl;
     cout<<"The value of a is "<<float(a)<<endl;

     cout<<"The value of b is "<<(int)b;
     cout<<"The value of b is "<<int(b);   
     int c = int(b);
     


    return 0;
}