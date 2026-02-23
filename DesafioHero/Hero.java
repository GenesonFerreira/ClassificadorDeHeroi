public class Heroi {

    private String nome;
    private int idade;
    private String tipo;

    // Construtor
    public Heroi(String nome, int idade, String tipo) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo.toLowerCase(); // garante comparação correta
    }

    // Método atacar
    public void atacar() {
        String ataque;

        switch (tipo) {
            case "mago":
                ataque = "usou magia";
                break;
            case "guerreiro":
                ataque = "usou espada";
                break;
            case "monge":
                ataque = "usou artes marciais";
                break;
            case "ninja":
                ataque = "usou shuriken";
                break;
            default:
                ataque = "usou um ataque desconhecido";
                break;
        }

        System.out.println("O " + tipo + " atacou usando " + ataque);
    }

    // Método principal para teste
    public static void main(String[] args) {
        Heroi heroi1 = new Heroi("Arthus", 30, "guerreiro");
        Heroi heroi2 = new Heroi("Merlin", 150, "mago");
        Heroi heroi3 = new Heroi("Lee", 40, "monge");
        Heroi heroi4 = new Heroi("Ryu", 25, "ninja");

        heroi1.atacar();
        heroi2.atacar();
        heroi3.atacar();
        heroi4.atacar();
    }
}