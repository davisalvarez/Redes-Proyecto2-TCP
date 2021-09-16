import java.util.*;

public class Juego {

    private int id;
    private String name;
    private ArrayList<Jugador> juadores;
    private Stack<Carta> deck;

    public Juego(){
        this.deck = new Stack<>();
        this.juadores = new ArrayList<>();
    }

    public void iniciarDeck(){
        Carta comodin = new Carta();

        for (int guard1 = 5; guard1>0; guard1--){
            this.deck.push(comodin.cartaGuard());
        }
        for (int priest2 = 2; priest2>0; priest2--){
            this.deck.push(comodin.cartaPriest());
        }
        for (int baron3 = 2; baron3>0; baron3--){
            this.deck.push(comodin.cartaBaron());
        }
        for (int handmaid4 = 2; handmaid4>0; handmaid4--){
            this.deck.push(comodin.cartaHandmaid());
        }
        for (int prince5 = 2; prince5>0; prince5--){
            this.deck.push(comodin.cartaPrince());
        }
        for (int king6 = 1; king6>0; king6--){
            this.deck.push(comodin.cartaKing());
        }
        for (int countes7 = 1; countes7>0; countes7--){
            this.deck.push(comodin.cartaCountess());
        }
        for (int princess8 = 1; princess8>0; princess8--){
            this.deck.push(comodin.cartaPrincess());
        }

        Collections.shuffle(deck);

/*        //ver orden de las cartas
        int count = 0;
        while(!deck.empty()){
            count++;
            System.out.print(count+" - ");
            System.out.println(deck.pop().getName());
        }*/
    }

    public void iniciarPartida(){
        //quitamos la primer carta
        this.deck.pop();



    }

    public void agregarJugador(Jugador player1){
        this.juadores.add(player1);
    }


}
