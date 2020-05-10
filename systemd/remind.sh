#!/bin/bash
# Description: Service to handle reminders
command="notify-send 'Lembrete' '%s' -t 0 && "
command+="paplay /usr/share/sounds/freedesktop/stereo/complete.oga"
remind -z1 -k"$command" ~/.local/share/reminds/remind
