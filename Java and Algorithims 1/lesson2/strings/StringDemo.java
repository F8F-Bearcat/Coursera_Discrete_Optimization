public class StringDemo
{
    public static void main(String[] args)
    {
        String river = "Mississippi";
        int numberOfLetters = river.length();
        System.out.println(numberOfLetters);
        String out_s = river.replace("i", "x");
        System.out.println(out_s);
        String greeting = "Hello";
        System.out.println(greeting.replace("H", "J"));
        System.out.println(greeting);
    }
}