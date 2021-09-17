import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class Servidor {

    private ServerSocket servidor;
    private Socket canal;

    private static Servidor instance = null;
    public static Servidor getInstance(){
        if (instance==null)
            instance = new Servidor();
        return instance;
    }

    private Servidor(){
        try{
            this.servidor = new ServerSocket(6666);
            this.canal = servidor.accept();
        }catch(Exception e){System.out.println(e);}
    }

    public void recibirMensaje(){
        try {
            DataInputStream dis=new DataInputStream(canal.getInputStream());
            String  str=(String)dis.readUTF();
            System.out.println("message= "+str);
        }catch (IOException e){System.out.println(e);}
    }

    public void cerrarServer() throws IOException {
        try {
            servidor.close();
        }catch (IOException e){System.out.println(e);}
    }

    public void repartirCarta(Juego juego, Jugador readyP1){
        int id = readyP1.getId(); // a donde va
        int card = readyP1.getRightHand().getStrength(); // que carta es

        //Acá manda por Socket
    }

    public static void main(String[] args){
        try{
            ServerSocket ss=new ServerSocket(6666);
            Socket s=ss.accept();//establishes connection
            DataInputStream dis=new DataInputStream(s.getInputStream());
            String  str=(String)dis.readUTF();
            System.out.println("message= "+str);
            ss.close();
        }catch(Exception e){System.out.println(e);}
    }


} 