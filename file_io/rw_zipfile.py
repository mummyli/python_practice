import gzip, bz2


data = ""
filename = "./testfiles/somefile.txt"
with open(filename, "rt") as f:
    data = f.read()

with gzip.open("./testfiles/data.bin", "wb") as f:
    f.write(data.encode("utf-8"))

    
with gzip.open("./testfiles/somefile.gz", "wt") as f:
    f.write(data)


with bz2.open("./testfiles/somefile.bz2", "wt", compresslevel=5) as f:
    f.write(data)

with gzip.open("./testfiles/somefile.gz", "rt") as f:
    print(f.read())

with bz2.open("./testfiles/somefile.bz2", "rt") as f:
    print(f.read())