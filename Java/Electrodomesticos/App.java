import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        ArrayList<Electrodomestico> arrayElect = new ArrayList<>();
        Electrodomestico e1 = new Electrodomestico();
        arrayElect.add(e1);
        Electrodomestico e2 = new Electrodomestico(200, "azul", 'G', 60);
        arrayElect.add(e2);
        Electrodomestico e3 = new Electrodomestico(150, 35);
        arrayElect.add(e3);
        Lavadora l1 = new Lavadora();
        arrayElect.add(l1);
        Lavadora l2 = new Lavadora(300, 75);
        arrayElect.add(l2);
        Lavadora l3 = new Lavadora(125, "verde", 'D', 46, 15);
        arrayElect.add(l3);
        Television t1 = new Television();
        arrayElect.add(t1);
        Television t2 = new Television(500, 18);
        arrayElect.add(t2);
        Television t3 = new Television(450,"negro", 'B', 12,44,true);        
        arrayElect.add(t3);
         

        for (int i = 0; i < arrayElect.size(); i++) {
            System.out.println(esInstancia(arrayElect.get(i)));
            System.out.println(arrayElect.get(i).precioFinal());            
        }
    }

    public static String esInstancia(Electrodomestico e){
        if (e instanceof Lavadora) {
            return "Lavadora";
        } else if (e instanceof Television) {
            return "Television";
        } else {
            return "Electrodomestico";
        }
    }
}