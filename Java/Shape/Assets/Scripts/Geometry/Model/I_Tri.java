package Shape.Assets.Scripts.Geometry.Model;

import Shape.Assets.Scripts.Geometry.Base.Shape;

public class I_Tri extends Shape{
    protected Double length, base, height;
    
    public I_Tri(Double height, Double length, Double base){
        this.length = length;
        this.base = base;
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
        return (2 * length) + base;
    }
    @Override
    public double getArea(){
        return (base * height)/2;
    }
}
