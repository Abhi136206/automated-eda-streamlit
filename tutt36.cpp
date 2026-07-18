#include <iostream>
using namespace std;

class Employe
{
    int id;

public:
    float salary;
    Employe(int inpid)
    {
        id = inpid;  
        salary = 34.0;
    }
};

class programer : Employe
{
public:
    programer(int inpId)
    {
        id = inpid;
    }
    int language = 9;
    void getdata(){
        cout<<id<<endl;
    }
};

int main()
{
    Employe harry(1), rohan(2);
    cout << harry.salary << endl;
    cout << rohan.salary << endl;
    programer skillF(1);
    cout << skillF.languagecode;

    return 0;
}