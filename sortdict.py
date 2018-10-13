#coding:utf-8

playbook_orders = [
    'create-deployer',
    'install-nginx',
    'install-cbt-web',
    'install-nginx-apk',
    'install-nginx-from-source',
    'install-docker',
    'docker-mongo',
    'docker-redis',
    'docker-mysql',
    'docker-rabbit',
    'install-tomcat',
    'install-license',
    'install-app',
    'install-report',
    'install-filebeat',
    'install-metricbeat',
]


print(playbook_orders.index('install-nginx'))