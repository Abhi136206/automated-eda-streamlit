#include <iostream>
using namespace std;

class employe
{
    int id;
    int salary;

public:
    void setid(void)
    {
        salary = 122;
        cout << "Enter the id of employe" << endl;
        cin >> id;
    }

    void getid(void)
    {
        cout << "The id of this employe is " << id << endl;
    }
};

int main()
{
    employe harry, rohan, sohan, mohan;
    //harry.setid();
    //harry.getid();
    employe fb[4];
    for (int i = 0; i < 4; i++)
    {
        fb[i].setid();
        fb[i].getid();
    }
    

    return 0;
}