import os

s1 = os.popen('git add .')
print(s1.read())
commit = input('请输入提交内容')
c = os.popen(f'git commit -m {commit}')
f = c.read()
print(f)

print(os.popen('git push').read())
