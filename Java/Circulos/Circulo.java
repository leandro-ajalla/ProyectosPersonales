public class Circulo {
    private Punto centro;
    private float radio;
    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }
    public Punto getCentro() {
        return centro;
    }
    public void setCentro(Punto centro) {
        this.centro = centro;
    }
    public float getRadio() {
        return radio;
    }
    public void setRadio(float radio) {
        this.radio = radio;
    }
    public boolean seTocan(Circulo otroCirculo){
        float sumaRadios = this.radio + otroCirculo.radio;
        double distancia = this.centro.calcularDistancia(otroCirculo.centro);
        return distancia <= sumaRadios;
    }
}