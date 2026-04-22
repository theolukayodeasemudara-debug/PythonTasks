import java.util.Scanner;
public class LotteryApp {
            public static void main (String[] args) {
                        Scanner userInput = new Scanner(System.in);

//                      player instruction one
                        System.out.println("Enter your first one digit number");
                        int pOne = userInput.nextInt();

//                      Generating a number between 0 and 9
                         int rOne = (int)(Math.random() * 10) + 1;


//                      player instruction two
                        System.out.println("Enter your second one digit number");
                        int pTwo = userInput.nextInt();

//                      Generating a number between 0 and 9
                         int rTwo = (int)(Math.random() * 10) + 1;

//                      checking player input
                        if(rOne == pOne && rTwo == pTwo) {
                            System.out.printf("Lottery number: %d%d  player number: %d%d %n Congratulations you have won $10,000 %n",rOne,rTwo, pOne,pTwo);
                        } else if(rOne == pOne || rOne == pTwo || rTwo == pOne || rTwo == pTwo) {
                            System.out.printf("Lottery number: %d%d  player number: %d%d %n Congratulations you have won $1,000 %n",rOne,rTwo, pOne,pTwo);        
                        } else if(rOne != pOne || rOne != pTwo || rTwo != pOne || rTwo != pTwo) {
                            System.out.printf("Your money is gone %n");        
                        }
}
}
