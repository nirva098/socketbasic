import java.io.*;  
import java.net.*;  
public class Client {
	public static void main(String[] args) {  
		try{      
			Socket s=new Socket("localhost",2000);  
			DataOutputStream dout=new DataOutputStream(s.getOutputStream());  
			dout.writeUTF("Hello python server, this is java Client");  
			dout.flush();  
			dout.close();  
			s.close();  
		}
		catch(Exception e){
			System.out.println(e);
		}  
	}
}