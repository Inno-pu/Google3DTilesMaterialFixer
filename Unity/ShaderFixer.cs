using UnityEngine;
using UnityEditor;

public class ShaderFixer : EditorWindow
{
    [MenuItem("Tools/Fix shaders")]
    public static void ShaderFixerMethod() 
    {
        GameObject[] selectedObjects = Selection.gameObjects;
        Debug.Log(selectedObjects.Length);

        foreach (GameObject gameObject in selectedObjects)
        {
            Renderer renderer = gameObject.GetComponent<Renderer>();
            if (renderer != null)
            {
                Shader shader = renderer.sharedMaterial.shader;
                if (shader.name != "Unlit/texture") 
                {
                    renderer.sharedMaterial.shader = Shader.Find("Unlit/Texture");
                }
            }
        }
    }
}
