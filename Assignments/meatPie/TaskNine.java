import java.util.Scanner; 
public class TaskNine{
                public static void main (String[] args) {
                    Scanner colorCollector = new Scanner(System.in);

                    System.out.println("What's your favorite color?");
                    String color = colorCollector.nextLine();   

                    System.out.printf("You just said your favorite color is  %s %n%n", color);        
                }
}
