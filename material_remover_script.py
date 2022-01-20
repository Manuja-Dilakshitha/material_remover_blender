import bpy

for material in bpy.data.materials:
    material.user_clear()
    bpy.data.materials.remove(material)
    
objects = bpy.context.scene.objects

for obj in objects:
    obj.active_material_index = 0
    
    for i in range(len(obj.material_slots)):
        bpy.ops.object.material_slot_remove({'object' : obj})