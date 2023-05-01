public class Television extends Electrodomestico {
    private int resolucion = 20;
    private boolean sintonizadorTDT = false;
    //construcrtor por defecto
    public Television() {
    }
    //peso y precio
    public Television(float precioBase, float peso) {
        super(precioBase, peso);
    }
    //res. y sint.
    public Television(float precioBase, String color, char consumo, float peso, int resolucion,
            boolean sintonizadorTDT) {
        super(precioBase, color, consumo, peso);
        this.resolucion = resolucion;
        this.sintonizadorTDT = sintonizadorTDT;
    }
    //get de atributos
    public int getResolucion() {
        return resolucion;
    }
    public boolean isSintonizadorTDT() {
        return sintonizadorTDT;
    }
    
    public float precioFinal(){
        float precioFinalTV = super.precioFinal();
        if (this.resolucion > 40) {
            precioFinalTV += precioFinalTV * 0.3;
        }
        if (this.sintonizadorTDT) {
            precioFinalTV += 50;
        }
        return precioFinalTV;
    }
}