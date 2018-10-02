 #==========Light_Temple==========
from os import system
from os import chdir

#Goes to ~ Directory
chdir('/home/robson/')

#Modify Rofi colors
system("echo ========Set_Rofi========")
system("sed -i '/rofi.color-normal: #333333, #aaaaaa, #1f201f,/c\ rofi.color-normal: #333333, #aaaaaa, #1f201f,#AF3F2F, #000000' ~/.Xresources")

#Modify Termite colors
system("echo ========Set_Termite========")
system("sed -i '/cursor = /c\cursor = #AF3F2F' .config/termite/config")
system("sed -i '/color12 = /c\color12 = #AF3F2F' .config/termite/config")

#Modify i3blocks colors
system("echo ========Set_i3blocks========")
system("sed -i '/color=/c\color=#AF3F2F' .config/i3/i3blocks.conf")

#Modify i3 configs colors
system("echo ========Set_i3========")
system("sed -i '/set $theme-color/c\set $theme-color #AF3F2F' .config/i3/config")
system("sed -i '/exec_always feh --bg-scale /c\exec_always feh --bg-scale ~/Pictures/Wallpaper/Light_Temple.png' .config/i3/config")

#Set GTK Theme
system("echo ========Set_GTK========")

system("sed -i '/gtk-theme-name=/c\gtk-theme-name="+'"Light_Temple"'+"' .gtkrc-2.0")
system("sed -i '/gtk-theme-name=/c\gtk-theme-name=Light_Temple' .config/gtk-3.0/settings.ini")

system('sudo plymouth-set-default-theme -R spinner')

#=======Theme_Color: #AF3F2F
system("echo =========Theme_Setted=========")
