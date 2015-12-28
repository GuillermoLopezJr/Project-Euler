//Answer: 25164150
public class Euler006{
	public static void main(String[] args)
	{
		int sumOfSquares = 0;
		int sum = 0;
		int squareOfSum = 0;
		int difference = 0;

		for(int i = 1; i <= 100; i++)
		{
			sumOfSquares += i*i;
			sum += i;
		}
		squareOfSum = sum*sum;
		difference = squareOfSum - sumOfSquares;
		System.out.println("Difference is: " + difference);
	}
}