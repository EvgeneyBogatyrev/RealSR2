import os


with open('/model/run.sh', 'w') as f:

    videos = os.listdir('/dataset')

    for video in videos:
        f.write(f'mkdir /results/{video}\n')
        f.write(f'python3 /model/codes/test.py -opt /model/codes/options/df2k/test_df2k.yml -in_path /dataset/{video} -res_path /results/{video}\n')

os.system('chmod +x /model/run.sh')
os.system('/model/run.sh')
