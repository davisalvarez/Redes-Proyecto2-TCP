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


    public Carta cartaGuard(){
        Carta naipe = new Carta();
        this.name = "Guardia";
        this.strength = 1;
        return naipe;
    }
    public Carta cartaPriest(){
        Carta naipe = new Carta();
        this.name = "Clérigo";
        this.strength = 2;
        return naipe;
    }
    public Carta cartaBaron(){
        Carta naipe = new Carta();
        this.name = "Barón";
        this.strength = 3;
        return naipe;
    }
    public Carta cartaHandmaid(){
        Carta naipe = new Carta();
        this.name = "Sirvienta";
        this.strength = 4;
        return naipe;
    }
    public Carta cartaPrince(){
        Carta naipe = new Carta();
        this.name = "Principe";
        this.strength = 5;
        return naipe;
    }
    public Carta cartaKing(){
        Carta naipe = new Carta();
        this.name = "Rey";
        this.strength = 6;
        return naipe;
    }
    public Carta cartaCountess(){
        Carta naipe = new Carta();
        this.name = "Condesa";
        this.strength = 7;
        return naipe;
    }
    public Carta cartaPrincess(){
        Carta naipe = new Carta();
        this.name = "Pricesa";
        this.strength = 8;
        return naipe;
    }
}
