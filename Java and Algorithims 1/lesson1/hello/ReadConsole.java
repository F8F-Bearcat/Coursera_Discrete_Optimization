import java.util.Scanner;

public class ReadConsole
{
    public static void main(String[] args)
    {
        System.out.println("Hello, World!");
        Scanner in = new Scanner(System.in);
        System.out.println("Scanner output here:");
        String text = in.nextLine();
        System.out.println(text);
        in.close();
    }
}
