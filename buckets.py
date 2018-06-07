from subprocess import Popen, PIPE

stdout = Popen('s3cmd ls -c ~/.ssh/s3cfg', shell=True, stdout=PIPE).stdout
queue = stdout.read()
with open('buckets.txt','w') as file:
    file.writelines(queue)

with open('buckets.txt','r') as file:
    q =file.readlines()
del q[0]
for i in range(len(q)):
    q[i] = q[i].split()[2] + '\n'
with open('buckets.txt','w') as file:
    file.writelines(q)
