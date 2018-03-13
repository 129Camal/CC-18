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

    public InetAddress getIpServer() {
        return ipServer;
    }

    public void setIpServer(InetAddress ipServer) {
        this.ipServer = ipServer;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public float getRTT() {
        return RTT;
    }

    public void setRTT(float RTT) {
        this.RTT = RTT;
    }

    public float getRAM() {
        return RAM;
    }

    public void setRAM(float RAM) {
        this.RAM = RAM;
    }

    public float getCPU() {
        return CPU;
    }

    public void setCPU(float CPU) {
        this.CPU = CPU;
    }

    public float getLargBanda() {
        return largBanda;
    }

    public void setLargBanda(float largBanda) {
        this.largBanda = largBanda;
    }
}
