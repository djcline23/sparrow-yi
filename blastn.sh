#PBS -N sparrow_blast_search
#PBS -l nodes=1:ppn=1
#PBS -l walltime=24:00:00
#PBS -l mem=20gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow

blastn -query 1128_SWS.fasta -db db_1150 -out 1128_search_1150 -outfmt 10
blastn -query 1150_TS.fasta -db db_1128 -out 1150_search_1128 -outfmt 10

