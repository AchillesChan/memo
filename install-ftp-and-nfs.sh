#!/bin/bash
####10 variables set
set -u
PROJECT_BASE=shijiazhuang-sfwm
FTP_USER_NAME="$PROJECT_BASE"-ftpuser
FTP_USER_PASSWORD=79dc1c2-01e5-4ca7-8960-a2080f
FTP_USER_HOME=/data/"$PROJECT_BASE"
FTP_CONTROL=21
FTP_WAN_CONTROL=50020
FTP_PORT_START=50100
FTP_PORT_END=50101
FTP_GROUP=ftp_group
FTP_CFG_FILE=/etc/vsftpd/vsftpd.conf
PERMIT_NFS_LAN='172.16.48.*'
SSH_CFG_FILE=/etc/ssh/sshd_config
PUBLIC_IP=$(curl -L cindy.50yc.com/ip.php)
NFS_CFG_FILE=/etc/exports
SELINUX_CFG_FILE=/etc/selinux/config
MNT_BASE=/mnt/nfs/
LOCAL_SUBNET="172.16"
LOCAL_IP=$(ip addr show|grep "$LOCAL_SUBNET"|awk '{print $2}'|sed -e 's:/.*$::g')
AZURE_HOST_NAME=B-SFWM-FILE8
DEVICE_PATH="/dev/sdd"
FILE_PATH="/data/$PROJECT_BASE"
DEVICE_PARTITION="/dev/sdd5"
FSTAB_FILE="/etc/fstab"
FILE_TYPE=ext4
OPERATIONVM=$(hostname)
#SCRIPTERRORLOG=scriptErrorLog 
ESP_NFS_DEBUG_FILE=/etc/custom-scripts/detect-nfs-status.sh

####20 function set
INSTALL_VSFTPD(){
sed -i 's:SELINUX=enforcing:SELINUX=disabled:g' "$SELINUX_CFG_FILE"
yum install -y vsftpd
mv "$FTP_CFG_FILE" /tmp

echo "
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=NO
xferlog_std_format=YES
ascii_upload_enable=YES
ascii_download_enable=YES
chroot_local_user=YES
listen=YES
listen_ipv6=NO
allow_writeable_chroot=YES
tcp_wrappers=YES
use_localtime=YES
pam_service_name=vsftpd
userlist_enable=YES
tcp_wrappers=YES
use_localtime=YES
pasv_enable=Yes
pasv_address=your_public_ip
pasv_min_port="$FTP_PORT_START"
pasv_max_port="$FTP_PORT_END"
port_enable=YES
xferlog_enable=YES
xferlog_file=/var/log/xferlog
vsftpd_log_file=/var/log/vsftpd.log
" >"$FTP_CFG_FILE"


sed -i "s:your_public_ip:$PUBLIC_IP:g" "$FTP_CFG_FILE"

firewall-cmd --add-port="$FTP_CONTROL"/tcp --permanent

seq "$FTP_PORT_START" "$FTP_PORT_END"|xargs -t -P 1 -n 1 -I {} firewall-cmd --add-port={}/tcp --permanent

firewall-cmd --reload

systemctl restart vsftpd
systemctl enable vsftpd
}

CREATE_FTP_USER(){

if ! ls "$FTP_USER_HOME"/Image
then
	mkdir -p "$FTP_USER_HOME"/Image
fi


if ! cat /etc/group |grep "$FTP_GROUP"
then
	groupadd "$FTP_GROUP"
fi

if ! cat /etc/passwd |grep "$FTP_USER_NAME"
then
	useradd -d "$FTP_USER_HOME" "$FTP_USER_NAME" -g "$FTP_GROUP"
fi

echo "$FTP_USER_PASSWORD"| passwd "$FTP_USER_NAME" --stdin

chown -R "$FTP_USER_NAME"."$FTP_GROUP" "$FTP_USER_HOME"

if ! grep "$FTP_GROUP" "$SSH_CFG_FILE"
then
	sed -i -e "\$aDenygroups "$FTP_GROUP"" "$SSH_CFG_FILE"  && systemctl restart sshd
fi
}
INSTALL_NFS_SERVER(){
yum install -y nfs-utils
systemctl enable nfs-server
systemctl enable nfs-lock
systemctl enable nfs-idmap
systemctl restart rpcbind
systemctl restart nfs-server
systemctl restart nfs-lock
systemctl restart nfs-idmap

echo ""$FTP_USER_HOME" "$PERMIT_NFS_LAN"(rw,sync,no_root_squash,no_all_squash)" >>"$NFS_CFG_FILE"

firewall-cmd --permanent --zone=public --add-service=nfs
firewall-cmd --add-port 111/tcp --permanent
firewall-cmd --add-port 2049/tcp --permanent
firewall-cmd --reload

}

SET_NFS_CLIENT(){
if systemctl status nfs-server|grep ' active' &>/dev/null && systemctl status vsftpd |grep ' active' &>/dev/null
then
echo ""
echo "==========running ON ESP1=========" 
echo "mkdir -p "$MNT_BASE$FTP_USER_NAME" && mount -t nfs "$LOCAL_IP":"$FTP_USER_HOME" "$MNT_BASE$FTP_USER_NAME""
cat <<Endofmessage
echo "if ! ls $MNT_BASE$FTP_USER_NAME/Image 
then 
        echo "WRONG $MNT_BASE$FTP_USER_NAME nfs ON $OPERATIONVM >>\$scriptErrorLog"
fi" >>$ESP_NFS_DEBUG_FILE
Endofmessage
	echo "==========running ON ESP1=========" 
	echo ""
fi
}

SET_DISK_PARTITION(){
sed -e 's/\s*\([\+0-9a-zA-Z]*\).*/\1/' <<eof |fdisk "$DEVICE_PATH"
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


[[ -d "$FILE_PATH" ]] || mkdir -p "$FILE_PATH"
mkfs."$FILE_TYPE" "$DEVICE_PARTITION"
DEVICE_UUID=$(blkid|grep "$DEVICE_PARTITION"|awk '{print $2}'|sed  's:"::g')

cp "$FSTAB_FILE" /tmp/                                         
echo "$DEVICE_UUID    $FILE_PATH    "$FILE_TYPE"     defaults       0 0" >>"$FSTAB_FILE"

mount -a

}

SET_AZURE_ENDPOINT(){
if systemctl status nfs-server|grep ' active' &>/dev/null && systemctl status vsftpd |grep ' active' &>/dev/null
then
echo ""
cat <<Endofmessage

echo "==========running ON azure-CLI=========" 
echo "azure vm endpoint create $AZURE_HOST_NAME $FTP_WAN_CONTROL $FTP_CONTROL"
echo "seq $FTP_PORT_START $FTP_PORT_END|xargs -P 1 -n 1 -t -I {} azure vm endpoint create $AZURE_HOST_NAME {} {}"
echo "==========running ON azure-CLI=========" 

Endofmessage

fi
}


####30 main section

#SET_DISK_PARTITION
#CREATE_FTP_USER
#INSTALL_VSFTPD
#INSTALL_NFS_SERVER
SET_NFS_CLIENT
SET_AZURE_ENDPOINT
