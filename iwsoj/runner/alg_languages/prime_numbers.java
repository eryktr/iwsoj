import java.io.*;
import java.lang.Math;

public class prime_numbers {

	private static int prime(int n) {
		if (n<2) {
			return 0;
		} else {
			int counter = 0;
			for (int i=2; i<=n; i++) {
				counter++;
				for (int j=2; j<=Math.sqrt(i); j++) {
					if (i%j==0) {
						counter--;
						break;
					}
				}
			}
		return counter;
		}       
	
	}
	
	public static void main(String[] args) {
		try{
			BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
			String line;
			while((line = bufferRead.readLine()) != null) {
				try {
					int n = Integer.parseInt(line);;
					System.out.println(prime(n));
				} catch(Exception e) {
					System.out.println("Uncorrect parameter");
				}
			}
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
	}

}