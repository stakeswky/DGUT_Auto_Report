from gevent import monkey;monkey.patch_all()
import click
from dgut_requests.dgut import dgutIllness, requests
from retry import retry
import gevent
import sys


@retry(tries=50, delay=2, backoff=2, max_delay=30)
def clock(u: dgutIllness, key: str=None) -> None:
    '''
    打卡并输出结果
    :param u: dgutIllness, 指定打卡的dgutIllness对象
    :param key: str | None, 指定Server酱的key
    :returns: None，打印结果
    '''
    result = u.report().get("message")
    print(u.username[-2:], '-', result) 
    if key and not "今日已打卡" in result:
        headers = {
            'Content-type': "application/x-www-form-urlencoded"
        }
        data = {
            "title": u.username + result[1:],
        }
        res = requests.post(f'https://sctapi.ftqq.com/{key}.send', data=data, headers=headers)
        if res.status_code == 200 and res.json().get("code") == 0:
            print(u.username[-2:]+"推送成功")





@click.command()
@click.option('-U', '--username', required=True, help="中央认证账号用户名", type=str)
@click.option('-P', '--password', required=True, help="中央认证账号密码", type=str)
@click.option('-K', '--key', help="server酱的key值", type=str)
def main(username, password, key):
    users = username.split(",")
    pwds = password.split(",")
    if key:
        keys = key.split(",")
    # locations = {int(item.split(',')[0]): (float(item.split(',')[1]), float(item.split(
    #     ',')[2])) for item in location.strip('[] ').split('],[')} if location else {}
    if len(users) != len(pwds):
        exit("账号和密码个数不一致")
    tasks = []
    for i in range(len(users)):
        if key and i < len(keys) and keys[i] != '0':
            tasks.append(gevent.spawn(clock, u=dgutIllness(users[i], pwds[i]), key=keys[i]))
        else:
            tasks.append(gevent.spawn(clock, u=dgutIllness(users[i], pwds[i])))
    # for usr in enumerate(zip(users, pwds), 1):
        # u = dgutIllness(usr[1][0], usr[1][1])
        # tasks.append(gevent.spawn(clock, u=u, location=locations.get(usr[0])))
    gevent.joinall(tasks)

if __name__ == '__main__':
    main()
