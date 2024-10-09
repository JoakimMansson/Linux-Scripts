#!/bin/bash

# Check if Discord is installed using yay
if ! yay -Q discord &>/dev/null; then
  echo "Discord is not installed on this system."
  exit 1
fi

# Check for Discord updates using yay
echo "Checking for Discord updates..."
update_info=$(yay -Qua | grep discord)

# If an update is available, install it
if [ ! -z "$update_info" ]; then
  echo "An update for Discord is available."
  echo "Updating Discord..."
  yay -Syu --noconfirm discord
  echo "Discord has been updated."
else
  echo "Discord is already up-to-date."
fi
