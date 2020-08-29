# readfile function
def rf(filename):
    return open(filename, "r").read()

# import external files
exec(rf("fileServer.py"))

# main body

# arg1 defines live server port
startServer(8080)