/*
real programer mindset
if you can't fix a bug make it a feature 
*/
#include <iostream>
#include <list>
#include <string>
using namespace std;

int main(){
    int i = 1;
    char op1;
    list<string> task;
    char op;
    string task2;
    while (true){
    
    cout<<"enter your option"<<endl;
    cout<<"add task(1)"<<endl;
    cout<<"remove task(2)"<<endl;
    cout<<"done task(3)"<<endl;
    cout<<"view task(4)"<<endl;
    cin>>op;
    switch (op)
    {
    case '1':
        cout<<"enter task"<<endl;
        cin>>task2;
        task.push_front(task2);
        break;
    case '2':
        cout<<"enter task"<<endl;
        cin>>task2;
        task.remove(task2);
        break;
    case '3':
        cout<<"enter task"<<endl;
        cin>>task2;
        task.remove(task2);
        break;
    case '4':
        for (const auto& t : task) {
            cout << t << endl;
        }
        break;

    default:
        cout<<"opps someing went wrong try again"<<endl;
        break;

    }
    if (op != '4'){
        cout<<"now you have to do "<<endl;
        for (const auto& t : task) {
            cout << t << endl;
        }
        cout<<endl;
    }
    if (i > 3){
        cout<<"do you want to contenue"<<endl;
        cin>>op1;
        if (op1 == 'n' || op1 == 'N'){
            break;
        }
    }
    i++;
    }
    return 0;
}