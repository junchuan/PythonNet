import optparse

parser=optparse.OptionParser('usage %prog -H <targethost> -p <target port>')
parser.add_option("-H",dest='tgtHost',type='string',help='specify target host')

parser.add_option("-p",dest='tgtPort',type='int',help='specify target port')

(option,args)=parser.parse_args()

tgtHost=option.tgtHost
tgtPort=option.tgtPort

if tgtHost==None | tgtPort==None:
    print parser.usage

    exit(0)



def testPass(cryptPass):
    salt = cryptPass[0:2]
    pass


def test2():
    testPass("sss")
