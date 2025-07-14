using System.Numerics;
using System.Runtime.CompilerServices;

internal class Program
{
	static void Main(string[] args)
	{
		string textFile = "../../../input.txt";
		string text = File.ReadAllText(textFile);
		string[] map = text.Split("\r\n");

		Vector2 direction = new Vector2(0, -1);
		Vector2 position = new Vector2();
		int index = text.Replace("\r\n", "").IndexOf("^");
		position.X = index % map[0].Length;
		position.Y = float.Floor((float)index / map[0].Length);

		int uniquePositions = 0;

		Vector2 nextPos = position + direction;
		bool isRunning = true;
		while (isRunning)
		{
			while (map[(int)nextPos.Y][(int)nextPos.X] != '#')
			{
				if (map[(int)nextPos.Y][(int)nextPos.X] != 'X')
					uniquePositions++;
				System.Text.StringBuilder strBuilder = new System.Text.StringBuilder(map[(int)nextPos.Y]);
				strBuilder[(int)nextPos.X] = 'X';
				map[(int)nextPos.Y] = strBuilder.ToString();
				position = nextPos;
				nextPos = position + direction;
				if (!isInBounds(nextPos, map))
				{
					uniquePositions++;
					isRunning = false;
					break;
				}
			}
			direction = new Vector2(-direction.Y, direction.X);
			nextPos = position + direction;
			if (!isInBounds(nextPos, map))
			{
				uniquePositions++;
				break;
			}
		}
		Console.WriteLine(uniquePositions);
	}

	static bool isInBounds(Vector2 position, string[] map)
	{
		return float.Clamp(position.X, 0, map[0].Length - 1) == position.X && float.Clamp(position.Y, 0, map.Length - 1) == position.Y;
	}

}