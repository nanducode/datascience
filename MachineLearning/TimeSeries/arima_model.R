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
timedf<-ts(tdf,frequency = 12)
imputedf<-na.kalman(timedf)
fwrite(timedf,"jnk.csv")
write.csv(tdf,"jnk.csv")
library(imputeTS)
timedf<-ts(tdf,frequency = 12)
imputedf<-na.kalman(timedf)
write.csv(imputedf,"imputefull.csv")
temprow <- matrix(c(rep.int(NA,length(imputedf))),nrow=5,ncol=length(imputedf))
newrow <- data.frame(temprow)
colnames(newrow) <- colnames(imputedf)
rownames(newrow) <- c("2008","2009","2010","2011","2012")
newrow
write.csv(newrow,"newrow.csv")
nrow(newrow)
newrow[1]
armafit<-auto.arima(imputedf)
library.install(forecast)
install.packages("forecast")
install.packages("forecast")
save.image("~/Work/AppliedProject/imputesession.RData")
install.packages("forecast")
install.packages("forecast")
imputeinterdf<-na.interpolation(timedf)
library(imputeTS)
imputeinterdf<-na.interpolation(timedf)
library(data.table)
typeof(newrow)
fwrite(newrow,"newrow.csv")
nrow(newrow)
rownames(newrow)
colnames(newrow)
ncol(newrow)
length(imptedf)
length(imputedf)
ncol(imputedf)
temprow <- matrix(c(rep.int(NA,ncol(imputedf))),nrow=5,ncol=ncol(imputedf))
newrow <- data.frame(temprow)
colnames(newrow) <- colnames(imputedf)
rownames(newrow) <- c("2008","2009","2010","2011","2012")
fwrite(newrow,"newrow.csv")
fwrite(data.frame(newrow),"newrow.csv")
newrow[1]
write.csv(newrow,"newrow.csv")
rownames(imputedf)
library(forecast)
arimafit<-auto.arima(timedf)
methods(mice)
library(mice)
methods(mice)
newrow[1]
fit<-auto.arima(imputedf[1])
is.na(imputedf[1])
imputedf[1]
imputedf[2]
imputedf[3]
nrow(imputedf)
timedf[1]
newimputedf<-data.frame(imputedf)
newimputedf[1]
newimputedf<-lapply(imputedf,function(x) ifelse(is.na(x),mean(x,na.rm=TRUE),x))
fit<-auto.arima(newimputedf[1])
imputedf[1]
newimputedf[1]
newimputedf[6]
newimputedf[7]
newimputedf[9]
newimputedf[10]
newimputedf[11]
newimputedf[12]
newimputedf[14]
fit<-auto.arima(newimputedf[14])
fit<-auto.arima(as.numeric(newimputedf[14]))
jnk<-as.numeric(newimputedf[14])
jnk<-newimputedf[14]
as.numeric(jnk)
jnk
as.numeric(unlist(jnk))
jnk<-as.numeric(unlist(newimputedf[14]))
fit<-auto.arima(as.numeric(unlist(newimputedf[14])))
output<-predict(fit,n.ahead=5)
output
data.frame(output)
(data.frame(output))$pred
(data.frame(output$pred))
fit<-auto.arima(as.numeric(unlist(newimputedf[1])))
output<-predict(fit,n.ahead=5)
output
newimputedf<-lapply(imputedf,function(x) auto.arima(as.numeric(unlist(x)))
;
fit<-lapply(imputedf,function(x) auto.arima(as.numeric(unlist(x))))
newimputedf<-lapply(imputedf,function(x) auto.arima(as.numeric(unlist(x)))
;
ncol(newimputedf)
newimputedf<-lapply(imputedf,function(x) if(is.na(x) || is.null(x)) {} else {auto.arima(as.numeric(unlist(x)))})
newimputedf<-lapply(imputedf,function(x) if(is.constant(x) || is.null(x)) {} else {auto.arima(as.numeric(unlist(x)))})
newimputedf<-lapply(imputedf,function(x) if(is.na(x) || is.null(x)) {} else {auto.arima(as.numeric(unlist(x)))})
cols(newimputedf)
ncol(newimputedf)
nrow(newimputedf)
newimputedf<-lapply(imputedf,function(x) if(!(is.constant(x) || is.na(x) || is.null(x))){auto.arima(as.numeric(unlist(x)))})
nrow(newimputedf)
ncol(newimputedf)
output<-lapply(newimputedf,functio(x) predict(x,n.ahead=5))
typeof(newimputedf)
length(newimputedf)
output<-lapply(newimputedf,function(x) predict(x,n.ahead=5))
ncol(imputedf)
output<-lapply(newimputedf,function(x) (predict(x,n.ahead=5))$pred)
output<-predict(newimputedf[1],n.ahead=5)
newimputedf[1]
newimputedf[2]
newimputedf[3]
newimputedf[4]
newimputedf[5]
newimputedf[6]
newimputedf[7]
newimputedf[8]
newimputedf[9]
newimputedf[10]
newimputedf[11]
newimputedf[14]
output<-lapply(newimputedf,function(x) if(!is.null(x)){(predict(x,n.ahead=5))$pred})
output<-lapply(newimputedf,function(x) if(!(is.null(x)){(predict(x,n.ahead=5))$pred})
output<-lapply(newimputedf,function(x) if(!(is.null(x))){(predict(x,n.ahead=5))$pred})
output<-lapply(newimputedf,function(x) if(!(is.null(x) || is.na(x))){(predict(x,n.ahead=5))$pred})
for (i in newimputedf) {}
for (i in newimputedf) {
if(is.null(i)){paste("NULL")}
}
for (i in newimputedf) {
if(is.null(i)){paste("NULL")}
}
for (i in newimputedf) {
if(is.na(i)){paste("NULL")}
}
for (i in newimputedf) {
paste(i)
}
length(newimputedf)
for (i in newimputedf) {
i
}
newimputedf[[1]]
newimputedf[[2]]
newimputedf[[14]]
is.null(newimputedf[[1]])
for i in 1:length(newimputedf):
is.null(newimputedf[[14]])
imputedf[[1]]
imputedf[[14]]
imputedf[[15]]
imputedf[1]
imputedf[14]
imputedf[15]
type(imputedf)
typeof(imputedf)
finaldf<-data.frame(imputedf)
finaldf[1]
(colnames(finaldf))[1]
(colnames(finaldf))[2]
finaldf<-lapply(imputedf,function(x) ifelse(is.na(x),mean(x,na.rm=TRUE),x))
newimputedf<-lapply(imputedf,function(x) if(!(is.na(x) || is.null(x))){auto.arima(as.numeric(unlist(x)))})
newimputedf[[1]]
newimputedf[[2]]
newimputedf[[14]]
newimputedf<-lapply(finaldf,function(x) if(!(is.na(x) || is.null(x))){auto.arima(as.numeric(unlist(x)))})
newimputedf[[2]]
newimputedf[[1]]
output<-lapply(newimputedf,function(x) if(!is.null(x)){(predict(x,n.ahead=5))$pred})
output1<-lapply(newimputedf,function(x) if(!is.null(x)){(predict(x,n.ahead=5))$pred})
typeof(finaldf)
nrow(finaldf)
typeof(imputedf)
class(imputedf)
class(newimputedf)
class(finaldf)
output1<-predict(newimputedf[[1]],n.ahead=5)
output1
length(newimputedf)
temprow <- matrix(c(rep.int(NA,0),nrow=5,ncol=0))
newrow <- data.frame(temprow)
colnames(newrow) <- colnames(finaldf)
rownames(newrow) <- c("2008","2009","2010","2011","2012")
nrow(temprow)
temprow
temprow <- matrix(c(rep.int(NA,length(finaldf))),nrow=5,ncol=length(finaldf))
newrow <- data.frame(temprow)
colnames(newrow) <- colnames(finaldf)
rownames(newrow) <- c("2008","2009","2010","2011","2012")
newrow[1]<-t(output$pred)
output$pred
jnk<-output$pred
jnk
jnk[1]
jnk[1:5]
newrow[1]<-t(jnk[1:5])
jnk2<-jnk[1:5]
jnk2
t(jnk2)
jnk2
newrow[1]
newrow[1][2]
newrow[[1]]
newrow[[1]]<-jnk2
newrow[1]
colnames(newrow[1])
colnames(newrow)
temprow <- matrix(c(rep.int(NA,length(finaldf))),nrow=5,ncol=length(finaldf))
newrow <- data.frame(temprow)
colnames(newrow) <- colnames(data.frame(finaldf))
rownames(newrow) <- c("2008","2009","2010","2011","2012")
for (i in 1:5) {
if(!is.na((newimputedf[[i]])))
{
output<-predict(newimputedf[[i]],n.ahead=5)
jnk<-output$pred
jnk2<-jnk[1:5]
newrow[[i]]<-jnk2
}
}
newimputedf[[1]]
i
newimputdf[[i]]
newimputedf[[i]]
for (i in 1:5) {
output<-predict(newimputedf[[i]],n.ahead=5)
jnk<-output$pred
jnk2<-jnk[1:5]
newrow[[i]]<-jnk2
}
newrow
newrow[1:5]
newrow[1:6]
newrow[1:7]
for (i in 1:length(newimputedf)) {
output<-predict(newimputedf[[i]],n.ahead=5)
jnk<-output$pred
jnk2<-jnk[1:5]
newrow[[i]]<-jnk2
}
for (i in 1:length(newimputedf)) {
paste(i)
output<-predict(newimputedf[[i]],n.ahead=5)
jnk<-output$pred
jnk2<-jnk[1:5]
newrow[[i]]<-jnk2
}
i
newimputedf[[24]]
newimputedf[[23]]
newimputedf[[25]]
newrow[[i]]
newrow[[23]]
for (i in 1:length(newimputedf)) {
paste(i)
fit<-newimputedf[[i]]
output<-predict(newimputedf[[i]],n.ahead=5)
jnk<-output$pred
jnk2<-jnk[1:5]
newrow[[i]]<-jnk2
}
fit
newjnk<-predict(fit,n.ahead=5)
newimputedf[[23]]
for (i in 1:length(newimputedf)) {
paste(i)
fit<-newimputedf[[i]]
output<-forecast(fit,n.ahead=5)
jnk<-output$pred
jnk2<-jnk[1:5]
newrow[[i]]<-jnk2
}
nrow(newrow)
ncol(newrow)
ncol(newimputedf)
length(newimputedf)
newrow[1]
newrow[[1]]
for(i in 1:5){
paste(i)
}
i
for(i in 1:5)
{
print(i)
}
sink("countjnk.txt")
for(i in 1:5)
{
print(i)
}
sink()
{
print(i)
}
for(i in 1:5)
{
print(i)
}
temprow <- matrix(c(rep.int(NA,length(finaldf))),nrow=5,ncol=length(finaldf))
newrow <- data.frame(temprow)
colnames(newrow) <- colnames(data.frame(finaldf))
rownames(newrow) <- c("2008","2009","2010","2011","2012")
ncol(newrow)
length(newimputedf)
jnk2
output<-forecast(newimputedf[[1]],n.ahead=5)
help forecast()
help forecast
?forecast()
output<-forecast(newimputedf[[1]],h=5)
output
jnk<-output$x
jnk
jnk<-output$fitted
jnk
jnk<-output$series
jnk
output
output$residuals
output$mean
jnk<-output$mean
jnk
newrow[[1]]<-jnk
newrow[1]
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
nrow(newrow)
ncol(newrow)
newrow[157]
newrow[159]
newrow[556]
project<-newrow
project[1]
write.csv(t(project),"projection.csv")
