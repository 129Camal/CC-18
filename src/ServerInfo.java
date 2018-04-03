import java.io.Serializable;
import java.net.InetAddress;

public class ServerInfo implements Serializable {

    private InetAddress ipServer;
    private int port;
    private float RTT;
    private float RAM;
    private float CPU;
    private float largBanda;

    public ServerInfo(InetAddress ipServer, int port, float RTT, float RAM, float CPU, float largBanda) {
        this.ipServer = ipServer;
        this.port = port;
        this.RTT = RTT;
        this.RAM = RAM;
        this.CPU = CPU;
        this.largBanda = largBanda;
    }

    public synchronized InetAddress getIpServer() {
        return ipServer;
    }

    public synchronized void setIpServer(InetAddress ipServer) {
        this.ipServer = ipServer;
    }

    public synchronized int getPort() {
        return port;
    }

    public synchronized void setPort(int port) {
        this.port = port;
    }

    public synchronized float getRTT() {
        return RTT;
    }

    public synchronized void setRTT(float RTT) {
        this.RTT = RTT;
    }

    public synchronized float getRAM() {
        return RAM;
    }

    public synchronized void setRAM(float RAM) {
        this.RAM = RAM;
    }

    public synchronized float getCPU() {
        return CPU;
    }

    public synchronized void setCPU(float CPU) {
        this.CPU = CPU;
    }

    public synchronized float getLargBanda() {
        return largBanda;
    }

    public synchronized void setLargBanda(float largBanda) {
        this.largBanda = largBanda;
    }
}
