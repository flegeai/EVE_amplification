import pyBigWig
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--interval_size", required=False, default=10, help="interval size (default=10)") 
ap.add_argument("-b1", "--bigwig1", required=True, help="bigwig 1 file (denominator)")
ap.add_argument("-b2", "--bigwig2", required=True, help="bigwig 1 file (numerator)")
ap.add_argument("-c", "--chroms_list", required=True, help="List of the chromosomes")
ap.add_argument("-o", "--suffix", required=False, default="ratio", help="suffix of output files (default='ratio')")
args = vars(ap.parse_args())

chroms = []
with open(args['chroms_list']) as file:
    for line in file: 
        line = line.strip()
        chroms.append(line) 

st1=pyBigWig.open(args["bigwig1"])
st3=pyBigWig.open(args["bigwig2"])

interval_size=args['interval_size']
chrs=[]
for chrom in chroms:
    outbw = pyBigWig.open(chrom+"."+args["suffix"]+".bw", "w")
    chrs_header=[(chrom,st1.chroms(chrom))]
    outbw.addHeader(chrs_header, maxZooms=0)  
    scaff_size=st1.chroms(chrom)    
    for i in range(0,scaff_size,interval_size): 
        if (i+interval_size>=scaff_size): continue
        else: end=i+interval_size
        st1val=st1.values(chrom, i, end)[0]
        st3val=st3.values(chrom, i, end)[0]
        if st1val==0: value=0
        else :
            value=st3val/st1val   
        starts = np.array([i], dtype=np.int64)
        ends = np.array([end], dtype=np.int64)
        values = np.array([value], dtype=np.float64)
        chrs=[chrom]
        outbw.addEntries(chrs, starts, ends, values)
    outbw.close()  

