import bpy
import os
#the only difference between this version and the other one is that this one remove the mirror 
#modifier if there is only mesh, this is useful to import on apps like substance painter which is my workflow.  

pathWay = bpy.data.filepath

objs = bpy.context.selected_objects
nameWay = os.path.splitext(pathWay)[0]

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):
    def draw(self, context):
        self.layout.label(text = message)
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

types = set([obj.type for obj in objs])
print(f'saw types: {types}', nameWay,)


if 'ARMATURE' in types and 'MESH' in types:
    theCall = 'Mesh with armature exported'
    fileName = nameWay + '_armaMesh.fbx'
    objINCLUDE = {'ARMATURE','MESH','OTHER'}
    bake = False
elif 'MESH' in types:
    theCall = 'only meshes exported'
    fileName = nameWay + '_meshOnly.fbx'
    objINCLUDE = {'MESH','OTHER'}
    bake = False
    obj.modifiers.remove(type='MIRROR')
else:
    theCall = 'Only armature, and animations axported'
    fileName = nameWay + '_armaAnim.fbx'
    objINCLUDE = {'ARMATURE','OTHER'}
    bake = True

print(fileName,objINCLUDE,bake,nameWay)
print(nameWay) #test print if my set of variables are working

bpy.ops.export_scene.fbx(use_selection = True ,
path_mode = 'RELATIVE',
filepath = fileName ,
 use_armature_deform_only = True,
  add_leaf_bones = False,
  object_types = objINCLUDE ,
   axis_forward ='Z',
    bake_anim = bake ,
    bake_anim_use_all_bones = True)


ShowMessageBox(theCall)
#this piece of shit code is made by bento césar (@gostbento everywhere)
#with help from some guys from discord
#feel free to use it however you like
#if this breaks anything it is not my fault. be safe eat salad.
