package Shape.Assets.Scripts.Geometry.Model;

import Shape.Assets.Scripts.Geometry.Base.Shape;

public class R_A_Tri extends Shape{
    private final Double hypotenuse, height, base;
    
    public R_A_Tri(Double hypotenuse, Double height, Double base){
        this.hypotenuse = hypotenuse;
        this.height = height;
        this.base = base;
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
        return hypotenuse + base + height;
    }
    @Override
    public double getArea(){
        return (base * height)/2;
    }
}
