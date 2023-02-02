#include <iostream>
using namespace std;
int main ()
{
for(int i = 99; i >= 1; i--) {

if(i % 3 == 0 and i % 5 == 0) {
    cout << "ПшшшшВжжжж" << endl;}
else if(i % 3 == 0) {
    cout << "Пшшшш" << endl;}
else if(i % 5 == 0) {
    cout << "Вжжжж" << endl;}
else {
cout << i << endl;}}

return 0;}