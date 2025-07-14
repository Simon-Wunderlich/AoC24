using System.Numerics;
using System.Runtime.CompilerServices;

namespace ConsoleApp3
{
	internal class Program
	{
		static Dictionary<string, char> directions = new Dictionary<string, char>()
		{
			["0-1"] = 'U',
			["01"] = 'D',
			["-10"] = 'L',
			["10"] = 'R'
		};
		static List<string> obstructions = new List<string>();
		static void Main(string[] args)
		{
			string textFile = "../../../input.txt";
			string text = File.ReadAllText(textFile);
			string[] lines = text.Split("\r\n");
			string[][] map = [];
			foreach (string line in lines)
			{
				map = map.Append(line.ToCharArray().Select(c => c.ToString()).ToArray()).ToArray();
			}


			Vector2 direction = new Vector2(0, -1);
			Vector2 position = new Vector2();
			int index = text.Replace("\r\n", "").IndexOf("^");
			position.X = index % lines[0].Length;
			position.Y = float.Floor((float)index / lines[0].Length);



			Vector2 nextPos = position + direction;
			bool isRunning = true;
			while (isRunning)
			{
				while (map[(int)nextPos.Y][(int)nextPos.X] != "#")
				{

					if (map[(int)nextPos.Y][(int)nextPos.X] == ".")
						checkLoop(nextPos, position, direction, map);
					map[(int)nextPos.Y][(int)nextPos.X] += directions[$"{direction.X}{direction.Y}"];
					position = nextPos;
					nextPos = position + direction;
					if (!isInBounds(nextPos, map))
					{
						isRunning = false;
						break;
					}
				}
				direction = rotate(direction);
				nextPos = position + direction;
				if (!isInBounds(nextPos, map))
				{
					break;
				}
			}
			Console.WriteLine(obstructions.Count);
		}

		static void checkLoop(Vector2 nextPos, Vector2 pos, Vector2 direction, string[][] map)
		{
			string[][] modMap = map.Select(a => a.Select(b => (string)b.Clone()).ToArray()).ToArray();
			Vector2 rotatedDir = direction;
			Vector2 modPos = pos;
			Vector2 checkPos = modPos;
			Vector2 blockPos = nextPos;
			modMap[(int)blockPos.Y][(int)blockPos.X] = "#";

			if (!isInBounds(checkPos, modMap))
				return;

			bool loopFound = false;
			while (!loopFound)
			{
				rotatedDir = rotate(rotatedDir);
				checkPos = modPos + rotatedDir;
				if (!isInBounds(nextPos, modMap))
				{
					break;
				}
				while (true)
				{
					if (!isInBounds(checkPos, modMap))
						return;
					if (modMap[(int)checkPos.Y][(int)checkPos.X].Contains("#"))
						break;
					if (modMap[(int)checkPos.Y][(int)checkPos.X].Contains(directions[$"{rotatedDir.X}{rotatedDir.Y}"]))
					{
						loopFound = true;
						break;
					}
					modMap[(int)checkPos.Y][(int)checkPos.X] += directions[$"{rotatedDir.X}{rotatedDir.Y}"];
					modPos = checkPos;
					checkPos = checkPos + rotatedDir;
				}
			}

			if (!isInBounds(blockPos, modMap))
				return;
			if (!obstructions.Contains($"{blockPos.X}, {blockPos.Y}"))
				obstructions.Add($"{blockPos.X}, {blockPos.Y}");
			Console.WriteLine($"{blockPos.X}, {blockPos.Y}");
		}

		static Vector2 rotate(Vector2 vec)
		{
			vec = new Vector2(-vec.Y, vec.X);
			vec.X = vec.X == -0 ? 0 : vec.X;
			vec.Y = vec.Y == -0 ? 0 : vec.Y;
			return vec;
		}

		static bool isInBounds(Vector2 position, string[][] map)
		{
			return float.Clamp(position.X, 0, map[0].Length - 1) == position.X && float.Clamp(position.Y, 0, map.Length - 1) == position.Y;
		}

	}
}
