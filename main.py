import subprocess
import sys

#import inquirer

import constant
from activity import Activity
from scene import Scene


def render_overlay(gpx_filename, template_filename, output_filename):
    activity = Activity(gpx_filename)
    scene = Scene(activity, activity.valid_attributes, template_filename)
    start, end = scene.configs["scene"]["start"], scene.configs["scene"]["end"]
    activity.trim(start, end)
    activity.interpolate(scene.fps)
    scene.build_figures()
    scene.render_video(end - start, output_filename)


def demo_frame(gpx_filename, template_filename, second):
    activity = Activity(gpx_filename)
    scene = Scene(activity, activity.valid_attributes, template_filename)
    start, end = scene.configs["scene"]["start"], scene.configs["scene"]["end"]
    activity.trim(start, end)
    activity.interpolate(scene.fps)
    scene.build_figures()
    scene.render_demo(end - start, second)
    #subprocess.run(["open", scene.frames[0].full_path()])
    return scene


# TODO improve argument handling
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <gpx_filename> <template_filename>")
        exit()
    
    gpx_filename = sys.argv[1]
    template_filename = sys.argv[2]

    if len(sys.argv) > 3:
        if sys.argv[3] == "demo":
            second = int(sys.argv[4]) if len(sys.argv) == 5 else 0
            while True:
                print(
                    f"demoing frame using the {template_filename} template and {gpx_filename} gpx file"
                )
                scene = demo_frame(gpx_filename, template_filename, second)
                input("enter to re-render:")
                scene.update_configs(template_filename)
    print(
        f"rendering overlay using the {template_filename} template and {gpx_filename} gpx file"
    )
    
    output_filename = gpx_filename[:-4] + ".mov"
    render_overlay(gpx_filename, template_filename, output_filename)
