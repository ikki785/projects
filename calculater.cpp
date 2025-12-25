#include <iostream>
using namespace std;
void ca(){
    long long a;
        char b;
        long long c;
        int i = 0;  
        char op ;
    while (true){/*add a loop in calculater*/
        
        i++; 
        cin>>a;
        cin >>b;
        cin >>c;
        if (cin.fail()){
            cin.clear();
            cin.ignore(10000, '\n');
        }
        switch (b){
            case  '+':
                cout<<a+c<<endl;
                break;
            case '-':
                cout<<a-c<<endl;
                break;
            case '*':
                cout<<a*c<<endl;
                break;
            case '/':
                cout<<a/c<<endl;
                break;
            case 'r':
                cout<<"big ass";
            default:
                cout<<"envialied option fool "<<endl;
                break;
            
        }
        if (i >= 3){
            cout <<"do you want to contiune"<<endl;
            cin>>op;
            if (op == 'n'){
                cout<<"thanks:)"<<endl;
                break;
                

            }
            else {
                i = i;
            }
            

        }

    }
    
}
int main(){
    ca(); 
    return 0;
}