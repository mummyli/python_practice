def test():
    a = 12
    # exec()之前使用locals()来得到一个局部变量字典
    loc = locals()
    exec("b=a+1")
    b = loc["b"]
    print(b)

test()

'''
作为 locals() 的一个替代方案，你可以使用你自己的字典，并将它传递给 exec() 
'''

def test2():
    a = 12
    loc = {"a": a}
    glb = {}

    exec("b = a + 1", glb, loc)

    print(glb)
    print(loc)

test2()