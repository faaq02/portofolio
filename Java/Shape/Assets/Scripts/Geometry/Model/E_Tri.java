package Shape.Assets.Scripts.Geometry.Model;

import Shape.Assets.Scripts.Geometry.Base.Shape;

public class E_Tri extends Shape{
    protected Double length, height;
    
    public E_Tri(Double length, Double height){
        this.length = length;
        this.height = height;
    }
    @Override
    public void perimeter(){
        System.out.println("Area: " + getPerimeter());
    }
    @Override
    public void area(){
        System.out.println("Perimeter: " + getArea());
    }
    @Override
    public double getPerimeter(){
        return 3 * length;
    }
    @Override
    public double getArea(){
        return (length * height)/2;
    }
}
