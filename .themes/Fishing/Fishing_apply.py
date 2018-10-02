 #==========Fishing==========
from os import system
from os import chdir

#Goes to ~ Directory
chdir('/home/robson/')

#Modify Rofi colors
system("echo ========Set_Rofi========")
system("sed -i '/rofi.color-normal: #333333, #aaaaaa, #1f201f,/c\ rofi.color-normal: #333333, #aaaaaa, #1f201f,#5D9449, #000000' ~/.Xresources")

#Modify Termite colors
system("echo ========Set_Termite========")
system("sed -i '/cursor = /c\cursor = #5D9449' .config/termite/config")
system("sed -i '/color12 = /c\color12 = #5D9449' .config/termite/config")

#Modify i3blocks colors
system("echo ========Set_i3blocks========")
system("sed -i '/color=/c\color=#5D9449' .config/i3/i3blocks.conf")

#Modify i3 configs colors
system("echo ========Set_i3========")
system("sed -i '/set $theme-color/c\set $theme-color #5D9449' .config/i3/config")
system("sed -i '/exec_always feh --bg-scale /c\exec_always feh --bg-scale ~/Pictures/Wallpaper/Fishing.png' .config/i3/config")

#Set GTK Theme
system("echo ========Set_GTK========")

system("sed -i '/gtk-theme-name=/c\gtk-theme-name="+'"Fishing"'+"' .gtkrc-2.0")
system("sed -i '/gtk-theme-name=/c\gtk-theme-name=Fishing' .config/gtk-3.0/settings.ini")

system('sudo plymouth-set-default-theme -R spinner')

#=======Theme_Color: #5D9449
system("echo =========Theme_Setted=========")
