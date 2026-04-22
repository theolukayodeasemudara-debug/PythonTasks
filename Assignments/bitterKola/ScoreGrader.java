import java.util.Scanner;
public class ScoreGrader {
            public static void main (String[] args) {
                    Scanner inputCollector = new Scanner(System.in);

//                      User instructions
                        System.out.println("What is your Grade (Example; A,B,C,D,F)?");
//                      The input is expected to take a charcter
                        String userGrade = inputCollector.nextLine();


                        if(userGrade == "A") {
                            System.out.println("Grade: 4.0");
                        } else if (userGrade == "B") {
                            System.out.println("Grade: 3.0");
                        } else if (userGrade == "C") {
                            System.out.println("Grade: 2.0");
                        } else if (userGrade == "D") {
                            System.out.println("Grade: 1.0");
                        } else if (userGrade == "F") {
                             System.out.println("Grade: 0.0");
                        } else  {
                            System.out.println("Error finding your grade.");
                        }
            }
}
