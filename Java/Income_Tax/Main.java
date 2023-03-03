package Income_Tax;

import java.util.Scanner;
import Income_Tax.Assets.Scripts.Tax;

public class Main{
    public static void main(String[] args){
        long nti, agi, result;
        char loop;
        Tax calculateTax;
        Scanner input = new Scanner(System.in);
        do{
            print("\nTax Calculator\n");
            print("\nAmount of Annual Income        : ");
            agi = input.nextLong();
            print("Amount of Non-taxable Income   : ");
            nti = input.nextLong();
            calculateTax = new Tax(nti, agi);
            result = calculateTax.calculate();
            print("\nTaxable Income   : ");
            print(calculateTax.getTi());
            print("\nTax Bracket      : ");
            print(calculateTax.getTax());
            print("%");
            print("\nAmount to Pay    : ");
            print(result);
            print("\n\nRe-enter? (y/n) : ");
            input.nextLine();
            loop = input.nextLine().charAt(0);
        }
        while(loop == 'y' || loop == 'Y');
        input.close();
    }
    private static void print(Object any){
        System.out.print(any);
    }
}