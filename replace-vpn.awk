NR==FNR{
        temp[$1]=$2
        }

NR!=FNR{
        for(j=1;j<=NF;j++){    
              if($j~/^%.*/)  
                   $j = temp[$j]
              s=$0       
        }
              print s
    }        
