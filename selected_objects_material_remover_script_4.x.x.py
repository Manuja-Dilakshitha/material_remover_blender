import bpy

objects = bpy.context.selected_objects

for obj in objects:
    # Ensure the object is the active object
    bpy.context.view_layer.objects.active = obj
    obj.active_material_index = 0
    
    # Iterate over the material slots and remove each
    for _ in range(len(obj.material_slots)):
        bpy.ops.object.material_slot_remove()
