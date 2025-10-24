using System;

class Program
{
    static void Main()
    {
        string palavra;
        int contadorVogais = 0;
        
        Console.Write("Digite uma palavra: ");
        palavra = Console.ReadLine();
        
        for(int i = 0; i < palavra.Length; i++)
        {
            char letra = palavra[i];
            
            if(letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u' ||
               letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U')
            {
                contadorVogais++;
            }
        }
        
        Console.WriteLine($"A palavra '{palavra}' possui {contadorVogais} vogais.");
    }
}