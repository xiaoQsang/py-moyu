import time
def log_the_string(comment):
    logFile = 'log.txt'
    logTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with open(logFile, 'a')as lf:
        lf.write(logTime + '\t' + comment + '\n')
    return 0

if __name__ == '__main__':
    log_the_string('hello')