import java.util.ArrayList;
import java.util.Random;
import java.util.Stack;

public class Juego {

    private int id;
    private String name;
    private ArrayList<Jugador> juadores;
    private Stack<Carta> deck;

    public Juego(){

    }

    public void iniciarDeck(){
        int guard1 = 5;
        int priest2 = 2;
        int baron3 = 2;
        int handmaid4 = 2;
        int prince5 = 2;
        int king6 = 1;
        int countes7 = 1;
        int princess8 = 1;

        Random rand = new Random();
        int select = -1;

                = rand.nextInt(7);

        Carta comodin = new Carta();

        boolean lleno=true;
        while(lleno){
            
        }



    }



}
