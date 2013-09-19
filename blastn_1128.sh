#PBS -N sparrow_blast_search_1128
#PBS -l nodes=1:ppn=1
#PBS -l walltime=10:00:00
#PBS -l mem=3gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow

blastn -query 1128_SWS.fasta -db db_1150 -out 1128_search_1150_v2 -outfmt '10 qseqid sseqid pident' -max_target_seqs 1
