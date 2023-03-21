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
while w < (a):
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




print('------------------------')



#x_keys = list(x.keys())
#print(x_keys)
#x_values = list(x.values())
#print(p_values)
p = ['d', 'b', 'c', 'a', 'e']
x = {p[0]: 11, p[1]: 20, p[2]: 33, p[3]: 44, p[4]: 55}
o = 0

while o < len(x):
    if p[o] == 'a':
         break
    if x[p[o]] == 20:
        o += 1
        continue
    print(o)
    print(p[o])
    print(x[p[o]])
    o += 1



for q in p:
    if q == 'a':
        break
    if x[q] == 20:
        continue
    print(q)
    print(x[q])
