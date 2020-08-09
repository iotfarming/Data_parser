import pandas as pd
csv_path = "CSV file name goes here"  #edit this line with the actual file name for the ip sheet. for exapmple 
                                      #if the file name is used-ips-log-20200805-0100.csv 
                                      #then csv_path = "used-ips-log-20200805-0100.csv"
df=pd.read_csv(csv_path)

pools = ['khi-cbbr2','khi-cbbr3','cbbr3-activity','jehlum_pool','nbb_fsd_pool','nbb_guj_pool','nbb_hyd_pool',
'nbb_jhang_pool','nbb_lhr2_pool','nbb_mul_pool','nbb_rwp_pool','nbb_ryk_pool','nbb_sgd_pool','psh_pool',
'sahiwal_pool']

cbbr = {}

#print(df)
for pool in pools:
    cbbr[pool] = {'pool_list': [], 'used_ips':0, 'remaining_ips':0, 'total_ips':0 }
    used = 0
    remain = 0
    total = 0
    for i in range (len(df[' pool_name'])):
        if pool in df[' pool_name'][i]:
            cbbr[pool]['pool_list'].append(df[' pool_name'][i])
            used  += df[' used_ips'][i]
            remain += df[' remaining_ips'][i]
            total += df[' total_ips'][i]
    cbbr[pool]['pool_name'] = pool
    cbbr[pool]['used_ips'] += used 
    cbbr[pool]['remaining_ips'] += remain
    cbbr[pool]['total_ips'] += total


print(cbbr['khi-cbbr2'])

for pool in cbbr:
    print("pool: {}".format(cbbr[pool]['pool_name']))
    print("used_ips: {}".format(cbbr[pool]['used_ips']))
    print("remaining_ips: {}".format(cbbr[pool]['remaining_ips']))
    print("total_ips: {}".format(cbbr[pool]['total_ips']))
