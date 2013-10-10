#PBS -N sparrow_blast_search_1150
#PBS -l nodes=1:ppn=1
#PBS -l walltime=10:00:00
#PBS -l mem=3gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow

blastn -query 1150_TS.fasta -db db_1128 -out results/1150_search_1128_v2 -outfmt '10 qseqid sseqid qlen slen length pident' -max_target_seqs 1