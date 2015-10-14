//ANSWER: 4613732

#include <iostream>

using namespace std;

int main()
{
	int term1 = 1;
	int term2 = 2;
	int sum = 2;
	while(term1 <4000000 || term2<4000000)
	{
		term1 = term1+term2;
		if(term1 % 2 == 0)
			sum += term1;
		term2 = term1+term2;
		if(term2 %2 == 0)
			sum += term2;
	}
	cout << "sum " << sum << endl;
	cin.get();

	return 0;
}