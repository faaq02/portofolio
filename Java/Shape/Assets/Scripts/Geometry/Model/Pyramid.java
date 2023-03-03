package Shape.Assets.Scripts.Geometry.Model;

public class Pyramid extends I_Tri{
    public Pyramid(Double length, Double height, Double base){
        super(length, height, base);
    }
    public void volume(){
        System.out.println("Volume : " + getVolume());
    }
    public void area(){
        System.out.println("Area : " + getArea());
    }    
    public void perimeter(){
        System.out.println("Perimeter : " + getPerimeter());
    }
    public double getVolume(){
        return (height * base * base)/3;
    }
    @Override
    public double getArea(){
        return (4 * (height * base)/2) + (base * base);
    }
    @Override
    public double getPerimeter(){
        return (4 * base) + (4 * length);
    }
}
