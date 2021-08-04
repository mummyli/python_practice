import io

s = io.StringIO()
s.write("Hello World!")
print(s.getvalue())


s = io.StringIO("Hello World!")
print(s.getvalue())

b = io.BytesIO(b"Hello World!")
print(b.getvalue())