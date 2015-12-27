//ANSWER:  232792560 
public class Euler005{
	public static void main(String[] args)
	{
		int num = 1;
		boolean isDivisible = false; //true if divisible by [1:20]
		do{
			num++;
			if( checkDivisibility(num) )
				isDivisible = true;
			
		}while(!isDivisible);

		System.out.println("number is: " + num);
	}

	public static boolean checkDivisibility(int num)
	{
		for(int i = 2; i <= 20; i++)
		{
			if(num%i != 0)
				return false;
		}
		return true;
	}
}