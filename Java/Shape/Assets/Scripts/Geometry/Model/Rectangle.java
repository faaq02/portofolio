package Shape.Assets.Scripts.Geometry.Model;

import Shape.Assets.Scripts.Geometry.Base.*;

public class Rectangle extends Shape{
    protected Double length, width;
    public Rectangle(Double length, Double width){
        this.length = length;
        this.width = width;
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
        return length * width;
    }
    @Override
    public double getPerimeter(){
        return 2 * (length + width);
    }
}
