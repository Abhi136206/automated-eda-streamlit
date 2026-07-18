#include<iostream>
using namespace std;
int sum(int a, int b){
    int c = a + b;
    return c;
}
void swapreferencevar(int &a, int &b){    
      int temp = a;
      a  = b;
      b = temp;
}     

int main(){
    int x = 4, y = 5;
    //cout<<"The sum of 4 and 5 is "<<sum(a,b);
    cout<<"The value of x is "<<x<<" and the value of y is "<<y<<endl;
    //swap(x,y) This  will not swap a and b
    //swappointer(&x,&b);//This will swap a and b using pointer reference
    swapreferencevar(x, y);//This will swap a and b using reference variables
    cout<<"The value of x is "<<x<<" and the value of is "<<y<<endl;

return 0;
}