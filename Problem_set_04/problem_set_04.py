#!/usr/bin/env python3

cd /ufrc/zoo6927/share/moeinraja/problem_set_04/final
module load python
python3


###Create the cnv database:

from sqlalchemy import create_engine
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, Float
import pandas as pd
engine = create_engine('sqlite:///cnv.sqlite')
metadata = MetaData()

### create the reads table:
reads = Table('reads', metadata,
              Column('ID', Integer, primary_key = True),
			  Column('chromosome', String),
              Column('start', Integer),
              Column('end',Integer),
              Column('test', Integer),
			  Column('ref', Integer),
			  Column('position', Integer),
              )

### create the stats table:

stats = Table('stats', metadata,
              Column('ID', Integer, primary_key = True),
              Column('position', Integer, ForeignKey("reads.position")),
              Column('log2', Integer),
              Column('pvstat', Integer),
              Column('cnv', Integer),
              Column('copynumbervariantssize', String),
              Column('copynumbervariantlog2', String),
              Column('copynumbervariantpvstat', String),
              )
metadata.create_all(engine)


### Add the reads data to the reads table:
from sqlalchemy import create_engine
engine = create_engine('sqlite:///cnv.sqlite')
conn = engine.connect()


data=pd.read_csv('ps3.csv',encoding = 'Latin-1',usecols=['ID','chromosome','start','end','test','ref','position'])
i=0
while True:
    ins = reads.insert().values(ID=data['ID'].tolist()[i],chromosome=data['chromosome'].tolist()[i],start=data['start'].tolist()[i],end=data['end'].tolist()[i],test=data['test'].tolist()[i],ref=data['ref'].tolist()[i],position=data['position'].tolist()[i])
    conn.execute(ins)
    i=i+1
    if i == len(data['ID'].tolist()):
        print('done!')
        break
		

		
### Add the stats data into the stats table:
from sqlalchemy import create_engine
engine = create_engine('sqlite:///cnv.sqlite')
conn = engine.connect()
data = pd.read_csv('ps3.csv',encoding = 'Latin-1',usecols=['ID','position','log2','pvstat','copynumbervariants','copynumbervariantssize','copynumbervariantlog2','copynumbervariantpvstat'])
i=0
while True:
    ins = stats.insert().values(ID=data['ID'].tolist()[i],position=data['position'].tolist()[i],log2=data['log2'].tolist()[i],pvstat=data['pvstat'].tolist()[i],copynumbervariants=data['copynumbervariants'].tolist()[i],copynumbervariantssize=data['copynumbervariantssize'].tolist()[i],copynumbervariantlog2=data['copynumbervariantlog2'].tolist()[i],copynumbervariantpvstat=data['copynumbervariantpvstat'].tolist()[i])
    conn.execute(ins)
    i=i+1
    if i == len(data['ID'].tolist()):
        print('done!')
        break

quit()
		
### Checking to see if the data were added or not:

module load sqlite
sqlite3
.open cnv.sqlite
SELECT COUNT(*) FROM reads;
200575
SELECT COUNT(*) FROM stats;
200575


#
# End of script