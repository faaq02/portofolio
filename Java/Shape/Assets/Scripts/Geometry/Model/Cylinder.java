package Shape.Assets.Scripts.Geometry.Model;

public class Cylinder extends Circle{
    protected int height;
    public Cylinder(int radius, int height){
        super(radius);
        this.height = height;
    }
    public double getVolume(){
        return Math.PI * Math.pow(radius, 2) * height;
    }
    public void volume(){
        System.out.println("Volume : " + getVolume());
    }
}
