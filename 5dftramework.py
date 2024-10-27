import bpy

# Function to create the pyramid
def create_pyramid():
    bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=115.2, depth=146.6, location=(0, 0, 73.3))
    pyramid = bpy.context.object
    pyramid.rotation_euler[2] = 0.785398  # Rotate to align with the base

    # Create a new material for the pyramid
    material = bpy.data.materials.new(name="StoneMaterial")
    material.use_nodes = True
    bsdf = material.node_tree.nodes["Principled BSDF"]

    # Add the texture to the material
    tex_image = material.node_tree.nodes.new('ShaderNodeTexImage')
    tex_image.image = bpy.data.images.load("path/to/your/stone_texture.jpg")
    material.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])

    # Assign the material to the pyramid
    if pyramid.data.materials:
        pyramid.data.materials[0] = material
    else:
        pyramid.data.materials.append(material)

# Function to create the King's Chamber
def create_kings_chamber():
    bpy.ops.mesh.primitive_cube_add(size=10, location=(0, 0, 50))
    chamber = bpy.context.object
    chamber.scale = (1, 2, 0.5)

# Function to add planets with frequencies
def add_planets():
    planet_data = [
        {"name": "Sun", "location": (150, 0, 100), "frequency": 126.22},
        {"name": "Mercury", "location": (200, 0, 100), "frequency": 141.27},
        {"name": "Venus", "location": (250, 0, 100), "frequency": 221.23},
        {"name": "Earth", "location": (300, 0, 100), "frequency": 194.18},
        {"name": "Moon", "location": (350, 0, 100), "frequency": 210.42},
        {"name": "Mars", "location": (400, 0, 100), "frequency": 144.72},
        {"name": "Jupiter", "location": (450, 0, 100), "frequency": 183.58},
        {"name": "Saturn", "location": (500, 0, 100), "frequency": 147.85},
        {"name": "Uranus", "location": (550, 0, 100), "frequency": 207.36},
        {"name": "Neptune", "location": (600, 0, 100), "frequency": 211.44},
        {"name": "Pluto", "location": (650, 0, 100), "frequency": 140.25},
    ]

    for planet in planet_data:
        bpy.ops.mesh.primitive_uv_sphere_add(radius=5, location=planet["location"])
        planet_obj = bpy.context.object
        planet_obj.name = planet["name"]
        
        # Add text for frequency
        bpy.ops.object.text_add(location=(planet["location"][0], planet["location"][1], planet["location"][2] + 10))
        text_obj = bpy.context.object
        text_obj.data.body = f"{planet['name']}: {planet['frequency']} Hz"
        text_obj.scale = (0.5, 0.5, 0.5)

# Function to adjust camera perspective
def adjust_camera():
    bpy.ops.object.camera_add(location=(300, -300, 200))
    camera = bpy.context.object
    camera.rotation_euler = (1.1, 0, 0.785398)
    bpy.context.scene.camera = camera

# Main function to execute all steps
def main():
    create_pyramid()
    create_kings_chamber()
    add_planets()
    adjust_camera()
    bpy.ops.render.render(write_still=True)

# Execute the main function
main()
