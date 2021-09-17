import java.io.*;
import java.net.*;
public class Cliente {

    private Socket socket;

    private static Cliente instance = null;
    public static Cliente getInstance(){
        if (instance==null)
            instance = new Cliente();
        return instance;
    }

    private Cliente(){

    }

    public void unirseAPartida(){
        //acá pide al servidor que lo meta a un juego.

    }

    public static void main(String[] args) {
        try{
            Socket s=new Socket("localhost",6666);
            DataOutputStream dout=new DataOutputStream(s.getOutputStream());
            dout.writeUTF("Hello Server");
            dout.flush();
            dout.close();
            s.close();
        }catch(Exception e){System.out.println(e);}
    }

    public void iniciarSocket(){
        /*try{
            Socket
        }*/
    }
}
