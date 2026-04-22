import java.util.Scanner;
public class ScoreGrader {
                public static void main (String[] args) {
                Scanner inputCollector = new Scanner(System.in);

                System.out.println("What is your score?");
                int score = inputCollector.nextInt();

//              score calculator between 90 - 100
                if(score >= 90 && score <= 100){
                String grade = "A";
                System.out.printf("%d is Grade: %s %n%n", score,grade);
                }

//               score calculator between 80 and 89
                else if(score >= 80 && score <= 89){
                String grade = "B";
                System.out.printf("%d is Grade: %s %n%n", score,grade);
                }

//               score calculator between 70 and 79
                else if(score >= 70 && score <= 79){
                String grade = "C";
                System.out.printf("%d is Grade: %s %n%n", score,grade);
                }

//               score calculator between 70 and 79
                else if(score >= 60 && score <= 69){
                String grade = "D";
                System.out.printf("%d is Grade: %s %n%n", score,grade);
                }     

//               score calculator less than 60
                else if(score < 60){
                String grade = "E";
                System.out.printf("%d is Grade: %s %n%n", score, grade);
                }               
        }
}
