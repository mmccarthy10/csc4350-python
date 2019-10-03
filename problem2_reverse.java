import java.util.Scanner;

public class problem2_reverse {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String input = "";

		System.out.print("Enter a sentence to reverse: ");
		input = in.nextLine();
		String[] split = input.split(" ");

		for (int i = split.length - 1;i >= 0;i--) {
			System.out.print(split[i] + " ");
		}

		System.out.println("");
	}
}
