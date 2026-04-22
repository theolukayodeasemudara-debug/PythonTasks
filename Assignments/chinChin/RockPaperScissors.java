import java.util.Scanner;
public class RockPaperScissors {
            public static void main (String[] args) {
                        Scanner userInput = new Scanner(System.in);

//                      User instructions
                        System.out.println("Pick a number between 0 and 3 to play 'Rock--1' 'Paper--2' 'Scissors--3' ");
                        int playerNum = userInput.nextInt();

//                      game variables
                        String one = "Rock";
                        String two = "Paper";
                        String three = "Scissors";

//                        String playerChoice;
//                      Matching player choice
//                        if (playerNum == 1){
//                               playerChoice = one;
//                        }

//                      Generating a number between 0 and 3
                         int randomNum = (int)(Math.random() * 3)+1;

//                      checking player input
                        if(randomNum == 1) {
                            System.out.printf("%s: Comp: %d,  player: %d %n",one,randomNum,playerNum);
                        } else if(randomNum == 2) {
                            System.out.printf("%s: Comp: %d,  player: %d %n",two,randomNum,playerNum);
                        } else if(randomNum == 3){
                            System.out.printf("%s: Comp: %d,  player: %d %n",three,randomNum,playerNum);
                        }
            }
}
