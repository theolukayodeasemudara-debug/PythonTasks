import java.util.Scanner;
public class TaskTwentySix {
                public static void main (String[] args) {
                            Scanner valueCollector = new Scanner(System.in);

                             System.out.println("What is your name champ?");
                             String name = valueCollector.nextLine();  

                             System.out.println("How old are you?");
                             int age = valueCollector.nextInt();

                            System.out.printf("Hello %s, you are %d years old!!! %n%n", name,age);  
                }
}
