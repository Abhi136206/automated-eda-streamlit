#include <iostream>
using namespace std;

class Employe
{
    int id;
    static int count;

public:
    void setdata(void)
    {
        cout << "Enter the id" << endl;
        cin >> id;
        count++;
    }
    void getdata(void)
    {
        cout << "The id of this Employe is " << id << " and this is Employe number " << count << endl;
        cin >> id;
    }
    static void getcount(void)
    {
        cout << "The value of count is " << count << endl;
    }
};
int Employe ::count = 1000;

int main()
{
    Employe harry, rohan, sohan;
    // harry.id = 1;
    // harry.count = 1; //cannot do this as id and count are private

    harry.setdata();
    harry.getdata();
    Employe::getcount();

    rohan.setdata();
    rohan.getdata();
    Employe::getcount();

    sohan.setdata();
    sohan.getdata();
    Employe::getcount();

    return 0;
}