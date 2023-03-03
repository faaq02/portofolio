package Shape;

import Shape.Assets.Scripts.Geometry.Base.*;
import Shape.Assets.Scripts.Geometry.Model.*;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Scanner input = new Scanner(System.in);
        ask();
        System.out.print("Enter choice : ");
        for(int i = 1; i <= 12; i++){
            switch(scanner.next()){
                case "1" :
                    System.out.println("\nCircle");
                    Circle(input);
                    break;
                case "2" :
                    System.out.println("\nRectangle");
                    Rectangle(input);
                    break;
                case "3" :
                    System.out.println("\nCone");
                    Cone(input);
                    break;
                case "4" :
                    System.out.println("\nCube");
                    Cube(input);
                    break;
                case "5" :
                    System.out.println("\nCylinder");
                    Cylinder(input);
                    break;
                case "6" :
                    System.out.println("\nSphere");
                    Sphere(input);
                    break;
                case "7" :
                    System.out.println("\nEquilateral Triangle");
                    E_Tri(input);
                    break;
                case "8" :
                    System.out.println("\nIsosceles Triangle");
                    I_Tri(input);
                    break;
                case "9" :
                    System.out.println("\nRight-angled Triangle");
                    R_A_Tri(input);
                    break;
                case "10" :
                    System.out.println("\nPyramid");
                    Pyramid(input);
                    break;
                case "11" :
                    System.out.println("\nTetrahedron");
                    Tetrahedron(input);
                    break;
                case "12" :
                    System.out.println("\nTriangular Prism");
                    Prism(input);
                    break;            
                default :
                    System.out.println("\nAdios\n");
                    System.exit(0);
                    break;
            }
            ask();
            System.out.print("Enter choice : ");
        }
        scanner.close();
        input.close();
    }
    private static void ask(){
        System.out.println("\nChoose Shape : ");
        System.out.println("1.  Circle");
        System.out.println("2.  Rectangle");
        System.out.println("3.  Cone");
        System.out.println("4.  Cube");
        System.out.println("5.  Cylinder");
        System.out.println("6.  Sphere");
        System.out.println("7.  Equilateral Triangle");
        System.out.println("8.  Isosceles Triangle");
        System.out.println("9.  Right-angled Triangle");
        System.out.println("10. Pyramid");
        System.out.println("11. Tetrahedron");
        System.out.println("12. Triangular Prism");
        System.out.println("Other number to quit\n");
    }
    private static void Circle(Scanner input){
        System.out.print("Radius : ");
        int radius = input.nextInt();
        Shape Circle = new Circle(radius);
        Circle.area();
        Circle.perimeter();
    }
    private static void Rectangle(Scanner input){
        System.out.print("Length : ");
        Double length = input.nextDouble();
        System.out.print("Width : ");
        Double width = input.nextDouble();
        Shape Rectangle = new Rectangle(width, length);
        Rectangle.area();
        Rectangle.perimeter();
    }
    private static void Cone(Scanner input){
        System.out.print("Radius : ");
        Double radiusCone = input.nextDouble();
        System.out.print("Height : ");
        Double heightCone = input.nextDouble();
        Cone Cone = new Cone(radiusCone, heightCone);
        Cone.area();
        Cone.volume();
    }
    private static void Cube(Scanner input){
        System.out.print("Side : ");
        Double side = input.nextDouble();
        System.out.print("Length : ");
        Double lengthSide = input.nextDouble();
        System.out.print("Width : ");
        Double widthSide = input.nextDouble();
        Cube Cube = new Cube(side, lengthSide, widthSide);
        Cube.side();
        Cube.volume();
    }    
    private static void Cylinder(Scanner input){
        System.out.print("Radius : ");
        int r = input.nextInt();
        System.out.print("Height : ");
        int h = input.nextInt();
        Cylinder Cylinder = new Cylinder(r, h);
        Cylinder.volume();
    }
    private static void Sphere(Scanner input){
        System.out.print("Radius : ");
        int surface = input.nextInt();
        Sphere Sphere = new Sphere(surface);
        Sphere.volume();
    }
    private static void E_Tri(Scanner input){
        System.out.print("Length : ");
        Double length = input.nextDouble();
        System.out.print("Height : ");
        Double height = input.nextDouble();
        Shape E_Tri = new E_Tri(length, height);
        E_Tri.area();
        E_Tri.perimeter();
    }
    private static void I_Tri(Scanner input){
        System.out.print("Length : ");
        Double length = input.nextDouble();
        System.out.print("Base : ");
        Double base = input.nextDouble();
        System.out.print("Height : ");
        Double height = input.nextDouble();
        Shape I_Tri = new I_Tri(length, height, base);
        I_Tri.area();
        I_Tri.perimeter();
    }
    private static void R_A_Tri(Scanner input){
        System.out.print("Hypotenuse : ");
        Double hypotenuse = input.nextDouble();
        System.out.print("Height : ");
        Double height = input.nextDouble();
        System.out.print("Base : ");
        Double base = input.nextDouble();
        Shape R_A_Tri = new R_A_Tri(hypotenuse, height, base);
        R_A_Tri.area();
        R_A_Tri.perimeter();
    }
    private static void Pyramid(Scanner input){
        System.out.print("Length : ");
        Double length = input.nextDouble();
        System.out.print("Height : ");
        Double height = input.nextDouble();
        System.out.print("Base : ");
        Double base = input.nextDouble();
        Pyramid Pyramid = new Pyramid(length, height, base);
        Pyramid.volume();
        Pyramid.area();
        Pyramid.perimeter();
    }   
    private static void Tetrahedron(Scanner input){
        System.out.print("Length : ");
        Double length = input.nextDouble();
        System.out.print("Height : ");
        Double height = input.nextDouble();
        Tetrahedron Tetrahedron = new Tetrahedron(length, height);
        Tetrahedron.volume();
        Tetrahedron.area();
        Tetrahedron.perimeter();
    }   
    private static void Prism(Scanner input){
        System.out.print("Length : ");
        Double length = input.nextDouble();
        System.out.print("Width : ");
        Double width = input.nextDouble();
        System.out.print("Height : ");
        Double height = input.nextDouble();
        System.out.print("Base : ");
        Double base = input.nextDouble();
        Prism Prism = new Prism(length, width, height, base);
        Prism.volume();
        Prism.area();
        Prism.perimeter();
    }      
}
