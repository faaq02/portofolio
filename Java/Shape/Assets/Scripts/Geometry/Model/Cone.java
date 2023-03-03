package Shape.Assets.Scripts.Geometry.Model;

import Shape.Assets.Scripts.Geometry.Base.Shape;

public class Cone extends Shape{
    private final Double height, radius;
    public Cone(Double height, Double radius){
        this.height = height;
        this.radius = radius;
    }
    @Override
    public double getPerimeter(){
        return 0;
    }
    public double getVolume(){
        return  Math.PI * Math.pow(radius, 2) * height * 1/3;
    }
    @Override
    public double getArea(){
        return Math.PI * radius * radius + Math.PI * radius * height;
    }
    @Override
    public void area(){
        System.out.println("Area : " + getArea());
    }
    @Override
    public void perimeter(){
        System.out.println("Perimeter: " + getPerimeter());
    }
    public void volume(){
        System.out.println("Volume : " + getVolume());
    }
}
