using UnityEngine;

public class TileMouseListener : MonoBehaviour
{
    private Color original;

    // Start is called before the first frame update
    void Start()
    {
        original = GetComponent<Renderer>().material.color;
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnMouseDown()
    {
        var block = (GameObject) Resources.Load("/Assets/Assets/Prefabs/ConstructionStruts.prefab", typeof(GameObject));

        Debug.Log($"Clicked tile at: {GetComponent<MeshFilter>().transform.position}");
        Instantiate(block, GetComponent<MeshFilter>().transform.position, Quaternion.identity);
    }

    void OnMouseOver()
    {
        GetComponent<Renderer>().material.color = new Color(0.25f, 0.25f, 0.5f, 0.5f);
    }

    void OnMouseExit()
    {
        GetComponent<Renderer>().material.color = original;
    }
}
