'''The main gui interface to users inside of blender.'''

# standard
# related
import Blender
# local
import bcrf.blender_lib.gui.main

gui = bcrf.blender_lib.gui.main.MainContainer()
guide_tab = bcrf.blender_lib.gui.main.GuideTabContent(gui)
rig_tab = bcrf.blender_lib.gui.main.RigTabContent(gui)

gui.add_tab(guide_tab)
gui.add_tab(rig_tab)

gui.register()
