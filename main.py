from synsets import synsets_gen

def main():
    for x in data:
        print synsets_gen(x)

#main()

#print(synsets_gen("ahad"))

aa =  ['one', 'two', 'three', 'satu']
bb = ['two', 'one', 'three', 'kygo', 'anton']

def testcase(a, b):
    print a <= b
    return a == b

testcase(aa,bb)