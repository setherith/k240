using UnityEngine;
using UnityEngine.UI;

public class IsoCamera : MonoBehaviour
{
    private Camera _cam;
    private Text _debugPanel;
    private GameObject _camPivot;

    // Start is called before the first frame update
    void Start()
    {
        _cam = GetComponent<Camera>();
        _cam.transform.position = new Vector3(-5, 10, -5);
        _cam.transform.rotation = Quaternion.Euler(25, 45, 0);
        _cam.orthographicSize = 7.5f;
        
        _camPivot = GameObject.Find("CameraPivot");

        _debugPanel = GameObject.Find("DebugPanel").GetComponent<Text>();
        UpdateDebugPanel();
    }

    // Update is called once per frame
    void Update()
    {
        var turning = Input.GetAxis("Horizontal");
        if (turning != 0)
            _camPivot.transform.Rotate(0, turning, 0);

        var zoom = Input.mouseScrollDelta.y;
        if (zoom != 0)
            if (_cam.orthographicSize > 0.1 && _cam.orthographicSize < 10)
                _cam.orthographicSize -= 0.1f * zoom;

        UpdateDebugPanel();
    }

    void UpdateDebugPanel()
    {
        _debugPanel.text = $"- - - Camera - - -\nPosition: {_cam.transform.position}\nRotation: {_cam.transform.rotation}";
    }
}
