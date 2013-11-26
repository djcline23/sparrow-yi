#PBS -N sparrow_blast_search_1128
#PBS -l nodes=1:ppn=1
#PBS -l walltime=1:00:00
#PBS -l mem=3gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow/1131

blastn -query 1128_candidates.fasta -db db_1131 -out 1128_cand_search_1131 -outfmt '10 qseqid sseqid qlen slen length pident' -max_target_seqs 1 -perc_identity 98.0

blastn -query 1150_candidates.fasta -db db_1131 -out 1150_cand_search_1131 -outfmt '10 qseqid sseqid qlen slen length pident' -max_target_seqs 1 -perc_identity 98.0
