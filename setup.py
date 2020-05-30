from distutils.core import setup

setup(
    name='cartopy_basic_hud',
    version='0.1dev',
    packages=['cartopy_basic_hud',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    entry_points={
        "console_scripts": [
            "cartopy_hud = cartopy_basic_hud.commands.main:main",
        ],
    }
)
