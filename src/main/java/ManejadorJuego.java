import java.util.ArrayList;

public class ManejadorJuego {
    private static ManejadorJuego instance = null;

    private ArrayList<Juego> salas;

    public static ManejadorJuego getInstance(){
        if (instance==null)
            instance = new ManejadorJuego();
        return instance;
    }

    public void repartirCarta(Juego juego, Jugador readyP1, Carta carta){
        int id = readyP1.getId(); // a donde va
        int card = carta.getStrength(); // que carta es

        //Acá manda por Socket
    }
}
