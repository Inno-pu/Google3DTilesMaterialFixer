#
# Created by Jippe Heijnen on 09-12-2023.
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


class SetViewportColorAsMaterialColor(types.Operator):
    bl_idname = 'test.viewport_color_as_material_color'
    bl_label = 'Convert IFC viewport color to material color'


    # this gets executed when the user presses the menu button.
    def execute(self, context):
        counter: int = 0
        if context.object:
            selection = context.selected_objects
            for obj in selection:
                for mat_item in obj.material_slots:
                    try:
                        mat: data.materials = mat_item.material
                        # inputs[0].default_value here is the base color
                        input = mat.node_tree.nodes['Principled BSDF'].inputs[0].default_value = mat.diffuse_color
                    except:
                        pass
                    counter+=1
            self.report({'INFO'}, f"{counter} Colors transferred.")
            print()

        return {'FINISHED'}

def draw_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(SetViewportColorAsMaterialColor.bl_idname, icon='MATERIAL')


def register():
    bpy.utils.register_class(SetViewportColorAsMaterialColor)
    bpy.types.UI_MT_button_context_menu.append(draw_menu)


def unregister():
    bpy.utils.unregister_class(SetViewportColorAsMaterialColor)


if __name__ == "__main__":
    register()