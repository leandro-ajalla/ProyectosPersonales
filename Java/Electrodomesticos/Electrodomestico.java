public class Electrodomestico {
    //Constante (valores por defecto)
    private float PRECIO_BASE = 100;
    private String COLOR = "blanco";
    private char CONSUMO = 'F';
    private float PESO = 5;
    //Variables
    private float precioBase = this.PRECIO_BASE;
    private String color = this.COLOR;
    private char consumo = this.CONSUMO;
    private float peso = this.PESO;

    // Un constructor por defecto
    public Electrodomestico() {
    }
    // Un constructor con todos los atributos
    public Electrodomestico(float precioBase, String color, char consumo, float peso) {
        this.precioBase = precioBase;
        this.color = comprobarColor(color);
        this.consumo = comprobarConsumoEnergetico(consumo);
        this.peso = peso;
    }
    // Un constructor con el precio y peso. El resto por defecto
    public Electrodomestico(float precioBase, float peso) {
        this.precioBase = precioBase;
        this.peso = peso;
    }    
    // Métodos get de todos los atributos
    public float getPrecioBase() {
        return precioBase;
    }
    public String getColor() {
        return color;
    }
    public char getConsumo() {
        return consumo;
    }
    public float getPeso() {
        return peso;
    }
    // comprueba que la letra es correcta, sino es correcta usara la letra por defecto. Se invocara al crear el objeto y no sera visible.
    protected char comprobarConsumoEnergetico(char letra){
        if (letra == 'A' || letra =='a'){
            return 'A';
        }
        if (letra == 'B' || letra =='b'){
            return 'B';
        }
        if (letra == 'C' || letra =='c'){
            return 'C';
        }
        if (letra == 'D' || letra =='d'){
            return 'D';
        }
        if (letra == 'E' || letra =='e'){
            return 'E';
        }
        return 'F';
    }
    // comprueba que el color es correcto, sino lo es usa el color por defecto. Se invocara al crear el objeto y no sera visible.
    protected String comprobarColor(String color){
        if (color.equalsIgnoreCase("negro")){
            return "negro";
        }
        if (color.equalsIgnoreCase("rojo")){
            return "rojo";
        }
        if (color.equalsIgnoreCase("azul")){
            return "azul";
        }
        if (color.equalsIgnoreCase("gris")){
            return "gris";
        }
        return this.COLOR;
    }
    // según el consumo energético, aumentara su precio, y según su tamaño, también. Esta es la lista de precios:
// Letra	Precio
// A	100 €
// B	80 €
// C	60 €
// D	50 €
// E	30 €
// F	10 €
// Tamaño	Precio
// Entre 0 y 19 kg	10 €
// Entre 20 y 49 kg	50 €
// Entre 50 y 79 kg	80 €
// Mayor que 80 kg	100 €
    public float precioFinal(){
        float precioTotal = 0;
         switch (this.consumo) {
            case 'A':
                precioTotal = this.precioBase + 100; 
                break;
            case 'B':
                precioTotal = this.precioBase + 80; 
                break;
            case 'C':
                precioTotal = this.precioBase + 60; 
                break;
            case 'D':
                precioTotal = this.precioBase + 50; 
                break;
            case 'E':
                precioTotal = this.precioBase + 30; 
                break;
            case 'F':
                precioTotal = this.precioBase + 10; 
                break;
        }
// Tamaño	Precio
// Entre 0 y 19 kg	10 €
// Entre 20 y 49 kg	50 €
// Entre 50 y 79 kg	80 €
// Mayor que 80 kg	100 €       
        if(this.peso > 0 && this.peso < 19){
            precioTotal += 10;
        }
        if(this.peso > 20 && this.peso < 49){
            precioTotal += 50;
        }
        if(this.peso > 50 && this.peso < 79){
            precioTotal += 80;
        }
        if(this.peso > 80){
            precioTotal += 100;
        }
        return precioTotal;
    }    
}
