//ANSWER: 104743
public class Euler007{
	public static void main(String[] args)
	{
		int primeCounter = 1;
		int number = 2;
		do{
			number++;
			if(isPrime(number))
				primeCounter++;
			
		}while(primeCounter < 10001);
		
		System.out.println("10,001st prime is: " + number);
	}

	public static boolean isPrime(int n)
	{
		for(int i =  2; i < n; i++)
		{
			if(n % i == 0)
				return false;
		}
		return true;
	}
}