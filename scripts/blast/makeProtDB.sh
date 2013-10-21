#PBS -N nr_db
#PBS -l nodes=1:ppn=1
#PBS -l walltime=24:00:00
#PBS -l mem=16gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/data/blast

makeblastdb -in nr.fasta -out nr -dbtype prot
