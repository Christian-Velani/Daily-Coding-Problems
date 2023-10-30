public class No
{
    public string raiz;
    public No direita;
    public No esquerda;

    public No(string raiz, No esquerda = null, No direita = null)
    {
        this.raiz = raiz;
        this.esquerda = esquerda;
        this.direita = direita;
    }
}