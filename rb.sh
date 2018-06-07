module load python/2.7
module load s3cmd
python buckets.py

while read bucket; do
  s3cmd del --recursive --force $bucket -c ~/.ssh/s3cfg
  s3cmd rb $bucket -c ~/.ssh/s3cfg
done <buckets.txt
