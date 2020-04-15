[root@host user]# cat sites
#SITE                               TAG                MIN_DAYS
www.abc.com                         rp-abc               22
an.abc.link                         rp-2.5.5             33



[root@host user]# cat detect-ca.sh
#!/bin/bash
#_DEBUG="on"

function DEBUG()
 {
      [ "$_DEBUG" == "on" ] &&  $@ || :
  }

PATH="/usr/local/bin:/usr/bin:/bin"
SITELIST="/home/Achilles/sites"
LOGFILE="/home/Achilles/siteca"
TIMEOUT=5

while IFS= read -r SITE
do
    if echo "$SITE"|grep '#' &>/dev/null
    then
        continue
    fi

URL=$(echo "$SITE"|awk '{print $1}')
TAG=$(echo "$SITE"|awk '{print $2}')
MIN_DAYS=$(echo "$SITE"|awk '{print $3}')
if curl -kvLI -ILkv --connect-timeout "$TIMEOUT" https://$URL 2>$LOGFILE 1>/dev/null
then

        DATE_THEN=$(date -d "$(grep "expire date" "$LOGFILE" |sed -e 's/^.*date://g')" +%s)
        DATE_NOW=$(date +%s)

        DATE_DIFFERENCE=$((($DATE_THEN - $DATE_NOW)/86400))
        if [[ "$DATE_DIFFERENCE" -le "$MIN_DAYS" ]]
        then
            mail -s "$(hostname) $(date) $URL $TAG cert only $DATE_DIFFERENCE DAYS" mail_user@abc.com </dev/null
        fi
else
        mail -s "$(hostname) $(date) https://$URL 没有响应 " mail_user@abc.com </dev/null
fi
done <"$SITELIST"
wait

