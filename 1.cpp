#include <iostream>
using namespace std;

class Student
{
private:
    int marks;

public:
    void getMarks()
    {
        cout << "Enter marks: ";
        cin >> marks;
    }

    void checkResult()
    {
        if (marks >= 40)
        {
            cout << "Result: Pass" << endl;
        }
        else
        {
            cout << "Result: Fail" << endl;
        }
    }
};

int main()
{
    Student s;

    s.getMarks();
    s.checkResult();

    return 0;
}
