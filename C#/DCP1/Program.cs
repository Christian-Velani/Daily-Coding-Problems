// This problem was recently asked by Google.

// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

// Bonus: Can you do this in one pass?

int k = 17;
List<int> numbers = new List<int> {25, 5, 9, 2};

static string TemSoma(List<int> numbers, int k)
{
    foreach (int number in numbers)
    {
        if (numbers.Contains(k - number))
        {
            return "É possivel alcançar k utilizando 2 números da lista";
        }
    }
    return "Não existe soma que gere k";
}

Console.WriteLine(TemSoma(numbers, k));