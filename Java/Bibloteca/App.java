public class App {
    public static void main(String[] args) throws Exception {
        Autor a1 = new Autor("leandro","leadnro@gmail.com",'m');
        a1.setEmail("leadnro");
        Autor a2 = new Autor("Gabril","gabo@sada",'m');
        Libro l1 = new Libro("holaaa", a2, 555.55, 5);
        System.out.println(a1);
        System.out.println(l1);

    
    
        System.out.println("Hello, World!");
    
    
    }
}
