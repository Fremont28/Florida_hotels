orlando=read.csv("orl_count.csv")
#subset words 
orlando_sub=subset(orlando,word=="wifi"|word=="walt"|word=="villa"|
                     word=="vacation"|word=="universal"|word=="studios"|
                     word=="pool"|word=="orlando"|word=="magic"|
                     word=="disney")

#plot word frequency 
color="blue"
ggplot(orlando_sub,aes(x=word,y=count))+geom_bar(stat="identity",fill=color)+
  xlab("Word")+ylab("Count")+ggtitle("Orlando Themed Hotel Reviews")+
  theme(plot.title = element_text(hjust = 0.5)) 