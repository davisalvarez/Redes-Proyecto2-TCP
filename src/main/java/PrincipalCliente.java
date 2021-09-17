public class PrincipalCliente {
    public static void main(String args[]){

        ManejadorJugador.getInstance().elegirNombre("DavisGT");

        ManejadorJugador.getInstance().unirseAJuego();
    }
}
