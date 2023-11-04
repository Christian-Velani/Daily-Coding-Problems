// This problem was asked by Google;

// Given the root to a binary tree, implement serialize(root), 
// which serializes the tree into a string, and deserialize(s), 
// which deserializes the string back into the tree.
// For example, given the following Node class

// class Node:
//     def __init__(self, val, left=None, right=None):
//         self.val = val
//         self.left = left
//         self.right = right

// The following test should pass:

// node = Node('root', Node('left', Node('left.left')), Node('right'))
// assert deserialize(serialize(node)).left.left.val == 'left.left'
string Serializar(No no, char separador)
{
    string noSerializado = "";
    noSerializado += no.raiz;

    if (no.esquerda != null)
    {
        noSerializado += (separador == '-' ? ',' : '-') + Serializar(no.esquerda, separador == '-' ? ',' : '-');
    }

    if (no.direita != null)
    {
        noSerializado += (separador == '-' ? ',' : '-') + Serializar(no.direita, separador == '-' ? ',' : '-');
    }

    return noSerializado;
}

No Desserializar(string noSerializado, char separador)
{
    List<string> partes = new(noSerializado.Split(separador == '-' ? ',' : '-'));
    No no = new No(partes[0]);

    try
    {
        no.esquerda = Desserializar(partes[1], separador == '-' ? ',' : '-');
    }
    catch (System.ArgumentOutOfRangeException) { }

    try
    {
        no.direita = Desserializar(partes[2], separador == '-' ? ',' : '-');
    }
    catch (System.ArgumentOutOfRangeException) { }

    return no;

}
string MostrarArvore(No no, int nivel = 0)
{
    if (nivel == 0)
    {
        nivel = 1;
    }
    return ($"Raiz - Nível {nivel}: {no.raiz}\n" + $"Nó esquerdo - Nível {nivel}: {(no.esquerda != null ? MostrarArvore(no.esquerda, nivel + 1) : "Vazio")}\n" + $"Nó direita - Nível {nivel}: {(no.direita != null ? MostrarArvore(no.direita, nivel + 1) : "Vazio")}");
}
No no = new("raiz", new No("esquerda", new No("esquerda.esquerda")), new No("direita"));
string noSerializado = Serializar(no, '-');
Console.WriteLine(noSerializado);
No noDesserializado = Desserializar(noSerializado, '-');
Console.WriteLine(MostrarArvore(noDesserializado));
Console.WriteLine(noDesserializado.esquerda.esquerda.raiz == "esquerda.esquerda");