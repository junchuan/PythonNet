import optparse
import argparse


def main():

    parser=argparse.ArgumentParser()

    parser.add_argument("-H","--host")
    parser.add_argument("-p","--port")

    #parser=optparse.OptionParser('usage %prog -H <targethost> -p <target port>')

    #parser.add_argument("-H",dest='tgtHost',type='string',help='specify target host')

    #parser.add_argument("-p",dest='tgtPort',type='int',help='specify target port')

    args=parser.parse_args()

    print args

    tgtHost=args.host
    tgtPorts= args.port.split(',')


    print tgtPorts

    if tgtHost==None or tgtPorts==None:
        print parser.usage

        exit(0)
    portScan(tgtHost,tgtPorts)


from socket import *
def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
        connSkt.connect(tgtHost,tgtPort)
        connSkt.send("violent python\r\n")
        results=connSkt.recv(100)


        print "%d TCP open" % tgtPort

        print str(results)

        connSkt.close()

    except:
        print "%d TCP close" % tgtPort

import nmap
def nmapScan(tgtHost,tgtPort):
    nmScan=nmap.PortScanner()

    nmScan.scan(tgtHost,tgtPort)
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']

    print tgtHost+'/tcp'+tgtPort+" "+state


def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "Cannot resolve %s :Unknown host" % tgtHost

        return

    try:
        tgtName=gethostbyaddr(tgtIP)

        print "Scan Results for : ", tgtName[0]
    except:
        print 'Scan Results for ',tgtIP

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost,tgtPort)
        #print "scanning ports", tgtPort
        #connScan(tgtHost,int(tgtPort))

if __name__=="__main__":
    main()
















