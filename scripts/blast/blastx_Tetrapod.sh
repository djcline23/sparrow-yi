#PBS -N blastx_Tetrapod
#PBS -l nodes=1:ppn=1
#PBS -l walltime=10:00:00
#PBS -l mem=3gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow/tetrapod

blastx -query 1150_hetero.fasta -db tetrapod -out tetrapodBlastResults -outfmt '10 qseqid sgi pident' -max_target_seqs 1
