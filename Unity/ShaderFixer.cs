using UnityEngine;
using UnityEditor;

public class ShaderFixer : EditorWindow
{
    [MenuItem("Tools/Fix shaders")]
    public static void ShaderFixerMethod()
    {
        GameObject[] selectedObjects = Selection.gameObjects;

        // loop through gameobjects
        foreach (GameObject gameObject in selectedObjects)
        {
            // loop through renderers 
            foreach (Renderer renderer in gameObject.GetComponents<Renderer>())
            {
                // loop through materials 
                foreach (Material material in renderer.materials)
                {
                    // get and set shader
                    Shader shader = material.shader;
                    if (shader.name != "Unlit/Texture")
                    {
                        material.shader = Shader.Find("Unlit/Texture");
                    }
                }
            }
        }
    }
}
