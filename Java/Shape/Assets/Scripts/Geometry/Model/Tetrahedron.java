package Shape.Assets.Scripts.Geometry.Model;

public class Tetrahedron extends E_Tri{    
    public Tetrahedron(Double length, Double height){
        super(length, height);
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
        return (height * (length * height)/2)/3;
    }
    @Override
    public double getArea(){
        return 4 * (length * height)/2;
    }
    @Override
    public double getPerimeter(){
        return (4 * (length * height));
    }
}
