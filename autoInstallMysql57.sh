#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/root/bin:/usr/local/mysq/bin
export PATH
#srvIP="192.168.1.13"  ####ftp server,comment
ftpUser="xml"
ftpPwd="dangerous"
mysqlPkg="mysql-5.7.17.tar.gz" ##需要boost版本
ftpPath="ftp://$srvIP/$mysqlPkg"
srcPath="/usr/local/src"
initialpw='abcd-1238'
installPath="/usr/local/mysql"
mysqlConf="/etc/my.cnf"
root_pwd="your-pass-here"
install_log=/usr/local/src/mysql_install.log
vmCpuCores=$(cat /proc/cpuinfo |grep processor |wc -l)
mv /tmp/$mysqlPkg $srcPath
cd $srcPath
##wget --user=$ftpUser --password=$ftpPwd $ftpPath  ####ftp wget comment 

#add mysql user
if [ `cat /etc/passwd|grep 'mysql' |wc -l` -eq 0 ];then
        groupadd -r mysql
        useradd -g mysql -s /sbin/nologin -g mysql -M mysql 
fi
yum install -y gcc-c++ ncurses-devel gcc gcc++ gcc-g77 openssl-devel cmake
tar zxf $mysqlPkg

cd $srcPath/mysql-5.7.17
cmake -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DMYSQL_UNIX_ADDR=$installPath/mysql.sock -DMYSQL_TCP_PORT=3306 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_USER=mysql -DWITH_DEBUG=0 -DWITH_SSL=system -DWITH_BOOST=/usr/local/src/mysql-5.7.17/boost/boost_1_59_0
if [ $? -eq 0 ];then
      make -j $vmCpuCores
fi

if [ $? -eq 0 ];then
      make install
fi
mkdir -p $installPath/data
chmod +w $installPath
chown -R mysql.mysql $installPath
cd $srcPath/mysql-5.7.17/support-files/

mv $mysqlConf "$mysqlConf".bak
cp my-default.cnf $mysqlConf

chown -R mysql.mysql $installPath  ####basedir and data dir need exactly path 
ls $install_log || touch $install_log 

$installPath/bin/mysqld --initialize --basedir=$installPath --datadir=$installPath/data/ --user=mysql 2>&1 | tee $install_log
initial_password=$(grep '20.*Note.*pass.*roo.*host' "$install_log"|sed -e 's/20.*pass.*root.*host:\ //g')
echo "PW:$initial_password"

cp $srcPath/mysql-5.7.17/support-files/mysql.server /etc/init.d/mysqld

chmod +x /etc/init.d/mysqld
chkconfig mysqld on
systemctl restart mysqld || service mysqld restart

if [ `cat /etc/profile|grep 'mysql/bin' |wc -l` -eq 0 ];then
        echo "export PATH=$installPath/bin:$PATH" >>/root/.bashrc
  source /root/.bashrc
fi

sleep 1s

mysql -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('$root_pwd')" -uroot -p"$initial_password" --connect-expired-password
