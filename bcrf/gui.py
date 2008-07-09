'''The main gui interface to users inside of blender.'''

# standard
# related
import Blender
# local
import bcrf.blender_lib.gui.main as bcrf_gui

gui = bcrf_gui.MainContainer()
create_comp_tab = bcrf_gui.CreateComponentTabContent(gui)
mod_comp_tab = bcrf_gui.ModifyComponentTabContent(gui)
guide_tab = bcrf_gui.GuideTabContent(gui)
rig_tab = bcrf_gui.RigTabContent(gui)
xml_tab = bcrf_gui.XMLTabContent(gui)

gui.add_tab(guide_tab)
gui.add_tab(rig_tab)
gui.add_tab(create_comp_tab)
gui.add_tab(mod_comp_tab)
gui.add_tab(xml_tab)

gui.register()
