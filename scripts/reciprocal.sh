#PBS -N reciprocal
#PBS -l nodes=1:ppn=1
#PBS -l walltime=1:00:00
#PBS -l mem=1gb
#PBS -k oe
#PBS -q bioforce-6
#PBS -m abe

cd ~/scratch/sparrow/results

python blast.py 1150_search_1128_v2 1128_search_1150_v2 reciprocal
