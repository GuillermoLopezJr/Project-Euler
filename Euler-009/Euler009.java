//ANSWER: 31875000 
public class Euler009
{
	public static void main(String[] args)
	{
		for(int a = 1; a < 1000; a++)
			for(int b = 2; b < 1000-a; b++) // sum can't be > 1000
			{
				int c = 1000 - (b + a); // sum can't be > 1000
				if(isPythagoreanTriplet(a,b,c))
				{
					if( (a + b + c) == 1000)
					{
						System.out.println("product is: " + a*b*c);
						System.exit(0);
					}
				}	
			}
	}

	public static boolean isPythagoreanTriplet(int a, int b, int c)
	{
		return ( (a*a) + (b*b) == (c*c) ); 
	}
}