using Assets.Scripts;
using UnityEngine;

public class RenderAsteroid : MonoBehaviour
{
    private Asteroid asteroid;

    // Start is called before the first frame update
    void Start()
    {
        asteroid = new Asteroid();

        for (int x = 0; x < asteroid.Length; x++)
        {
            for (int z = 0; z < asteroid.Width; z++)
            {
                if (asteroid.tiles[x * z] == 0x1)
                {
                    GameObject tile = GameObject.CreatePrimitive(PrimitiveType.Plane);
                    tile.transform.position = new Vector3(x, 0, z);
                    tile.transform.localScale = new Vector3(0.1f, 0.1f, 0.1f);
                    var colour = Random.ColorHSV(0, 1, 0, 0, 0.5f, 0.75f);
                    tile.GetComponent<Renderer>().material.color = colour;
                    tile.AddComponent<TileMouseListener>();
                }
            }
        }

        Debug.Log($"{asteroid.Name}");
    }

    // Update is called once per frame
    void Update()
    {

    }
}
