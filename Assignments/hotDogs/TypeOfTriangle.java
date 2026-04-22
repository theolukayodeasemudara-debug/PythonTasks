import java.util.Scanner;
public class TypeOfTriangle {
                public static void main (String[] args) {
                Scanner inputCollector = new Scanner(System.in);

                System.out.println("Enter side One");
                int sideA = inputCollector.nextInt();

                System.out.println("Enter side Two");
                int sideB = inputCollector.nextInt();

                System.out.println("Enter side Three");
                int sideC = inputCollector.nextInt();

//              checking whether all three sides are equal (Equilateral Traingle)
                if(sideA == sideB && sideB== sideC){
                String type = "Equilateral Triangle";
                System.out.printf("Traingle with sides %d %d %d is an %s %n%n",sideA,sideB,sideC,type);
                } 

//              checking whether two sides are equal (Equilateral Traingle)
//              checking side A
                if(sideA == sideB && sideB != sideC){
                String type = "Isosceles Triangle";
                System.out.printf("Traingle with sides %d %d %d is an %s %n%n",sideA,sideB,sideC,type);
                }
                
//              checking sideB  
                else if(sideA != sideB && sideB == sideC){
                String type = "Isosceles Triangle";
                System.out.printf("Traingle with sides %d %d %d is an %s %n%n",sideA,sideB,sideC,type);
                }

//              checking sideC
                else if(sideA == sideC && sideB == sideB){
                String type = "Isosceles Triangle";
                System.out.printf("Traingle with sides %d %d %d is an %s %n%n",sideA,sideB,sideC,type);
                }

//              end of checking whether two sides are equal

//              checking whether the three sides have unequal values 
               if (sideA != sideB && sideB != sideC && sideC != sideA) {
                 String type = "Scalene Triangle";
                System.out.printf("Traingle with sides %d %d %d is an %s %n%n",sideA,sideB,sideC,type);
                }  
        }
}
