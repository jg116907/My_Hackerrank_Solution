read cal
# 5+50*3/20 + (19*2)/7
echo "scale=3;$cal" | bc -l # 올림이 아닌 버림 처리가 된다. # 17.928
printf "%.3f\n" $(echo "scale=5;$cal" | bc -l) # 5자리에서 3자리로 변환하면서 올림 처리됨 # 17.929
