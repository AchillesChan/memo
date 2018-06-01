######Startmemoof autoInstallMysql57.sh #######
######Start autoInstallMysql57.sh #######
#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/root/bin:/usr/local/mysq/bin
export PATH
#srvIP="192.168.1.13"  ####ftp server,comment
ftpUser="username"
ftpPwd="dangerous"
mysqlPkg="mysql-5.7.17.tar.gz" ##需要boost版本
ftpPath="ftp://$srvIP/$mysqlPkg"
srcPath="/usr/local/src"
installPath="/usr/local/mysql"
dataPath="/data/mysql"
mysqlConf="/etc/my.cnf"
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
cmake -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 \
 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 \
 -DMYSQL_UNIX_ADDR=$installPath/mysql.sock -DMYSQL_TCP_PORT=3306 \
 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all \
 -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_USER=mysql -DWITH_DEBUG=0 -DWITH_SSL=system \
 -DWITH_BOOST=/usr/local/src/mysql-5.7.17/boost/boost_1_59_0
if [ $? -eq 0 ];then
      make -j $vmCpuCores
fi

if [ $? -eq 0 ];then
      make install
fi
mkdir -p $dataPath
chmod +w $installPath
chown -R mysql.mysql $installPath
chown -R mysql.mysql $dataPath
cd $srcPath/mysql-5.7.17/support-files/


###cp $srcPath my.cnf to /etc/my.cn
###MUST include Correct datadir and basedir in my.cnf
###First touch my.cnf in $srcPath 
cp  $srcPath/my.cnf $mysqlConf

chown -R mysql.mysql $installPath  #basedir and data dir need exactly path 

####if $dataPath not EMPTY ,get error,rm everything in $dataPath
$installPath/bin/mysqld --initialize --basedir=$installPath --datadir=$dataPath --user=mysql

cp $srcPath/mysql-5.7.17/support-files/mysql.server /etc/init.d/mysqld

chmod +x /etc/init.d/mysqld

systemctl enable mysqld
systemctl start mysqld
ln -s $installPath/bin/* /bin/

echo "Install mysqld successful"
######End autoInstallMysql57.sh #######
######Endmemoof autoInstallMysql57.sh #######
