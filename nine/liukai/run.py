#! /usr/bin/env python
# _*_coding:utf-8_*_

from app import app
#import sys

#reload(sys)


#sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)   
