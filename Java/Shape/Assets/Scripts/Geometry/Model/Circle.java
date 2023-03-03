package Shape.Assets.Scripts.Geometry.Model;

import Shape.Assets.Scripts.Geometry.Base.Shape;

public class Circle extends Shape{
    protected int radius;
    public Circle(int radius){
        this.radius = radius;
    }
    @Override
    public void area(){
        System.out.println("Area : " + getArea());
    }
    @Override
    public void perimeter(){
        System.out.println("Perimeter : " + getPerimeter());
    }
    @Override
    public double getArea(){
        return Math.PI * radius * radius;
    }
    @Override
    public double getPerimeter(){
        return Math.PI * radius * 2;
    }
}
