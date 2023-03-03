package Shape.Assets.Scripts.Geometry.Model;

public class Cube extends Rectangle{
    private final Double side;
    public Cube(Double length, Double width, Double side){
        super(length, width);
        this.side = side;
    }
    public Double getSide(){
        return side * (length * length);
    }
    public Double getVolume(){
        return length * length * length;
    }
    public void side(){
        System.out.println("Surface area : " + getSide());
    }
    public void volume(){
        System.out.println("Volume : " + getVolume());
    }
}
