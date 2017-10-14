# Author: tailorYang

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'yangyi',
    'database':'reboot15',
    'charset':'utf8'
}

user_fields=['id','username','password','role','phone','job']
idc_fields = ['id','name','name_cn','address','userid']
cabinet_fields=['id','name','idc_id','u_num','power']
server_fields = ['id','hostname','lan_ip','wan_ip','cabinet_id','user_id']
job_fields = ['id','apply_date','apply_type','apply_desc','deal_persion','status','deal_desc','deal_time','apply_persion']