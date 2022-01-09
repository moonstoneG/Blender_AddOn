bl_info = {
    "name": "TextTool_Plugin",
    "author": "Astro_MoonStone",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Simply add a text at scene.",
    "warning": "",
    "doc_url": "",
    "category": "Add Text",
}


import bpy

class TextTool(bpy.types.Panel):
    bl_label = "Text Tool"
    bl_idname = "OBJECT_PT_TextTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Create A new text'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("wm.textop",text = "Add Text")







class WM_OP_Text(bpy.types.Operator):
    bl_label = "Text Tool"
    bl_idname = "wm.textop"

    text = bpy.props.StringProperty(name = "Enter Text:")
    scale = bpy.props.FloatProperty(name = "Scale:",default = 1)
    #center = bpy.props.BoolProperty(name = "Center Origin",default = False)
    
    def execute(self,context):
        t = self.text
        s = self.scale
        #c = self.center
        bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(0, 0, 0))
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        bpy.ops.font.text_insert(text = t)
        bpy.ops.object.editmode_toggle()
        
            
        
        return{'FINISHED'}
    
    def invoke(self,context,event):
        return context.window_manager.invoke_props_dialog(self)
        
    






def register():
    bpy.utils.register_class(TextTool)
    bpy.utils.register_class(WM_OP_Text)

def unregister():
    bpy.utils.unregister_class(TextTool)
    bpy.utils.unregister_class(WM_OP_Text)


if __name__ == "__main__":
    register()
