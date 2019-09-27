FullFact.2.2<-function(){
  A<-c(-1,1,-1,1)
  B<-c(-1,-1,1,1)
  AB<-A*B
  df<-data.frame(A,B,AB)
  rn<-c("1","a","b","ab")
  row.names(df)<-rn
  return(df)  
}
(ff22<-FullFact.2.2())
rowct<-nrow(ff22)
colct<-ncol(ff22)
for (xrow in 1:rowct) { ff22[xrow+4,]<-ff22[xrow,]}

rownames(ff22)[rowct+1]<-"c"
for(xrow in 2:rowct){rownames(ff22)[rowct+xrow]<-paste(rownames(ff22)[xrow],"c",sep"")}

nextFF<-function(ff2k) {
  rowct<-nrow(ff2k)
  colct<-ncol(ff2k)
  for(xrow in 1:rowct) {
    for (xrow in 1:rowct) { ff22[xrow+rowct,]<-ff22[xrow,]}
    
  }
  X<-c(rep(-1,rowct),rep(1,rowct))
  ff2k<-cbind(ff2k,X)
  k<-log2(colct+1)
  ultr<-LETTERS[k+1]
  names(ff2k)[colct+1]<-ultr
  
  
  return(ff2k)
}