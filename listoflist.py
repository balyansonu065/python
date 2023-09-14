value = ["Gfg" , 3 , "is" , 8 , "Best" , 10 , "for" , 18 , "Geeks" , 31]
keywords = ["name" , "number"]
n = len(value)
res = []
for i in range(0,n,2):
    res.append( {keywords[0]:value[i] , keywords[1]:value[i+1]} )

print(str(res))