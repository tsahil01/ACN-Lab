#include<bits/stdc++.h>
using namespace std;

int main(){
    int a,b;
    string ip;
    string arr[6];
    cout<<"Enter the Ipv4 address string: ";
    cin>>ip;
    int j = 0;
    int len = 1;

    for(int i = 0; i<ip.length(); i++){
        if(ip[i]!='.'){
            arr[j] = arr[j] + ip[i];
        } else{
            j++;
            len++;
        }
    }

    int input;
    while (true){
    cout<<endl;
    cout<<"Enter:"<<endl
    <<"1. To check leading zeors."<<endl
    <<"2. To check the range of IP address and Check if contains integer values."<<endl
    <<"3. To check cell should have exactaly 4 cells"<<endl
    <<"4. To check each Ip cell value should be seperated by dot/period only"<<endl
    <<"5. To check the Class of Ip address"<<endl
    <<"6. To check if it is a special IP address or not."<<endl;
    cout<<"enter input: ";
    cin>>input;
        switch (input){
            case 1:
            a = 0;
            for(int j = 0; j<4; j++){
                if(arr[j][0] == '0'){
                    cout<<"Error: There should be no leading zeros in the IPv4 address string: "<<arr[j]<<endl;
                    a++;
                    break;
                }
            }
            if(a == 0){
                cout<<"There are no leading zero error"<<endl;
            }
            break;

            case 2:
            a = 0;
            b = 0;
            for(int j = 0; j<4; j++){
                try{
                    int value = stoi(arr[j]);
                    if(!(value>0 && value<255)){
                    cout<<"ERROR: "<<value<<" should be between the range of 0-255 "<<endl;
                    a++;
                    break;
                }
                } catch(exception e){
                    cout<<"ERROR: The entered Ipv4 does not contain only integer values"<<endl;
                    b++;
                    break;
                }
            }
            if(a==0) cout<<"No range error."<<endl;
            if(b==0) cout<<"The cell value have only integer values."<<endl;
            break;

            case 3:
            a = 0;
            if(len != 4){
                a++;
                cout<<"ERROR: The Ip address should have exactly 4 cells"<<endl;
            }
            if(a==0) cout<<"Ip add have 4 cells"<<endl;
                break;

            case 4:
                a = 0;
            for(int i = 0; i<ip.length(); i++){
                if(!(int(ip[i]) == 46 || int(ip[i])>47 && int(ip[i])<58 )){ 
                    a++;
                    cout<<"ERROR: Each Ip cell value should be seperated by dot/period only. Error: "<<ip[i]<<endl;
                    break; 
                }
            }
            if(a == 0) cout<<"Each ip celss is seperated by dot/peroid."<<endl;
                break;

            case 5:
            try{
            if(stoi(arr[0]) > 0 && stoi(arr[0])<127)
                cout<<"Class A"<<endl;
            if(stoi(arr[0]) > 127  && stoi(arr[0])<191)
                cout<<"Class B"<<endl;
            if(stoi(arr[0]) > 191  && stoi(arr[0])<223)
                cout<<"Class C"<<endl;
            if(stoi(arr[0]) > 223  && stoi(arr[0])<239)
                cout<<"Class D"<<endl;
            if(stoi(arr[0]) > 240  && stoi(arr[0])<255)
                cout<<"Class E"<<endl;
            } catch(exception e){
                cout<<"Undefined Class"<<endl;
            }
            break;

            case 6:
            if(ip == "127.0.0.1" || "0.0.0.0" || "224.0.0.1"){
                cout<<"It is a Special Ip address"<<endl;
            } else{
                cout<<"It is not a Speical Ip address"<<endl;
            }

            default:
            cout<<"Enter correct option"<<endl;
            break;
        }
    }


    return 0;
}
