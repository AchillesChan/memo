[root@S-INFRA-MON01L Achilles]# cat sites
#SITE                               TAG
www.abcyc.com                        WAN2.8.6
an.abc.link                          139.359.7.3



[root@S-INFRA-MON01L Achilles]# cat detect-ca.sh
#!/bin/bash
PATH="/usr/local/bin:/usr/bin:/bin"
SITELIST="/home/Achilles/sites"
LOGFILE="/home/Achilles/siteca"
MIN_DAYS=99



while IFS= read -r SITE
do
    if echo "$SITE"|grep '#' &>/dev/null
    then
        continue
    fi

    URL=$(echo "$SITE"|awk '{print $1}')
    TAG=$(echo "$SITE"|awk '{print $2}')


curl -kvLI $URL 2>$LOGFILE

DATE_THEN=$(date -d "$(grep "expire date" "$LOGFILE" |sed -e 's/^.*date://g')" +%s)
DATE_NOW=$(date +%s)
DATE_DIFFERENCE=$((($DATE_THEN - $DATE_NOW)/86400))

if [ $DATE_DIFFERENCE -le $MIN_DAYS ]
then
    mail -s "$(hostname) $(date) $URL $TAG cert only $DATE_DIFFERENCE DAYS" mail_user@abc.link </dev/null
fi

done <"$SITELIST"
wait

