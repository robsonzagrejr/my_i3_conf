# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
#dir='/usr/share/cows/'
#file=`/bin/ls -1 "$dir" | sort --random-sort | head -1`
#cow=$(echo "$file" | sed -e "s/\.cow//")
#/usr/games/fortune -a | cowsay -f $cow

#fortune | cowsay -f moose
cowsay -f turtleR O Ontem é história, O Amanhã é um mistério, mas o hoje é uma dádiva. É por isso que se chama PRESENTE. 

