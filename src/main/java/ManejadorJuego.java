import java.util.ArrayList;
import java.util.Collections;

public class ManejadorJuego {
    private static ManejadorJuego instance = null;
    private int cJugadores;

    private ArrayList<Juego> salas;

    public static ManejadorJuego getInstance(){
        if (instance==null)
            instance = new ManejadorJuego();
        return instance;
    }

    public ManejadorJuego(){
        this.cJugadores = 0;
        this.salas = new ArrayList<>();
    }

    public void repartirCarta(Juego juego, Jugador readyP1){
        int id = readyP1.getId(); // a donde va
        int card = readyP1.getRightHand().getStrength(); // que carta es

        //Acá manda por Socket
    }

    public void asignarJugador(String nombre){
        Jugador nuevo = new Jugador();
        nuevo.setNombre(nombre);
        this.cJugadores++;
        nuevo.setId(this.cJugadores);

        boolean agregado = false;

        for (Juego partida: this.salas){
            if(partida.getJuadores().size()<=4) {
                partida.addJugador(nuevo);
                agregado = true;
            }
        }
        if (!agregado){
            Juego overWatch = new Juego();
            overWatch.addJugador(nuevo);
            this.salas.add(overWatch);
        }
    }

    public void iniciarPartida(){
        //quitamos la primer carta
        this.deck.pop();

        //Repartimos aleatoreamente las cartas a cada jugador
        Collections.shuffle(juadores);

        for (Jugador tracer: this.juadores){
            tracer.setRightHand(deck.pop());
            ManejadorJuego.getInstance().repartirCarta(this, tracer);
        }

    }
}
