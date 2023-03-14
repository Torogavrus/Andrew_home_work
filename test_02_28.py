# my home-work

a = "hello world"
a += " !"
print(a)

a += "jfkdskba " \
    + "thsdsathuady"

print(a)

q = ['a', 'b', 'c', 'd', 'e']
x = 0
while x < 5:
    print(q[x])
    x += 1

print('---------------------------------------------------------------')

w = 0
while w < len(a):
    if a[w] in ['l', 's']:
        w += 1
        continue
    print(a[w])
    w += 1
    if a[w] == 'u':
        break

print('----------------------------------')


s = {'x': 10, 'q': 76, 'a': 9, 'b': 20, 'c': 3}

s_keys = list(s.keys())
print(s_keys)
s_values = list(s.values())
print(s_values)

o = 0

print('-----------------------while1')
while o < len(s):
    if s_keys[o] == 'a':
        break
    print(s[s_keys[o]])
    print(s_keys[o])
    o += 1

    #print(list(s.keys()[o]))
    #print(list(s.values())[o]
print('------------------------while2')
print(s_values)
print(s_keys)
o = 0
while o < len(s):
    if s_values[o] == 20:
        o += 1
        continue 
    print(s[s_keys[o]])
    print(s_keys[o])
    o += 1


print('-------------------------while3')
o = -1
while o < (len(s)-1):
    o += 1
    if  s_values[o] == 20:
        continue
    print(s[s_keys[o]])
    print(s_keys[o])




print('------------------------for')

for x in s_keys:
    if x == 'a':
        break
    print(s[x])
    print(x)


