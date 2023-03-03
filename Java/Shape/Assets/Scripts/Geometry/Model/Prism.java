package Shape.Assets.Scripts.Geometry.Model;

import Shape.Assets.Scripts.Geometry.Base.Shape;

public class Prism extends Shape{
    protected Double base, height;
    protected Double length, width;
    
    public Prism(Double base, Double height, Double length, Double width){
        this.base = base;
        this.height = height;
        this.length = length;
        this.width = width;
    }
    public void volume(){
        System.out.println("Volume : " + getVolume());
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
        return (3 * length * width) + (2 * (base * height/2));
    }
    @Override
    public double getPerimeter(){
        return (4 * width) + (3 * length) + (2 * base);
    }
    public double getVolume(){
        return ((base * height)/2) * length;
    }
}
