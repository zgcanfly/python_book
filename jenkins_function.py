#coding=utf-8
#jenkins中匿名用户需要有项目可读权限
import jenkins
jenkins_server_url='http://jenkins.stockalert.cn'
jenkins_id='zgyang'
jenkins_token='f4f892e1871ae8b437ca4c990895b5ca'
server=jenkins.Jenkins(url=jenkins_server_url,username=jenkins_id,password=jenkins_token)
# job_name='dev_nodejs'
# server.build_job(job_name)
# server.build_job(job_name,parameters=param_dict)
#
# server.get_job_info(job_name)['lastBuild']['number']
# jobs=server.get_jobs()
# print(jobs)
# my_job=server.get_job_config('Ansible SSH List Update')
# print(my_job)
server.build_job('Ansible SSH List Update')
