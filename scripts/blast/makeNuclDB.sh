#PBS -N sparrow_blast_db
#PBS -l nodes=1:ppn=1
#PBS -l walltime=2:00:00
#PBS -l mem=8gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow

makeblastdb -in 1128_SWS.fasta -out db_1128 -dbtype nucl
makeblastdb -in 1150_TS.fasta -out db_1150 -dbtype nucl
