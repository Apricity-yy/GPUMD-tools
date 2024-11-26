for i in {47..50} 
do
cd $i
echo "$i", time 
qsub vasp.pbs
wait
cd ..
done