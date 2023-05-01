public class Libro {
    // Atributos
    private String name;
    private Author author;
    private double price;
    private int quantity;

    // Constructor
    public Libro (String name, Author author, double price){
        this.name = name;
        this.author = author;
        this.price= price;
    }
    public Libro(String name, Author author, double price, int quantity){
        this.name = name;
        this.author = author;
        this.price= price;
        this.quantity = quantity;
    }
   
    //Getters
    public String getName(){
        return name;
    }
    public Author getAuthor(){
        return author;
    }
    public double getPrice(){
        return price;    
    }
    public int getQuantity(){
        return quantity;
    }

    //Setters
    public void setPrice(double price ){
        this.price= price;
    }
    public void setQuantity(int quantity){
        this.quantity = quantity;
    }

    //ToString
    @Override
    public String toString(){
        return "Libro [nombre="+ name + "autor="+ author + "precio=" + price + "cantidad="+ quantity + "]";
    }
}   