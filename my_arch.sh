#Solve de Key Problem
sudo pacman-key --delete 91FFE0700E80619CEB73235CA88E23E377514E00
sudo pacman-key --populate archlinux
#sudo gpg --full-gen-key
gpg --recv-keys 465022E743D71E39

#Install Network Manager
sudo pacman -S networkmanager network-manager-applet

#Install Grafics and Audio Components
sudo pacman -S pulseaudio pulseaudio-alsa alsa alsa-utils xorg xorg-xinit

#git clone https://github.com/robsonzagrejr/my_i3_conf.git

#Install Windows Manager
sudo pacman -S i3-wm i3lock i3blocks

#Install Terminal
sudo pacman -S termite rofi compton vim

#Install File Manager
sudo pacman -S ranger w3m ffmpeg ffmpegthumbnailer udiskie

#Install Componnents
sudo pacman -S firefox scrot feh imagemagick python mplayer seaudio arandr

#Install aurman
git clone https://github.com/polygamma/aurman.git
cd aurman
makepkg -si
cd ..
rm -rf aurman

#Install Other
aurman -S google-chrome mirage plymouth

#Install Configurations
cd ~
rm -rf .bash* .config .cache
cd my_i3_conf.git
mv * ..
mv .* ..
mv .X* ..
mv .x* ..
cd ~
sudo mv lock /bin/

#Configure Keyboard
sudo localectl set-keymap br-abnt2
setxkbmap -model abtn2 -layout br -variant abnt2

#Verivy Video Drivers
echo "Verify your video driver and if is the case, install manualy"
lspci | grep -e VGA -e 3D
sudo pacman -Ss xf86-video
