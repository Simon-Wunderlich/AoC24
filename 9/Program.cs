using System.Numerics;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;

namespace ConsoleApp3
{
	internal class Program
	{
		static void Main(string[] args)
		{
			string textFile = "../../../input.txt";
			string text = File.ReadAllText(textFile);
			string[] blocks = convToBlocks(text.ToArray());
			string[] compressedBlocks = compress(blocks);
			long total = calc(compressedBlocks);
			Console.WriteLine(total);
		}
		static string[] convToBlocks(char[] blocks)
		{
			string[] result = [];
			for (int i = 0; i < blocks.Length; i++)
			{
				string blockChar = "";
				if (i % 2 == 0)
					blockChar = (i / 2).ToString();
				else
					blockChar = ".";
				for (int j = 0; j < int.Parse(blocks[i].ToString()); j++)
				{
					result = result.Append(blockChar.ToString()).ToArray();
				}
			}
			return result;
		}

		static string[] compress(string[] blocks)
		{
			for (int i = 0; i < blocks.Length; i++)
			{
				if (blocks[i] != ".")
					continue;
				for (int j = blocks.Length - 1; j > i; j--)
				{
					if (blocks[j] == ".")
						continue;
					//Swap positions
					(blocks[i], blocks[j]) = (blocks[j], blocks[i]);
					break;
				}
			}
			return blocks;
		}
		static long calc(string[] blocks)
		{
			long total = 0;
			for (long i = 0; i < blocks.Length; i++)
			{
				if (blocks[i] == ".")
					break;
				total += int.Parse(blocks[i]) * i;
			}
			return total;
		}
	}
}
