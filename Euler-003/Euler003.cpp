//ANSWER: 6857
#include <iostream>
using namespace std;

//This function returns largest prime factor
int get_factor(long long int n)
{
	int factor = 2;
	while(n > 1)
	{
		while(n % factor == 0)
			n /= factor;
		++factor;
	}
	return --factor;
}

int main()
{
	long long int num = 600851475143;
	int maxPFactor = get_factor(num);
	cout << "Max Prime Factor: " << maxPFactor << endl;
	cin.get();
	
	return 0;
}