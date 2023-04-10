#include<iostream>
using namespace std;

int main() {

	// C++ array of 6 values (FIXED size)
	int array[6] = { 1, 3, 7, -20, 5, 9 };

	array[2] -= 1;
	array[4] += 15;
	array[5] = array[0] + 4;

	for (int i = 0; i < 6; ++i)
		cout << array[i]<<" ";

	return 0;
}

