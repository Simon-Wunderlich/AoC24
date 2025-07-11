using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace main
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("AAAAAAAAAAAAAAAAAAAAAAAAAA");
			string textFile = "../../../input.txt";
			string text = File.ReadAllText(textFile);
			string pattern = "mul\\(\\d{1,3},\\d{1,33}\\)";
			Regex rg = new Regex(pattern);
			MatchCollection validMults = rg.Matches(text);
			int total = 0;
			foreach (Match match in validMults)
			{
				total += multiply(match.Value);
			}
			Console.WriteLine(total);
		}
		static int multiply(string text)
		{
			string pattern = "\\d{1,3}";
			Regex rg = new Regex(pattern);
			MatchCollection numbers = rg.Matches(text);

			return Int32.Parse(numbers.First().Value) * Int32.Parse(numbers.Last().Value);
		}
	}
}