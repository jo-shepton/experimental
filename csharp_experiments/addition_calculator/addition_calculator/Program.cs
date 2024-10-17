// takes user input and stores it
// datatype is string, variable is userInput
Console.WriteLine("Enter a number");
var userInput = float.Parse(Console.ReadLine());
Console.WriteLine("Enter another");
var userInput2 = float.Parse(Console.ReadLine());

float added_values  = userInput + userInput2;
Console.WriteLine("These add up to " + added_values);
Console.ReadKey();  
