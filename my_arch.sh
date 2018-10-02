#Install Network Manager
sudo pacman -S networkmanager network-manager-applet

#Install Grafics and Audio Components
sudo pacman -S pulseaudio pulseaudio-alsa xorg xorg-init git

#Install Configurations
git clone https://github.com/robsonzagrejr/my_i3_conf.git
cd my_i3_conf
mv -r * ..
cd ..
rm -rf my_i3_conf

#Install Windows Manager
sudo pacman -S i3-wm i3lock i3blocks

#Install Terminal
sudo pacman -S termite rofi compton vim

#Install File Manager
sudo pacman -S ranger w3m ffmpeg ffmpegthumbnailer

#Install Componnents
sudo pacman -S firefox scrot feh imagemagick python mplayer pulseaudio arandr

#Install aurman
git clone https://github.com/polygamma/aurman.git
cd aurman
makepkg -si
cd ..

#Install Other
aurman -S google-chrome mirage plymouth

cd ~
sudo mv lock /bin/

