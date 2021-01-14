# -*- coding: utf-8 -*-
# @author Wendy
# @created on 2021/1/14
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
proj_dir = os.path.join(dir_path, '..')

# 2021/1/14
cookies = {"bid":"QngtB-xuAV4","douban-fav-remind":"1","__utmv":"30149280.6718","ll":"\"108258\"","_vwo_uuid_v2":"DDEEC31D952FCAFB8A89674E32AB334AC|97e5d732130a9964c8fa0bcbdf5194dc","douban-profile-remind":"1","gr_user_id":"7d2ed445-faa2-4035-bb20-b253bb0a9c78","__gads":"ID","viewed":"\"3082082\"","__utmc":"30149280","dbcl2":"\"67181129:EvEBdBt2dYU\"","ck":"lvDn","push_doumail_num":"0","frodotk":"\"6eab907ee06e91ec4c02b17ca14bb5c4\"","push_noty_num":"0","__utmz":"30149280.1610531251.30.18.utmcsr","__utma":"30149280.1089770535.1599224554.1610531251.1610632133.31","__utmb":"30149280.0.10.1610632133","ap_v":"0,6.0","talionusr":"\"eyJpZCI6ICI2NzE4MTEyOSIsICJuYW1lIjogIlx1Njc2OFx1NjAxZFx1NTJhMCJ9\"","Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2":"1610633742","_ga":"GA1.2.1089770535.1599224554","_gid":"GA1.2.1266975464.1610633744","Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2":"1610634923"}


def read_file(filename):
    with open(filename) as cur_file:
        data = cur_file.read()
        print('[read_file]')
        return data


def read_mock(filename):
    return read_file(os.path.join(proj_dir, 'mock', filename + '.txt'))


def read_json(filename):
    with open(os.path.join(proj_dir, 'data', filename + '.json')) as json_file:
        data = json.load(json_file)
    return data

# def main():
#     print('good day!')
#
#
# if __name__ == '__main__':
#     main()
