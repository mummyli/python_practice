from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile

with TemporaryFile("w+t") as f:
    f.write("Hello\n")
    f.write("World!\n")

    f.seek(0)
    print(f.read())


with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)