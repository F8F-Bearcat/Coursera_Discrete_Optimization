import java.util.Scanner;


public class ReadConsole
{
    private WeightedQuickUnionUF QF = new WeightedQuickUnionUF(10);
    
    public static void main(String[] args)
    {
        System.out.println("Hello, World!");
        System.out.println(QF.count());
        Scanner in = new Scanner(System.in);
        System.out.println("Scanner output here:");
        String text = in.nextLine();
        System.out.println(text);
        in.close();
    }
}
