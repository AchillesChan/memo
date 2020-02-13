#!/bin/bash
set -u
devicePath="/dev/sdc"
filePath="/data"
devicePartition="/dev/sdc5"
fstabFile="/etc/fstab"
fileType=xfs
sed -e 's/\s*\([\+0-9a-zA-Z]*\).*/\1/' <<eof |fdisk "$devicePath" < /dev/null &>/dev/null
n #new
e #extend
  # space
  # space
  # space
n #logical
l #logical
  # space
  # space
w #
eof


[[ -d "$filePath" ]] || mkdir -p "$filePath"
mkfs."$fileType" "$devicePartition" < /dev/null &>/dev/null
deviceUUID=$(blkid|grep "$devicePartition"|awk '{print $2}'|sed  's:"::g')

cp "$fstabFile" /tmp/
echo "$deviceUUID    "$filePath"    "$fileType"     defaults       0 0" >>"$fstabFile"

mount -a

