for NAME in POSCAR-*
do
NUM=${NAME#*-}
mkdir $NUM
cp $NAME $NUM
cp INCAR KPOINTS POTCAR $NUM
cp run.slurm run-$NUM.slurm
sed -i -e "s/XXX/$NUM/g" run-$NUM.slurm
cp run-$NUM.slurm $NUM
cd $NUM
mv $NAME POSCAR
cd ..
done