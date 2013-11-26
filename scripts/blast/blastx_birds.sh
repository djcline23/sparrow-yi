#PBS -N blastx_forBirds_remaining
#PBS -l nodes=1:ppn=1
#PBS -l walltime=28:00:00
#PBS -l mem=12gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow/birds

blastx -query remaining.fasta -db birds -out birdsRemainingResults -outfmt '10 qseqid sseqid pident' -max_target_seqs 1
