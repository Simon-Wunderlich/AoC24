using System.Diagnostics.Tracing;
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
			string[][] blocks = convToBlocks(text.ToArray());
			string[][] compressedBlocks = compress(blocks);
			long total = calc(compressedBlocks);
			Console.WriteLine(total);
		}
		static string[][] convToBlocks(char[] blocks)
		{
			string[][] result = [];
			for (int i = 0; i < blocks.Length; i++)
			{
				string blockChar = "";
				if (i % 2 == 0)
					blockChar = (i / 2).ToString();
				else
					blockChar = ".";
				string[] block = [];
				for (int j = 0; j < int.Parse(blocks[i].ToString()); j++)
				{
					block = block.Append(blockChar.ToString()).ToArray();
				}
				result = result.Append(block).ToArray();
			}
			return result;
		}

		static string[][] compress(string[][] blocks)
		{
			for (int j = blocks.Length - 1; j > 0; j--)
			{
				if (blocks[j].Length == 0)
					continue;
				if (string.Join("", blocks[j]).Contains("."))
					continue;
				for (int i = 0; i <= j; i++)
				{
					if (!string.Join("", blocks[i]).Contains("."))
						continue;
					if (blocks[i].Length == 0)
						continue;

					if (blocks[i].Length < blocks[j].Length)
						continue;
					//Swap positions
					string[] freeSpace = [];
					for (int k = 0; k < blocks[j].Length; k++)
					{
						freeSpace = freeSpace.Append(".").ToArray();
					}
					List<string[]> blockList = blocks.ToList();
					blockList.Insert(i, blocks[j]);
					blocks = blockList.ToArray();
					(blocks[i + 1], blocks[j + 1]) = (blocks[i + 1][blocks[j + 1].Length..], freeSpace);
					break;
				}
			}
			return blocks;
		}
		static long calc(string[][] blocks)
		{
			long total = 0;
			int blockNum = 0;
			for (int i = 0; i < blocks.Length; i++)
			{
				if (string.Join("", blocks[i]).Contains("."))
				{
					blockNum += string.Join("", blocks[i]).Length;
					continue;
				}
				foreach (string block in blocks[i])
				{
					total += int.Parse(block) * blockNum;
					blockNum++;

				}
			}
			return total;
		}
	}
}
