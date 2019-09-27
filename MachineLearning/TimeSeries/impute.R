setwd("C:/Users/anand/Documents/Work/AppliedProject/")
df<-read.csv("Training.csv")
dfseries<-df$Series.Name
dfcountries<-df$Country.Name
dfseriescode<-df$Series.Code
dfindex<-df$X
drops<-c("X","Unnamed..0","Country.Name","Series.Code","Series.Name")
newdf<-df[,!(colnames(df) %in% drops)]
#Only data is retained
tdf<-t(newdf)
colnames(tdf)<-dfseries
write.csv(tdf,"jnkdfull.csv")
# imputeddf<-mice(tdf,m=5,maxit=50,method='pmm',seed=500)
# imputeddf<-mice(tdf,m=5,maxit=10,method='pmm',seed=500)
dfseries<-data.frame(dfseries)
dfseriescode<-data.frame(dfseriescode)
dfindex<-data.frame(dfindex)
dfcountries<-data.frame(dfcountries)
dfseriescode<-data.frame(t(dfseriescode))
dfseries<-data.frame(t(dfseries))
dfcountries<-data.frame(t(dfcountries))
dfindex<-data.frame(t(dfindex))
#dfseriescode<-cbind(jnk,dfseriescode)
#dfseries<-cbind(jnk,dfseries)
#dfindex<-cbind(jnk,dfindex)
#dfcountries<-cbind(jnk,dfcountries)
colnames(dfseries)<-colnames(tdf)
colnames(dfseriescode)<-colnames(tdf)
colnames(dfcountries)<-colnames(tdf)
colnames(dfindex)<-colnames(tdf)
nd<-rbind(dfcountries,dfseries)
nd<-rbind(nd,dfseriescode)
nd<-rbind(nd,dfindex)
nd[3]
nd[6]
tdf[1]
nrow(tdf)
tdf[2]
tdf[,1]
tdf[,2]
rownames(tdf)
library(imputeTS)
timedf<-ts(tdf,frequency = 1)


library(zoo)
install.packages("mcparallel")
library(mcparallel)
imputedf<-na.kalman(timedf)
#imputedf<-na.seadec(timedf)
#imputedf<-lapply(timedf,function(x)if(sum(!(is.na(x))) > 3){na.interp(x)})

x<-data.frame(imputedf)

write.csv(imputedf,"imputefull_forecast_interp.csv")



#Fill values with mean
finaldf<-lapply(imputedf,function(x) ifelse(is.na(x),mean(x,na.rm=TRUE),x))
write.csv(finaldf,"jnk.csv")

#Model fitting
library(forecast)
newimputedf<-lapply(finaldf,function(x) if(!(is.na(x) || is.null(x))){auto.arima(as.numeric(unlist(x)))})


temprow <- matrix(c(rep.int(NA,length(finaldf))),nrow=5,ncol=length(finaldf))
newrow <- data.frame(temprow)
colnames(newrow) <- colnames(data.frame(finaldf))
rownames(newrow) <- c("2008","2009","2010","2011","2012")
#If we use predict, there is a drift involved by auto.arima, so using forecast instead
for (i in 1:length(newimputedf))
{
fit<-newimputedf[[i]]
output<-forecast(fit,h=5)
jnk<-output$mean
newrow[[i]]<-jnk
}

project<-newrow
project[1]
write.csv(t(project),"projectionsinterp.csv")

