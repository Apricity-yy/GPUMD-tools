for i in {1..50} 
do
cd $i
echo "$i", time 
sbatch run-$i.slurm
wait
cd ..
done