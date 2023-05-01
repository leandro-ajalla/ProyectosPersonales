public class Punto {
    private float posicionX;
    private float posicionY;

    public Punto() {
    }
    public Punto(float posicionX, float posicionY) {
        this.posicionX = posicionX;
        this.posicionY = posicionY;
    }
    public float getPosicionX() {
        return posicionX;
    }
    public void setPosicionX(float posicionX) {
        this.posicionX = posicionX;
    }
    public float getPosicionY() {
        return posicionY;
    }
    public void setPosicionY(float posicionY) {
        this.posicionY = posicionY;
    }
    
    public double calcularDistancia(Punto otroPunto){
        float distanciaRelativaX = this.posicionX - otroPunto.getPosicionX();
        float distanciaRelativaY = this.posicionY - otroPunto.getPosicionY();
        double distancia = Math.sqrt(Math.pow(distanciaRelativaX, 2) + Math.pow(distanciaRelativaY, 2));
        return distancia;
    }
}