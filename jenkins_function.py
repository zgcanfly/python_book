#coding=utf-8
#jenkins中匿名用户需要有项目可读权限
import jenkins
import time
jenkins_server_url='http://jenkins.stockalert.cn'
jenkins_id='zgyang'
jenkins_token='f4f892e1871ae8b437ca4c990895b5ca'
server=jenkins.Jenkins(url=jenkins_server_url,username=jenkins_id,password=jenkins_token)
project='Ansible SSH List Update'

#
server.build_job(project)

# time.sleep(10)
# tinfo=server.get_build_info(project,number)

# deploylist=server.get_all_jobs()
# for i in range(len(deploylist)):
#     print(deploylist[i]['name'])
number = server.get_job_info(project)['lastCompletedBuild']['number']
number +=1
time.sleep(10)
tinfo = server.get_build_info(project, number)
if tinfo['result'] == 'SUCCESS':
    print(number,tinfo['result'])