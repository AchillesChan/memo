#!/bin/bash
#########define area################
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/root/bin:/usr/local/mysql/bin
export PATH
SRVIP="192.168.1.3"  ####ftp server,comment
FTPUSER="xml"
FTPPWD="dangerous"
MYSQLPKG="mysql-boost-8.0.19.tar.gz" ##需要boost版本
FTPPATH="ftp://$SRVIP/$MYSQLPKG"
SRCPATH="/usr/local/src"
INSTALLPATH="/usr/local/mysql"
MYSQLCFG="/etc/my.cnf"
ROOTPWD="root_pwd"
INSTALL_LOG=/usr/local/src/mysql_install.log
CPUNUM=$(cat /proc/cpuinfo |grep processor |wc -l)
DATAPATH="/data/mysql"
cd $SRCPATH   ####sourece file dir

#########define area################


#########function area##################
GET_INSTALL_FILE(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
#wget --user=$FTPUSER --password=$FTPPWD $FTPPATH  ####ftp wget comment
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

CREATE_DIR_USER(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
ls /var/log/mysql || mkdir -p /var/log/mysql
ls /var/log/mysql-slow.log || touch /var/log/mysql-slow.log
if [ `cat /etc/passwd|grep 'mysql' |wc -l` -eq 0 ];then
        groupadd -r mysql
        useradd -g mysql -s /sbin/nologin -g mysql -M mysql
fi
#mkdir -p /data/mysql/db_3306/{undolog,tmp,relaylog,redolog,errlog,data,binlog}
chown -R mysql.mysql /var/log/mysql-slow.log
chown -R mysql.mysql /var/log/mysql
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}


INSTALL_DEP(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
yum install centos-release-scl mailx epel* -y
yum install -y gcc-c++ ncurses-devel gcc gcc++ gcc-g77 openssl-devel cmake3.x86_64
yum install -y devtoolset-7
mv /bin/cmake /bin/cmake-old
ln -s /bin/cmake3 /bin/cmake
echo "source /opt/rh/devtoolset-7/enable ">/etc/profile

source /opt/rh/devtoolset-7/enable

echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

DECOMPRESS_TAR(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
tar zxf $MYSQLPKG
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

CONFIG()
{
echo "---------start ${FUNCNAME[0]} Fuction-----------"
cd $SRCPATH/mysql-8.0.19
mkdir -p $SRCPATH/mysql-8.0.19/bld && cd $SRCPATH/mysql-8.0.19/bld
cmake3 .. -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DMYSQL_UNIX_ADDR=$INSTALLPATH/mysql.sock -DMYSQL_TCP_PORT=3306 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_USER=mysql -DWITH_DEBUG=0 -DWITH_SSL=system -DWITH_BOOST=$SRCPATH/mysql-8.0.19/boost
if [ $? -eq 0 ];then
      make -j $CPUNUM
fi

if [ $? -eq 0 ];then
      make install
fi
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

INSTALL(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"
ls $DATAPATH && rm -rf $DATAPATH  ###delete exist,danger,confor
ls $DATAPATH || mkdir -p $DATAPATH
chown -R mysql.mysql $DATAPATH
mkdir -p $INSTALLPATH/data
chmod +w $INSTALLPATH
chown -R mysql.mysql $INSTALLPATH
cd $SRCPATH/mysql-8.0.19/support-files/
rm -rfv /data/mysql/*
rm -fv "$MYSQLCFG"
chown -R mysql.mysql $INSTALLPATH  ####basedir and data dir need exactly path
ls $INSTALL_LOG || touch $INSTALL_LOG
echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}

INITIAL(){
echo "---------start ${FUNCNAME[0]} Fuction-----------"

cp "$SRCPATH"/my.cnf "$MYSQLCFG"
mkdir -p /data/mysql/db_3306/{undolog,tmp,relaylog,redolog,errlog,data,binlog}
chown -R mysql.mysql /data/mysql/db_3306
/usr/local/mysql/bin/mysqld --initialize --user=mysql
cd /usr/local/mysql
mkdir /usr/local/mysql/mysql-files
chown mysql:mysql -R /usr/local/mysql
chmod 750 /usr/local/mysql/mysql-files
/usr/local/mysql/bin/mysql_ssl_rsa_setup
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld
chmod +x /etc/init.d/mysqld
chkconfig mysqld on
systemctl restart mysqld || service mysqld restart
systemctl enable mysqld

initial_password=$(grep '20.*Note.*pass.*roo.*host' /data/mysql/db_3306/errlog/mysql.err|sed -e 's/20.*pass.*root.*host:\ //g')
echo "PW:$initial_password"
if [ `cat /etc/profile|grep 'mysql/bin' |wc -l` -eq 0 ];then
        echo "export PATH=$INSTALLPATH/bin:$PATH" >>/etc/profile
  source /root/.bashrc
fi

sleep 1s

/usr/local/mysql/bin/mysql -S /data/mysql/db_3306/mysql.sock -e "alter user 'root'@'localhost' identified by '$ROOTPWD'" -uroot -p"$initial_password" --connect-expired-password

ln -s /usr/local/mysql/bin/* /bin/
firewall-cmd --add-port 3306/tcp --perm && firewall-cmd --reload

echo "---------end   ${FUNCNAME[0]} Fuction-----------"
}
#########function area##################

###########main area########
INSTALL_DEP
GET_INSTALL_FILE
CREATE_DIR_USER
DECOMPRESS_TAR
CONFIG
INSTALL
INITIAL
##########main area############
