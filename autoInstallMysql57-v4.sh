#!/bin/bash
#########define area################
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/root/bin:/usr/local/mysq/bin
export PATH
srvIP="192.168.1.13"  ####ftp server,comment
ftpUser="xml"
ftpPwd="dangerous"
mysqlPkg="mysql-5.7.27.tar.gz" ##需要boost版本
ftpPath="ftp://$srvIP/$mysqlPkg"
srcPath="/usr/local/src"
installPath="/usr/local/mysql"
mysqlConf="/etc/my.cnf"
root_pwd="pwd"
install_log=/usr/local/src/mysql_install.log
vmCpuCores=$(cat /proc/cpuinfo |grep processor |wc -l)
DATAPATH="/datassd/mysql"
SLOWLOG="/var/log/$(hostname)-mysql-slow.log"
ERRORLOG="/var/log/$(hostname)-mysql-error.log"
TMPLOG="/var/log/mysql"
OTHERLOG="/data/mysql/logs"




cd $srcPath   ####sourece file dir

#########define area################


#########function area##################
GET_INSTALL_FILE(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
#wget --user=$ftpUser --password=$ftpPwd $ftpPath  ####ftp wget comment 
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

CREATE_DIR_USER(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
#add mysql user
if [ `cat /etc/passwd|grep 'mysql' |wc -l` -eq 0 ];then
        groupadd -r mysql
        useradd -g mysql -s /sbin/nologin -g mysql -M mysql 
fi
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}


INSTALL_DEP(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
yum install -y gcc-c++ ncurses-devel gcc gcc++ gcc-g77 openssl-devel cmake
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

DECOMPRESS_TAR(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
tar zxf $mysqlPkg
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

CONFIG()
{
echo "---------start ${FUNCNAME[0]} Fuction-----------"
cd $srcPath/mysql-5.7.27
cmake -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DMYSQL_UNIX_ADDR=$installPath/mysql.sock -DMYSQL_TCP_PORT=3306 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_USER=mysql -DWITH_DEBUG=0 -DWITH_SSL=system -DWITH_BOOST=/usr/local/src/mysql-5.7.27/boost/boost_1_59_0
if [ $? -eq 0 ];then
      make -j $vmCpuCores
fi

if [ $? -eq 0 ];then
      make install
fi
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

INSTALL(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
systemctl stop mysqld                 ###shut exist
ls $DATAPATH && rm -rf $DATAPATH  ###delete exist,danger,confor
ls "$DATAPATH" || mkdir -p "$DATAPATH"
ls "$OTHERLOG" || mkdir -p "$OTHERLOG"
ls "$SLOWLOG"  || touch "$SLOWLOG"
ls "$ERRORLOG" || touch "$ERRORLOG"
ls "$TMPLOG"   || mkdir -p "$TMPLOG"
chown -R mysql.mysql "$DATAPATH"
chown -R mysql.mysql "$OTHERLOG"
chown -R mysql.mysql "$ERRORLOG"
chown -R mysql.mysql "$SLOWLOG"
chown -R mysql.mysql "$TMPLOG"
rm -fv "$mysqlConf"
chown -R mysql.mysql $installPath  ####basedir and datassd dir need exactly path 
ls $install_log || touch $install_log 
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

INITIAL(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
$installPath/bin/mysqld --initialize --basedir=$installPath --datadir=$DATAPATH --user=mysql 2>&1 | tee $install_log
initial_password=$(grep '20.*Note.*pass.*roo.*host' "$install_log"|sed -e 's/20.*pass.*root.*host:\ //g')
echo "PW:$initial_password"

cp "$srcPath"/my.cnf "$mysqlConf"
cp $srcPath/mysql-5.7.27/support-files/mysql.server /etc/init.d/mysqld

chmod +x /etc/init.d/mysqld
chkconfig mysqld on
systemctl restart mysqld || service mysqld restart
systemctl enable mysqld
if [ `cat /etc/profile|grep 'mysql/bin' |wc -l` -eq 0 ];then
        echo "export PATH=$installPath/bin:$PATH" >>/etc/profile
  source /root/.bashrc
fi

sleep 1s

/usr/local/mysql/bin/mysql -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('$root_pwd')" -uroot -p"$initial_password" --connect-expired-password

ls /bin/mysql || ln -s /usr/local/mysql/bin/* /bin/
firewall-cmd --list-all|grep 3306 || firewall-cmd --add-port 3306/tcp --perm && firewall-cmd --reload

echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}
#########function area##################

###########main area########
GET_INSTALL_FILE
CREATE_DIR_USER
INSTALL_DEP
DECOMPRESS_TAR
CONFIG
INSTALL
INITIAL
############main area############
