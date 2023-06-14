#!/usr/bin/env python3

import argparse, requests

parser = argparse.ArgumentParser(description='TP-Link Easy Smart Switch config backup.')
parser.add_argument('target', metavar='host', help='IP address or hostname of switch')
parser.add_argument('-p', '--password', metavar='password', required=True, help='password for switch access')
parser.add_argument('-u', '--username', metavar='username', required=False, default='admin', help='username for switch access')
args = vars(parser.parse_args())

user = args['username']
password = args['password']
baseurl = "http://"+args['target']

s = requests.Session()

data = {"logon": "Login", "username": user, "password": password}
headers = { 'Referer': f'{baseurl}/Logout.htm'}
try:
    r = s.post(f'{baseurl}/logon.cgi', data=data, headers=headers, timeout=5)
except requests.exceptions.Timeout as errt:
       sys.exit("ERROR: Timeout Error at login")
except requests.exceptions.RequestException as err:
       sys.exit("ERROR: General error at login: "+str(err))

headers = {'Referer': f'{baseurl}/',
           'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           'Upgrade-Insecure-Requests': "1" }
r = s.get(f'{baseurl}/config_back.cgi?btnBackup=Backup Config', headers=headers, timeout=6)


open('%s_config.cfg' % args['target'], 'wb').write(r.content)
