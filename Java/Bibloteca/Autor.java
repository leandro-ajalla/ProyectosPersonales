public class Autor {
    private String name;
    private String email;
    private char gender;
    // Constructor
    public Autor(String name, String email, char gender){
    this.name = name;
    this.email = email;
    this.gender = gender;
}

    //Getters
    public String getName(){
    return name;
}
    public String getEmail(){
    return email;
}
    public char getGender(){
    return gender;
}

    //Setter
    public void setEmail(String email){
        this.email = email;
    }

    // toString
    @Override
    public String toString(){
        return "Autor [nombre=" + name + ",email=" + email + ", genero=" + gender + "]";

    }
}