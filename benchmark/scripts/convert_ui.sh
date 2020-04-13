#!/bin/bash

dir_ui_raw="../ui_raw"
dir_ui="../ui"

mainwindow="mainwindow"
add_software="add_software"
model="model"
install_software_dialog="install_software_dialog"

pyuic5 "$dir_ui_raw/$mainwindow.ui" -o "$dir_ui/$mainwindow.py"
pyuic5 "$dir_ui_raw/$add_software.ui" -o "$dir_ui/$add_software.py"
pyuic5 "$dir_ui_raw/$model.ui" -o "$dir_ui/$model.py"
pyuic5 "$dir_ui_raw/$install_software_dialog.ui" -o "$dir_ui/$install_software_dialog.py"

