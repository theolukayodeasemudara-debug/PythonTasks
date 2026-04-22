import java.util.Scanner;
public class EndPointCalc {
        public static void main (String[] args) {
            Scanner input = new Scanner(System.in);

//          user instruction prompt
            System.out.println("Give me any preferred number");
            int userNum = input.nextInt(); 

//          logic check
            if(userNum >10 && userNum < 100) {
                    System.out.println("Your number is between 10 and 100");
            } else {
                    System.out.println("Your number is not within range!");
            }
        }
}
