public class Carta {
    private int id;
    private String name;
    private int strength;

    public Carta(int id, String name, int strength){
        this.id=id;
        this.name=name;
        this.strength=strength;
    }

    public Carta(){
        this.id=-1;
        this.name="";
        this.strength=0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getStrength() {
        return strength;
    }

    public void setStrength(int strength) {
        this.strength = strength;
    }

    public Carta cartaGuard(){
        Carta naipe = new Carta();
        naipe.name = "Guardia";
        naipe.strength = 1;
        return naipe;
    }
    public Carta cartaPriest(){
        Carta naipe = new Carta();
        naipe.name = "Clérigo";
        naipe.strength = 2;
        return naipe;
    }
    public Carta cartaBaron(){
        Carta naipe = new Carta();
        naipe.name = "Barón";
        naipe.strength = 3;
        return naipe;
    }
    public Carta cartaHandmaid(){
        Carta naipe = new Carta();
        naipe.name = "Sirvienta";
        naipe.strength = 4;
        return naipe;
    }
    public Carta cartaPrince(){
        Carta naipe = new Carta();
        naipe.name = "Principe";
        naipe.strength = 5;
        return naipe;
    }
    public Carta cartaKing(){
        Carta naipe = new Carta();
        naipe.name = "Rey";
        naipe.strength = 6;
        return naipe;
    }
    public Carta cartaCountess(){
        Carta naipe = new Carta();
        naipe.name = "Condesa";
        naipe.strength = 7;
        return naipe;
    }
    public Carta cartaPrincess(){
        Carta naipe = new Carta();
        naipe.name = "Pricesa";
        naipe.strength = 8;
        return naipe;
    }
}
