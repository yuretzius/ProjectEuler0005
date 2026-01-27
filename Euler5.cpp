#include <iostream>
#include <ctime>
#include <climits>

using namespace std;

int main(){
    unsigned long long valueFromLimits = ULLONG_MAX;
    cout << "Please enter an integer from 1 to 46 (max possible without overflowing unsigned long long)" << endl;
    int n;
    cin >> n;
    // not doing the sanity check, but if n > 46, this will result in garbage
    
    clock_t c_start = clock(); // clocking is really irrelevant here
    
    // numbers below are limited by 100, but since only inputs < 47 make sense
    // the lists can be shortened to {7,11,13,17,19,23,29,31,37,41,43}
    // {2,4,8,16,32} and {3,9,27}
    
    int primes[] = {7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}; //larger than 5
    int pow2[] = {2,4,8,16,32,64};
    int pow3[] = {3,9,27,81};
    int pow5[] = {5,25};
    unsigned long long res = 1;
    int i = 0;
    cout << res << endl;
    while (primes[i] <= n && i != 22) {
        res *= primes[i]; // since 7*7 > 46, each factor needs to be only used once 
        cout << res << endl; // product so far
        i++;
    }
    cout << "primes done" << endl;
    cout << "max possible:" << endl;
    cout << valueFromLimits << endl; // to see the limit and check for overflow
    cout << "____________________" << endl;
    i = 0;
    // cycle through the feasible power of 2
    while (pow2[i] <= n && i != 6) {
        res *= 2;
        i++;
        cout << res << endl; // product so far
    }
    cout << "2 done" << endl;
    cout << "max possible:" << endl;
    cout << valueFromLimits << endl; // to see the limit and check for overflow
    cout << "____________________" << endl;
    i = 0;
    while (pow3[i] <= n && i != 4) {
        res *= 3;
        i++;
        cout << res << endl; // product so far
    }
    cout << "3 done" << endl;
    cout << "max possible:" << endl;
    cout << valueFromLimits << endl; // to see the limit and check for overflow
    cout << "____________________" << endl;
    i = 0;
    while (pow5[i] <= n && i != 2) {
        res *= 5;
        i++;
        cout << res << endl; // product so far
    }
    cout << "5 done" << endl;
    cout << "result:" << endl;
    cout << res << endl; // final product
    clock_t c_end = clock();
    cout << "max possible:" << endl;
    cout << valueFromLimits << endl; // to see the limit and check for overflow
    cout << "____________________" << endl;
    cout << endl;
    cout << 1000.0*(c_end - c_start) / CLOCKS_PER_SEC << " ms\n";
    return 0;
}