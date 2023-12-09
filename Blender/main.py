#
# Created by Jippe Heijnen on 13-11-2023.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import bpy
from bpy import types
from bpy import context
from bpy import data


class Google3DTileMaterialFixer(types.Operator):
    bl_idname = 'test.material_fixer'
    bl_label = 'Convert materials to Principled BSDF'


    # this gets executed when the user presses the menu button.
    def execute(self, context):
        counter: int = 0
        if context.object:
            selection = context.selected_objects
            for obj in selection:
                for mat_item in obj.material_slots:
                    mat: data.materials = convert_shader(mat_item.material)
                    counter+=1
            self.report({'INFO'}, f"counter} 3D Tiles modified.")
            print()

        return {'FINISHED'}


def clean_material(mat: data.materials):

    mat.use_nodes = True
    if mat.node_tree:
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        links.clear()
        try:
            for node in nodes:
                if (node.name != "Image Texture" and node.name != "Material Output") and node.label != "BASE COLOR":
                    nodes.remove(nodes[node.name])
        except:
            # don't raise errors when a node is not found.
            pass

    return mat


def convert_shader(mat):
    new_mat = clean_material(mat)
    nodes = new_mat.node_tree.nodes
    links = new_mat.node_tree.links
    output = nodes['Material Output']
    shader = nodes.new(type='ShaderNodeBsdfPrincipled')
    
    input = None
    try:
        input = nodes['Image Texture']
        links.new(input.outputs[0], shader.inputs[0])
    except:
        pass

    links.new(shader.outputs[0], output.inputs[0])
    self.report({'INFO'}, f"Fixed {mat.name}.")
    return mat


def draw_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(Google3DTileMaterialFixer.bl_idname, icon='MATERIAL')


def register():
    bpy.utils.register_class(Google3DTileMaterialFixer)
    bpy.types.UI_MT_button_context_menu.append(draw_menu)


def unregister():
    bpy.utils.unregister_class(Google3DTileMaterialFixer)


if __name__ == "__main__":
    register()
