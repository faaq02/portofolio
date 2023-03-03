package Income_Tax.Assets.Scripts;

public class Tax{
    private long ti, nti, agi, tax;
    public Tax(long nti, long agi){
        this.nti = nti;
        this.agi = agi;
    }
    public long calculate(){
        float result = 0;
        this.ti = this.agi - this.nti;
        if(this.ti > 0){
            if(this.ti <= 50000000){
                this.tax = 5;
                result = this.ti * this.tax / 100;
            } 
            else if(this.ti > 50000000 && this.ti <= 250000000){
                this.tax = 15;
                result = (5 / 100 * 50000000) + ((this.ti - 50000000) * 
                this.tax / 100);
            } 
            else if(this.ti > 250000000 && this.ti <= 500000000){
                this.tax = 25;
                result = (5 / 100 * 50000000) + (15 / 100 * 200000000) + 
                ((this.ti - 250000000) * this.tax / 100);
            } 
            else if(this.ti > 500000000){
                this.tax = 30;
                result = (5 / 100 * 50000000) + (15 / 100 * 200000000) + 
                (25 / 100 * 250000000) + ((this.ti - 500000000) * this.tax / 100);
            }
        }
    return(long) result;
    }
    public long getTax(){
        return this.tax;
    }
    public long getTi(){
        return this.ti;
    }
}