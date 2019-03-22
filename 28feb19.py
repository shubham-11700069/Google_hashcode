landscape=[]
tags={}
ntags=[]
#N=int(input())

Hzl,Vtcl=[],[]
file=open('c_memorable_moments.txt','r')
N=int(file.readline())
'''file=[['H', '3', 'cat', 'beach', 'sun'],['V', '2', 'selfie', 'smile'],
      ['V', '2', 'garden', 'selfie'],['H', '2', 'garden', 'cat']]
'''
for _ in range(N):
    f=file.readline()
    line=list(map(str,f[:-1].split(' ')))
    #line=list(map(str,input().split(' ')))
    #line=file[_]
    landscape.append(line[0])
    if (line[0]=='H'):
        Hzl.append(_)
    else:
        Vtcl.append(_)
    tags[_]=line[2:]
    ntags.append(line[1])
    

#print(tags)

similartags={}
phototags={}
tagnames={}
for i in range(N):
    for j in range(i+1,N):
        phototags['photo %s %s'%(i,j)]=0
        tagnames['photo %s %s'%(i,j)]=[]
        for k in (tags[i]):
            for l in (tags[j]):
                #if (k==l):
                if (('photo %s %s tag %s %s'%(i,j,k,l)) in similartags.keys()):
                    if (str(k)==str(l)):
                        similartags['photo %s %s tag %s %s'%(i,j,k,l)]+=1
                        
                else:
                    if (str(k)==str(l)):
                        similartags['photo %s %s tag %s %s'%(i,j,k,l)]=1
                        tagnames['photo %s %s'%(i,j)]+=['%s'%l]
                    else:
                        similartags['photo %s %s tag %s %s'%(i,j,k,l)]=0
                phototags['photo %s %s'%(i,j)]+=similartags['photo %s %s tag %s %s'%(i,j,k,l)]
                
#print(similartags)
#print(phototags)
#print(tagnames)
tagnames=sorted(tagnames.items(), key=lambda kv: (len(kv[1]), kv[0]))
#print(tagnames)
newtagnames=[]
for i in tagnames:
    if(len(i[1])!=0):
        #print(i)
        newtagnames.append(i)
'''for w in sorted(tagnames, key=tagnames.get, reverse=True):
  print (w, tagnames[w])
  '''
'''  
for i,j in phototags:
    if (j>0):
   '''    
'''print('3')
print('0')
print('3')
print('12') 
  '''
ofile=open('c_memorable_moments_sol.txt','w')
slides=len(newtagnames)+1
for i in newtagnames:
    if(landscape[int(i[0][6])] == 'V' and landscape[int(i[0][8])]=='V'):
        slides-=1
print(slides)
ofile.write('%s\n'%slides)
for i in newtagnames:
    if(landscape[int(i[0][6])] != 'V' and landscape[int(i[0][8])]!='V'):
        print(i[0][6])
        ofile.write('%s\n'%i[0][6])
        print(i[0][8])
        ofile.write('%s\n'%i[0][8])

    elif(landscape[int(i[0][6])] == 'V' and landscape[int(i[0][8])]=='V'):
        print(i[0][6], i[0][8])
        ofile.write('%s %s\n'%(i[0][6], i[0][8]))

ofile.close()
file.close()
