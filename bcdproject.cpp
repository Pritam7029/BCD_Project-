#include<iostream>
using namespace std;


void output(char b[])
{
    cout<<"\n "<<b[0]<<" ";
    cout<<"\n"<<b[5]<<b[6]<<b[1];
    cout<<"\n"<<b[4]<<b[3]<<b[2];
}
void convert(int a[])
{
    char b[7];
    for(int i=0;i<7;i++)
    {
        if(a[i]==1)
        {
            if(i==0||i==3||i==6)
            {
                b[i]='_';
            }
            else
            {
                b[i]='|';
            }
        }
        else
            b[i]=' ';
    }
    output(b);
}
int main()
{
    int a[7];
    int i=0;
    cout<<"\n Enter binary no. for all the segment ";
    while(i<7)
    {
        cout<<"\n "<<char(97+i)<<" :: ";
        cin>>a[i];
        if (a[i]==0||a[i]==1)
        {
            i++;
        }
        else
        cout<<" Please input 0 or 1 ";
    }
    convert(a);
    cout<<endl;
return(0);
}