public class ManejadorJugador {
    private Jugador myself;
    private int idJuego;

    private static ManejadorJugador instance = null;
    public static ManejadorJugador getInstance(){
        if (instance==null)
            instance = new ManejadorJugador();
        return instance;
    }

    private ManejadorJugador(){
        this.myself = new Jugador();
    }

    public void recibirCarta(){

    }

    public void elegirNombre(String nombre){
        this.myself.setNombre(nombre);
    }

    public void unirseAJuego(){

        //aca se comunica con el servidor y lo mete a un juego
        Cliente.getInstance().unirseAPartida();

    }



}
