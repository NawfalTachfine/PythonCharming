import logging as lg

# File logging

lg.basicConfig(filename='out.log',
               level=lg.DEBUG,
               filemode='w',
               format='%(asctime)s\t%(levelname)s\t%(message)s',
               datefmt='%Y-%m-%d %H:%M:%S'
               )
# add filemode='w' to empty file with each execution
# remove filemode='w' to append with each execution

lg.info('here we go')
lg.debug('so far so good')
lg.warning('oh boy!')
