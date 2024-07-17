#----------------------------------------------------------------------------------------
# Oh My Posh "Theme Editor"
# 
# Instructions
# - Add/edit the _template property of any segment within your Oh My Posh theme
# - Run: python edit_theme.py <FILE_NAME> to "build" the segment templates
#----------------------------------------------------------------------------------------

import sys
import json


def load_theme(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        print(f"Error: Could not open a file named {file_name}")
        return False


def edit_theme(theme):
    blocks = theme.get("blocks")
    if not blocks:
        return

    for block_index, block in enumerate(blocks):
        segments = block.get("segments")
        if not segments:
            continue
        
        for segment_index, segment in enumerate(segments):
            template_builder = segment.get("properties").get("_template")
            if not template_builder:
                continue
            
            template = "".join(template_builder)
            theme['blocks'][block_index]['segments'][segment_index]['template'] = template

    return theme


def save_theme(theme, file_name):
    with open(file_name, 'w') as file:
        json.dump(theme, file, indent = 4)
    
    print(f"{file_name} saved")


if __name__ == "__main__":
    file_name = ""

    if len(sys.argv) <= 1:
        # ask for the theme's file name, if it's not provided as a command line argument
        file_name = input('Edit what theme?\n')
    else:
        # otherwise, get the file name from the command line arguments
        file_name = str(sys.argv[1])

    # append the Oh My Posh file extension if it's not already provided by the user
    if not file_name.endswith(".omp.json"):
        file_name = file_name + ".omp.json"
    
    # open the theme (my_theme.omp.json)
    theme = load_theme(file_name)
    if not theme:
        sys.exit()

    # for each segment, create a template property by joining the _template strings
    edit_theme(theme)

    # save the theme
    save_theme(theme, file_name)
