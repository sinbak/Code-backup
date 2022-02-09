import turtle as t
def frectal(n):
    if n <= 5:
        for i in range(3):
            t.forward(n)
            t.right(120)
        return
    next_n = n/2
    frectal(next_n)
    t.forward(next_n)
    frectal(next_n)
    t.backward(next_n)
    t.right(60)
    t.forward(next_n)
    t.left(60)
    frectal(next_n)
    t.right(60)
    t.backward(next_n)
    t.left(60)
t.speed(0)
frectal(160)
t.hideturtle()
t.done()
# 참고자료 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=mario002&logNo=2214502043