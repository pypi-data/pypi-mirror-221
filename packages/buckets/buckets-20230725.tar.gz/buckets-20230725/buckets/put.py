import sys
import requests

requests.packages.urllib3.disable_warnings()


def main():
    res = requests.put(sys.argv[1], data=sys.stdin.read(), verify=False)

    if 200 != res.status_code:
        print(res.content.decode())
        exit(1)

    print('db      : {}'.format(res.headers['x-db']))
    print('key     : {}'.format(res.headers['x-key']))
    print('version : {}'.format(res.headers['x-version']))
    print('length  : {}'.format(res.headers['content-length']))


if '__main__' == __name__:
    main()
