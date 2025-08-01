namespace Day21
{
	internal class Program
	{
		static Dictionary<string, string> proximities = new Dictionary<string, string>
		{
			{"<", "<v^>A" },
			{"v", "v<^>A" },
			{">", ">vA^<" },
			{"^",  "^vA<>"},
			{"A", "A^>v<" }

		};
		static Dictionary<string, Key> numPad = new Dictionary<string, Key>();
		static Key zero = new Key("0");
		static Key one = new Key("1");
		static Key two = new Key("2");
		static Key three = new Key("3");
		static Key four = new Key("4");
		static Key five = new Key("5");
		static Key six = new Key("6");
		static Key seven = new Key("7");
		static Key eight = new Key("8");
		static Key nine = new Key("9");
		static Key numA = new Key("A");
		static Dictionary<string, Key> dirPad = new Dictionary<string, Key>();
		static Key left = new Key("<");
		static Key right = new Key(">");
		static Key up = new Key("^");
		static Key down = new Key("v");
		static Key dirA = new Key("A");
		static void Main(string[] args)
		{
			string textFile = "../../../input.txt";
			string[] text = File.ReadAllText(textFile).Split("\r\n");
			initNumPad();
			initDirPad();
			int total = 0;
			foreach (string line in text)
			{
				List<string> paths = getShortestPaths(getShortestPaths(getShortestPaths([line], numPad), dirPad), dirPad, true);
				total += paths[0].Length * getNum(line);
			}
			Console.WriteLine(total);
		}

		static int getNum(string input)
		{
			input = input.Replace("A", "");
			return int.Parse(input);
		}

		static void initDirPad()
		{
			left.connections = new Dictionary<string, Key>
			{
				{">", down }
			};
			dirPad.Add("<", left);
			down.connections = new Dictionary<string, Key>
			{
				{"<", left},
				{">", right },
				{"^", up }
			};
			dirPad.Add("v", down);
			up.connections = new Dictionary<string, Key>
			{
				{"v", down},
				{">", dirA }
			};
			dirPad.Add("^", up);
			right.connections = new Dictionary<string, Key>
			{
				{"<", down},
				{"^", dirA }
			};
			dirPad.Add(">", right);
			dirA.connections = new Dictionary<string, Key>
			{
				{"<", up},
				{"v", right }
			};
			dirPad.Add("A", dirA);
		}

		static void initNumPad()
		{
			numA.connections = new Dictionary<string, Key>
			{
				{ "<", zero },
				{ "^", three }
			};
			numPad.Add("A", numA);
			zero.connections = new Dictionary<string, Key>
			{
				{ "^" , two },
				{ ">", numA }
			};
			numPad.Add("0", zero);
			one.connections = new Dictionary<string, Key>
			{
				{ ">" , two },
				{ "^", four }
			};
			numPad.Add("1", one);
			two.connections = new Dictionary<string, Key>
			{
				{ "<" , one },
				{ "^", five },
				{ ">", three },
				{ "v", zero }
			};
			numPad.Add("2", two);
			three.connections = new Dictionary<string, Key>
			{
				{ "<" , two },
				{ "^", six },
				{ "v", numA }
			};
			numPad.Add("3", three);
			four.connections = new Dictionary<string, Key>
			{
				{ "v" , one },
				{ ">", five },
				{ "^", seven }
			};
			numPad.Add("4", four);
			five.connections = new Dictionary<string, Key>
			{
				{ "v" , two},
				{ ">", six },
				{ "^", eight},
				{ "<", four }
			};
			numPad.Add("5", five);
			six.connections = new Dictionary<string, Key>
			{
				{ "v" , three},
				{ "^", nine},
				{ "<", five }
			};
			numPad.Add("6", six);
			seven.connections = new Dictionary<string, Key>
			{
				{ "v" , four},
				{ ">", eight}
			};
			numPad.Add("7", seven);
			eight.connections = new Dictionary<string, Key>
			{
				{ "v" , five},
				{ ">", nine},
				{ "<", seven }
			};
			numPad.Add("8", eight);
			nine.connections = new Dictionary<string, Key>
			{
				{ "v" , six},
				{ "<", eight }
			};
			numPad.Add("9", nine);
		}

		static List<string> navToKey(string start, string targetChar, Dictionary<string, Key> pad)
		{
			List<string> solutions = new List<string>();
			if (start == targetChar)
			{
				return ["A"];
			}
			Queue<string[]> queue = new Queue<string[]>();
			queue.Enqueue(new string[] { start, "A" });

			while (queue.Count > 0)
			{
				string[] current = queue.Dequeue();
				string path = current[0];
				string steps = current[1];
				if (path.Contains("ERROR"))
					continue;
				if (solutions.Count > 0)
				{
					if (path.Length > solutions[0].Length + 1)
						continue;
				}

				string state = path[path.Length - 1].ToString();
				foreach (char dir in proximities[steps[steps.Length - 1].ToString()])
				{
					string newKey = pad[state].getNewState(dir.ToString());
					if (newKey == targetChar)
					{
						if (steps.Length == 1)
							solutions.Add(dir.ToString() + "A");
						else
							solutions.Add(steps[1..] + dir.ToString() + "A");
					}
					if (newKey != "ERROR" && !path.Contains(newKey))
						queue.Enqueue([path + newKey, steps + dir]);
				}
			}
			return solutions;
		}
		static List<string> getPath(string num, Dictionary<string, Key> pad)
		{
			List<string> path = new List<string>() { "" };
			string prevChar = "A";
			foreach (char c in num)
			{
				List<string> _Paths = new List<string>();
				List<string> newPaths = navToKey(prevChar, c.ToString(), pad);
				foreach (string paths in path)
				{
					foreach (string newPath in newPaths)
					{
						_Paths.Add(paths + newPath);
					}
				}
				path = _Paths;
				prevChar = c.ToString();
			}
			return path;
		}
		static string getFinalPath(string num, Dictionary<string, Key> pad)
		{
			string path = "";
			string prevChar = "A";
			foreach (char c in num)
			{
				List<string> _Paths = new List<string>();
				List<string> newPaths = navToKey(prevChar, c.ToString(), pad);
				string min = "";
				foreach (string _path in newPaths)
				{
					if (_path.Length < min.Length || min == "")
						min = _path;
				}
				path += min;
				prevChar = c.ToString();
			}
			return path;
		}
		static List<string> getShortestPaths(List<string> paths, Dictionary<string, Key> pad, bool final = false)
		{
			List<string> newPaths = new List<string>();
			foreach (string path in paths)
			{
				if (final)
					newPaths.Add(getFinalPath(path, pad));
				else
					newPaths.AddRange(getPath(path, pad));
			}
			int min = int.MaxValue;
			foreach (string path in newPaths)
			{
				if (path.Length < min)
					min = path.Length;
			}
			//List<string> g = newPaths.Where(_ => _.Length == min).ToList();
			//Console.WriteLine(string.Join("\n",g));
			return newPaths.Where(_ => _.Length <= min + 1).ToList();
		}

	}

	internal class Key
	{
		public string key;
		public Dictionary<string, Key> connections = new Dictionary<string, Key>();

		public Key(string state)
		{
			key = state;
		}

		public string getNewState(string dir)
		{
			if (connections.ContainsKey(dir))
				return connections[dir].key;
			return "ERROR";
		}
	}
}