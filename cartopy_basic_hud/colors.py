from matplotlib.colors import LinearSegmentedColormap
import re

rgb_color_hex_pattern = re.compile(r'^#[0-9a-fA-F]{6}$')
rgba_color_hex_pattern = re.compile(r'^#[0-9a-fA-F]{8}$')

def saturation_colormap(color_hex):
    if rgb_color_hex_pattern.match(color_hex):
        # Explicitly designate full saturation
        color_hex = color_hex + 'FF'
    elif rgba_color_hex_pattern.match(color_hex):
        pass
    else:
        raise ValueError("Supply color_hex in #rrbbggaa or #rrggbb form.")

    # Produce a colormap ranging smoothly from transparent white to the supplied color.
    return LinearSegmentedColormap.from_list(name=None, colors=['#FFFFFF00', color_hex])
