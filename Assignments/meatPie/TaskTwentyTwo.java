import java.util.Scanner; 
public class TaskTwentyTwo{
                                public static void main (String[] args) {

                                        Scanner valueCollector = new Scanner(System.in);    
                                        System.out.println("Give me a radius value!");

                                        double rad = valueCollector.nextDouble();
                                        float valOfPi = 3.142f;

                                        System.out.printf("The Area of a Circle with radius:%f, with val of Pi:%f is:",rad,valOfPi);
                                        System.out.println(3.142*rad*rad);
                       }
}
