#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here
    int cur = 0;
    int fuel_remaining = tank;
    if(dist < tank) return 0;
    int num_refuel = 0;

    stops.push_back(dist);
    int n = stops.size();
    for(int i=0; i<n; i++){
        int dist = (stops[i]-cur);
        if( dist > tank) return -1;
        if( dist > fuel_remaining){
            num_refuel++;
            fuel_remaining = tank - dist;
        }else{
            fuel_remaining -= dist;
        }
        cur = stops[i];
    }
    return num_refuel;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (int i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
