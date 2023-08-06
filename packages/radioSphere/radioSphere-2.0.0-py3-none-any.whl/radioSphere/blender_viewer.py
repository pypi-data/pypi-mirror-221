#!BPY

__doc__ = """
Example usage for this test.
>blender --background --factory-startup --python blender_viewer.py -- -d DATA_DIR

Notice:
'--factory-startup' is used to avoid the user default settings from
                    interfering with automated scene generation.
'--' causes blender to ignore all following arguments so python can use
them.

See blender --help for details.
"""

__author__ = "benjy marks"
__version__ = "2.3"

# This is distributed under the GPL"

import bpy
import csv
import sys
import os

# from numpy import interp
from math import log, sqrt, atan
from mathutils import Vector


def build_world():
    print("#### Building world ####")
    scene = bpy.context.scene

    # Clear existing objects.
    scene.camera = None
    # for obj in scene.objects:
    # scene.objects.remove(obj)

    # bpy.data.worlds['World'].horizon_color=[0.0,0.0,0.0] # no backlights


def set_scene():
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 200  # 0
    scene.cycles.preview_samples = 1
    #     bpy.context.screen.areas[-1].spaces[0].viewport_shade = 'RENDERED'
    scene.render.use_motion_blur = True
    scene.render.motion_blur_shutter = 0.075
    scene.cycles.film_transparent = True


def make_particles(data_file_path):
    print("#### Making particles ####")

    bpy.ops.mesh.primitive_uv_sphere_add()
    ob = bpy.context.object  # This is 'Sphere', others start at 'Sphere.001'

    with open(data_file_path) as f:
        reader = csv.reader(f, delimiter="\t")
        for i, row in enumerate(reader):
            if i > 0:
                particle = i
                name = "Sphere." + str(particle).zfill(3)
                s = float(row[3]) / float(2.0)
                copy = ob.copy()
                copy.data = ob.data.copy()
                copy.scale = (s, s, s)
                # bpy.context.scene.objects.link(copy)
                bpy.data.objects[name].location = [
                    float(row[0]),
                    float(row[1]),
                    float(row[2]),
                ]

                mat = bpy.data.materials.new("M" + name)
                mat.use_nodes = True
                mat.node_tree.nodes.new(type="ShaderNodeBsdfGlass")
                mat.node_tree.nodes["Glass BSDF"].inputs["Roughness"].default_value = 0.0  # 05
                inp = mat.node_tree.nodes["Material Output"].inputs["Surface"]
                outp = mat.node_tree.nodes["Glass BSDF"].outputs["BSDF"]
                mat.node_tree.links.new(inp, outp)
                bpy.data.objects[name].active_material = mat
                print("Created " + str(i) + " particles", end="\r")
    bpy.ops.object.shade_smooth()
    sp = bpy.data.objects["Sphere"]
    # bpy.context.scene.objects.remove(sp)


def main():
    import sys  # to get command line args
    import argparse  # to parse options for us and print a nice help message

    # get the args passed to blender after "--", all of which are ignored by
    # blender so scripts may receive their own arguments
    argv = sys.argv

    if "--" not in argv:
        argv = []  # as if no args are passed
    else:
        argv = argv[argv.index("--") + 1 :]  # get all args after "--"

    # When --help or no args are given, print this help
    usage_text = "Run blender in background mode with this script:"
    "  blender --background --python " + __file__ + " -- [options]"

    parser = argparse.ArgumentParser(description=usage_text)

    # Possible types are: string, int, long, choice, float and complex.
    parser.add_argument(
        "-d",
        "--directory",
        dest="data_file_path",
        help="This is the directory of the data files",
        required=True,
        metavar="FOLDER",
    )

    args = parser.parse_args(argv)  # Ignore the args

    if not argv:
        parser.print_help()
        return
    if not args.data_file_path:
        print('Error: --text="some string" argument not given, aborting.')
        parser.print_help()
        return
    data_file_path = args.data_file_path

    build_world()
    set_scene()
    make_particles(data_file_path)
    bpy.ops.object.select_all()


if __name__ == "__main__":
    main()
