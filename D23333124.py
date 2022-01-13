import statistics
import random
import plotly_express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

curvyyy_the_first=pd.read_csv("StudentsPerformance.csv")

mean= sum(curvyyy_the_first["reading score"])/len(curvyyy_the_first["reading score"])
sd = statistics.stdev(curvyyy_the_first["reading score"])
pone=len(curvyyy_the_first["reading score"])/100
mode = statistics.mode(curvyyy_the_first["reading score"])
median = statistics.median(curvyyy_the_first["reading score"])

sd11=mean-sd
sd12=mean+sd
d1=[result for result in curvyyy_the_first["reading score"] if result>sd11 and result<sd12]
pd1=len(d1)/pone

sd21=mean-(2*sd)
sd22=mean+(2*sd)
d2=[result for result in curvyyy_the_first["reading score"] if result>sd21 and result<sd22]
pd2=len(d2)/pone

sd31=mean-(3*sd)
sd32=mean+(3*sd)
d3=[result for result in curvyyy_the_first["reading score"] if result>sd31 and result<sd32]
pd3=len(d3)/pone

print("THE MEAN IS",mean)
print("THE MODE IS",mode)
print("THE MEDIAN IS",median)
print("THE PERCENTAGE FOR FIRST SD IS",pd1)
print("THE PERCENTAGE FOR SECOND SD IS",pd2)
print("THE PERCENTAGE FOR THIRD SD IS",pd3)

fig = ff.create_distplot([curvyyy_the_first["reading score"]],["reading_scores"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sd12,sd12 ], y=[0, 0.17], mode="lines", name="SD1"))
fig.add_trace(go.Scatter(x=[sd22,sd22 ], y=[0, 0.17], mode="lines", name="SD2"))
fig.add_trace(go.Scatter(x=[sd32,sd32 ], y=[0, 0.17], mode="lines", name="SD3"))
fig.add_trace(go.Scatter(x=[sd11,sd11 ], y=[0, 0.17], mode="lines", name="SD1"))
fig.add_trace(go.Scatter(x=[sd21,sd21 ], y=[0, 0.17], mode="lines", name="SD2"))
fig.add_trace(go.Scatter(x=[sd31,sd31 ], y=[0, 0.17], mode="lines", name="SD3"))
fig.show()