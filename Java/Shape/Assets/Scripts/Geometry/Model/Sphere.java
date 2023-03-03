package Shape.Assets.Scripts.Geometry.Model;

public class Sphere extends Circle{
    public Sphere(int r){
        super(r);
    }
    public double getVolume(){
        return Math.PI * Math.pow(radius, 3) * 4/3;
    }
    @Override
    public double getArea(){
        return Math.PI * Math.pow(radius, 2) * 4;
    }
    public void volume(){
        System.out.println("Volume : " + getVolume());
    }
}
