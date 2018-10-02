 #==========Violet_Pink==========
from os import system
from os import chdir

#Goes to ~ Directory
chdir('/home/robson/')

#Modify Rofi colors
system("echo ========Set_Rofi========")
system("sed -i '/rofi.color-normal: #333333, #aaaaaa, #1f201f,/c\ rofi.color-normal: #333333, #aaaaaa, #1f201f,#D47FB4, #000000' ~/.Xresources")

#Modify Termite colors
system("echo ========Set_Termite========")
system("sed -i '/cursor = /c\cursor = #D47FB4' .config/termite/config")
system("sed -i '/color12 = /c\color12 = #D47FB4' .config/termite/config")

#Modify i3blocks colors
system("echo ========Set_i3blocks========")
system("sed -i '/color=/c\color=#D47FB4' .config/i3/i3blocks.conf")

#Modify i3 configs colors
system("echo ========Set_i3========")
system("sed -i '/set $theme-color/c\set $theme-color #D47FB4' .config/i3/config")
system("sed -i '/exec_always feh --bg-scale /c\exec_always feh --bg-scale ~/Pictures/Wallpaper/Violet_4.png' .config/i3/config")

#Set GTK Theme
system("echo ========Set_GTK========")

system("sed -i '/gtk-theme-name=/c\gtk-theme-name="+'"Violet_Pink"'+"' .gtkrc-2.0")
system("sed -i '/gtk-theme-name=/c\gtk-theme-name=Violet_Pink' .config/gtk-3.0/settings.ini")

system('sudo plymouth-set-default-theme -R Violet_Pink')

#=======Theme_Color: #D47FB4
system("echo =========Theme_Setted=========")
