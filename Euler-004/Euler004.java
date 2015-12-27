//ANSWER:  906609 
public class Euler004{
	public static void main(String[] args)
	{		
		int largestPalindrom = -1;
		
		for(int num1 = 1; num1 <= 999; num1++)
		{
			for(int num2 = 1; num2 <= 999; num2++)
			{
				int product = num1 * num2;
				if(isPalindrom(product))
				{
					if(largestPalindrom < product)
						largestPalindrom = product;
				}
			}
		}

		System.out.println("largest palindrom is: " + largestPalindrom);
	}

	public static boolean isPalindrom(int num)
	{
		String strNum = String.valueOf(num);
		int length = strNum.length();
		
		String firstHalf = strNum.substring(0, length/2);
		String secondHalf = strNum.substring(length/2, length);
		String secondHalfRev = "";

		for(int i = secondHalf.length()-1; i >= 0; i--)
			secondHalfRev += secondHalf.charAt(i);

		return firstHalf.equals(secondHalfRev);	
	}
}