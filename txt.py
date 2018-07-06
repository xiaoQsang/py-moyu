def log_the_string(comment):
    logFile = 'wei,zaima.txt'
    with open(logFile, 'a')as lf:
        lf.write(comment + '\n')
    return 0

if __name__ == '__main__':
    log_the_string('buzai,cmn')