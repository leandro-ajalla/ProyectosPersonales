public class App {
    public static void main(String[] args) throws Exception {
        Punto p1 = new Punto(3,4);
        Punto p2 = new Punto(0,0);
        System.out.println(p1.calcularDistancia(p2));
        System.out.println(p2.calcularDistancia(p1));
        Circulo c1 = new Circulo(p1, 2);
        Circulo c2 = new Circulo(p2, 2);
        System.out.println(c1.seTocan(c2));
    }
}