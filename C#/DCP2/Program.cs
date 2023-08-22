// This problem was asked by Uber.

// Given an array of integers, return a new array such that each element at index i 
// of the new array is the product of all the numbers in the original array except the one at i.

// For example, if our input was [1, 2, 3, 4, 5], the expected output 
// would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

// Follow-up: what if you can't use division?

List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 1};

static List<int> ListaMult(List<int> numeros)
{
    List<int> numeros2 = new List<int>();
    for (int n = 0; n < numeros.Count; n++)
    {
        int n2 = 1;
        for (int n3 = 0; n3 < numeros.Count; n3++)
        {
            if (n3 != n)
            {
                n2 *= numeros[n3];
            }
        }
        numeros2.Add(n2);
    }
    return numeros2;
}

Console.WriteLine(string.Join(", ", ListaMult(numeros)));
