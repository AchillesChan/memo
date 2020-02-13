#!/bin/bash
#########define area################
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/root/bin:/usr/local/mysq/bin
export PATH
srvIP="192.168.1.13"  ####ftp server,comment
ftpUser="xml"
ftpPwd="dangerous"
mysqlPkg="mysql-5.7.17.tar.gz" ##需要boost版本
ftpPath="ftp://$srvIP/$mysqlPkg"
srcPath="/usr/local/src"
installPath="/usr/local/mysql"
mysqlConf="/etc/my.cnf"
root_pwd="Your_password"
install_log=/usr/local/src/mysql_install.log
vmCpuCores=$(cat /proc/cpuinfo |grep processor |wc -l)
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
ls /var/log/mysql || mkdir -p /var/log/mysql
ls /var/log/mysql-slow.log || touch /var/log/mysql-slow.log
#add mysql user
if [ `cat /etc/passwd|grep 'mysql' |wc -l` -eq 0 ];then
        groupadd -r mysql
        useradd -g mysql -s /sbin/nologin -g mysql -M mysql
fi
chown -R mysql.mysql /var/log/mysql
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
cd $srcPath/mysql-5.7.17
cmake -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DMYSQL_UNIX_ADDR=$installPath/mysql.sock -DMYSQL_TCP_PORT=3306 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_USER=mysql -DWITH_DEBUG=0 -DWITH_SSL=system -DWITH_BOOST=/usr/local/src/mysql-5.7.17/boost/boost_1_59_0
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
ls /data/mysql && rm -rf /data/mysql  ###delete exist,danger,confor
ls /data/mysql || mkdir -p /data/mysql
chown -R mysql.mysql /data/mysql
mkdir -p $installPath/data
chmod +w $installPath
chown -R mysql.mysql $installPath
cd $srcPath/mysql-5.7.17/support-files/
rm -rfv /data/mysq/*
rm -fv "$mysqlConf"
#mv $mysqlConf "$mysqlConf".bak
chown -R mysql.mysql $installPath  ####basedir and data dir need exactly path
ls $install_log || touch $install_log
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

INITIAL(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
$installPath/bin/mysqld --initialize --basedir=$installPath --datadir=/data/mysql --user=mysql 2>&1 | tee $install_log
initial_password=$(grep '20.*Note.*pass.*roo.*host' "$install_log"|sed -e 's/20.*pass.*root.*host:\ //g')
echo "PW:$initial_password"

cp "$srcPath"/my.cnf "$mysqlConf"
cp $srcPath/mysql-5.7.17/support-files/mysql.server /etc/init.d/mysqld

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
