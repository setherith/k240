using System;

namespace Assets.Scripts
{
    public class Asteroid
    {
        private const int MAX_SIZE = 20;

        public string Name { get; set; }
        public int Width { get; set; }
        public int Length { get; set; }

        public byte[] tiles { get; set; }

        private Random rand;

        string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string numbers = "0123456789";

        public Asteroid()
        {
            rand = new Random();
            Name = GenerateName();

            Width = rand.Next(5, MAX_SIZE); // 5 or less is the smallest we want to go for building
            Length = rand.Next(5, MAX_SIZE);

            tiles = new byte[Width * Length];
            for (int t = 0; t < Width * Length; t++) {
                tiles[t] = 0x1;
            }
        }

        private string GenerateName()
        {
            string name = string.Empty;

            for (int l = 0; l < 10; l++)
                if (rand.NextDouble() >= 0.5)
                    name += alphabet.Substring(rand.Next(0, 25), 1);
                else
                    name += numbers.Substring(rand.Next(0, 9), 1);

            return name;
        }
    }
}