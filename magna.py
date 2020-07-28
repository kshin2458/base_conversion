from base_conversion import Number
import logging
import sys
logger = logging.getLogger('Logging')

logger.setLevel("INFO")
fh = logging.FileHandler('magna.log')
logger.addHandler(fh)
input1=int(sys.argv[1])
logger.info("####Start number {}####".format(input1))
count=1
while True:
    num2=Number(input1).get_new_number(2)
    while num2[-1]=="0":
        num2=num2.rstrip("0")
    if len(num2)==1:
        logger.info({count: [int(num2),None]})
        print("{}: finish!".format(num2))
        break
    else:
        l=int(num2)
    num3=Number(int(num2,2)).get_new_number(3)
    num3=num3+"1"
    m=int(num3)
    input1=int(num3,3)
    logger.info({count: [l,m]})
    count=count+1

