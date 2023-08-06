import sys
import requests

requests.packages.urllib3.disable_warnings()


def main():
    res = requests.delete(sys.argv[1], verify=False)

    if 200 != res.status_code:
        print(res.content.decode())
        exit(1)

    print('db      : {}'.format(res.headers['x-db']))
    print('log-seq : {}'.format(res.headers['x-log-seq']))
    print('old-seq : {}'.format(res.headers['x-old-seq']))
    print('length  : {}'.format(res.headers['content-length']))


if '__main__' == __name__:
    main()
