# -*- coding: UTF-8 -*-
'''
@Project ：easypcd
@File    ：easypcd.py
@Author  ：王泽辉
@Date    ：2023-05-09 15:02 
'''
import numpy as np

class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        value = self[key]
        if isinstance(value, dict):
            value = DotDict(value)
        return value

class ep():
    def __init__(self):
        self.format_dic = {0: 'pcd', 1: "txt"}
        self.pcd_head = '# .PCD v0.7 - Point Cloud Data file format'
        self.VERSION = 'VERSION 0.7'

    def processing_str(self, input, s, length):
        for i in range(length):
            input += " "
            input += str(s)
        return input

    def read_pcd(self, pcd_file):
        format_type = {"I": np.int32, "U": np.uint, "F": np.float32}
        pcd_data = []
        pcd_information = {}
        with open(pcd_file, 'r') as f:
            lines = f.readlines()
            for i in lines[1:11]:
                info = list(i.strip('\n').split(' '))
                if len(info) > 2:
                    info_line = [info[0], ' '.join(info[1:])]
                else:
                    info_line = info
                pcd_information.update({info_line[0]: info_line[1]})
            pcd_type = pcd_information['TYPE'].split(" ")
            for line in lines[11:]:
                line = list(line.strip('\n').split(' '))
                if line == ['']:
                    pass
                else:
                    tmp = []
                    for i in range(len(line)):
                        tmp.append(format_type[pcd_type[i]](line[i]))
                    pcd_data.append(tmp)
            points = np.array(pcd_data)
            pcd_information.update({"points": points})
        return DotDict(pcd_information)

    def write_pcd(self, save_name, points, color=False, normal=False, _SIZE=4,
                  _TYPE="F", _COUNT=1, _HEIGHT=1, _VIEWPOINT='0 0 0 1 0 0 0', _DATA='ascii'):
        if color == True and normal == False:
            length = 6
            FIELDS = "FIELDS x y z r g b"
        if color == False and normal == False:
            length = 3
            FIELDS = "FIELDS x y z"
        if color == False and normal == True:
            length = 6
            FIELDS = "FIELDS x y z nx ny nz"
        if color == True and normal == True:
            length = 9
            FIELDS = "FIELDS x y z r g b nx ny nz"
        pcd_init = {
            "pcd_head": self.pcd_head,
            "VERSION": self.VERSION,
            "FIELDS": FIELDS,
            "SIZE": self.processing_str("SIZE", _SIZE, length),
            "TYPE": self.processing_str("TYPE", _TYPE, length),
            "COUNT": self.processing_str("COUNT", _COUNT, length),
            "WIDTH": "WIDTH " + str(len(points)),
            "HEIGHT": 'HEIGHT ' + str(_HEIGHT),
            "VIEWPOINT": 'VIEWPOINT ' + str(_VIEWPOINT),
            "POINTS": "POINTS " + str(len(points)),
            "DATA": 'DATA ' + str(_DATA)
        }
        try:
            with open(save_name, mode='w') as f:
                for i in pcd_init:
                    f.write(pcd_init[i] + '\n')
                np.savetxt(f, points, delimiter=' ', fmt='%d')
        except:
            assert "一个未知的错误！"

    def write_txt(self, points, save_name):
        with open(save_name, mode='w') as f:
            for line in points:
                for p in line:
                    p = str(int(p))
                    f.write(p)
                    f.write(" ")
                f.write("\n")


if __name__ == '__main__':
    easypcd1 = easypcd()
    pcd = easypcd1.read_pcd("point.pcd")
    easypcd1.write_pcd("1.pcd", pcd.points, True, True)
