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

    private ManejadorJuego(){
        this.cJugadores = 0;
        this.salas = new ArrayList<>();
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

                if(partida.getJuadores().size()>=4) {
                    this.iniciarPartida(partida);
                }
                break;
            }
        }
        if (!agregado){
            Juego overWatch = new Juego();
            overWatch.addJugador(nuevo);
            this.salas.add(overWatch);
        }
    }

    public void iniciarPartida(Juego partida){

        //Repartimos aleatoreamente las cartas a cada jugador
        Collections.shuffle(partida.getJuadores());

        for (Jugador tracer: partida.getJuadores()){
            tracer.setRightHand(partida.getDeck().pop());
            Servidor.getInstance().repartirCarta(partida, tracer);
        }

    }
}
