import java.util.Random;

public class problem1_missing {
	public static void main(String[] args) {
		int[] numbers = new int[100];

		System.out.println(generator());
		int[] testArray = new int[100];
		testArray = generator();

		for (int i = 0;i < 100;i++) {
			System.out.print(testArray[i] + " ");
		}

		System.out.println("The missing number is: " + detector(testArray));
	}

	public static int[] generator() {
		Random rand = new Random();
		int[] numbers = new int[100];
		int missing_number = rand.nextInt(100) + 1;
		
		for (int i = 1; i <= 100; i++) {
			if (i != (missing_number + 1))
				numbers[i - 1] = i;


		}


		return numbers;
	
	}

	public static int detector(int[] numbers) {
		int full_total = 5050;
		int new_total = 0;
		int missing_number = 0;

		for (int i = 0;i < 100; i++) {
			System.out.println(numbers[i]);
			new_total += numbers[i];
		}

		missing_number = full_total - new_total;

		return missing_number;


	}

}
