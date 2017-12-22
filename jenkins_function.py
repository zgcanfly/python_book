#coding=utf-8
#jenkins中匿名用户需要有项目可读权限
import jenkins
jenkins_server_url='http://jenkins.stockalert.cn'
server=jenkins.Jenkins(url=jenkins_server_url,username='zgyang',password='f4f892e1871ae8b437ca4c990895b5ca')
print(server.get_version())