def tri(rows):
    spaces=(rows-1)
    stars=1
    total_Stars=2*rows-1
    while(stars<=total_Stars):
        print(' '*spaces,'*'*stars,sep="")
        stars+=2
        spaces-=1


tri(7)
