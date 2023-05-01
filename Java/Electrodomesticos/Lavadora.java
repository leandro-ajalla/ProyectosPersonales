public class Lavadora extends Electrodomestico {
    //constante
    private float CARGA = 5;
    //variable
    private float carga = this.CARGA;
    //constructor por defecto
    public Lavadora() {
    }
    //constructor precio y peso
    public Lavadora(float precioBase, float peso) {
        super(precioBase, peso);
    }
    //constructor con todo
    public Lavadora(float precioBase, String color, char consumo, float peso, float carga) {
        super(precioBase, color, consumo, peso);
        this.carga = carga;
    }
    //get de carga
    public float getCarga() {
        return carga;
    }
    //precio final
    public float precioFinal(){
        float precioFinalLavadora = super.precioFinal();
        if (this.carga > 30) {
            precioFinalLavadora += 50;
        }
        return precioFinalLavadora;
    }
}