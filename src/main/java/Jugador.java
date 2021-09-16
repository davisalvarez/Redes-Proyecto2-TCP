import java.util.ArrayList;

public class Jugador {
    private int id;
    private String nombre;
    private boolean alive;
    private Carta leftHand;
    private Carta rightHand;
    private ArrayList<Carta> discarded;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public boolean isAlive() {
        return alive;
    }

    public void setAlive(boolean alive) {
        this.alive = alive;
    }

    public Carta getLeftHand() {
        return leftHand;
    }

    public void setLeftHand(Carta leftHand) {
        this.leftHand = leftHand;
    }

    public Carta getRightHand() {
        return rightHand;
    }

    public void setRightHand(Carta rightHand) {
        this.rightHand = rightHand;
    }

    public ArrayList<Carta> getDiscarded() {
        return discarded;
    }

    public void setDiscarded(ArrayList<Carta> discarded) {
        this.discarded = discarded;
    }
}
