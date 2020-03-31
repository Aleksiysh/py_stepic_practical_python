

# a = [x.split(":")[1] for x in input().split()]
# a = {int(x.split(":")[0]): x.split(":")[1] for x in input().split()}

a = {int(k): v for k, v in (s.split(':') for s in input().split(' ') if s)}
pass
