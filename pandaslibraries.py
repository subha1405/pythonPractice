import pandas as pd
import matplotlib.pyplot as plt
# df=pd.DataFrame(
#     {
#         "NAME":["abdul","Sankar","Rajneesh","abdul","Sankar","Rajneesh","abdul","Sankar","Rajneesh","abdul","Sankar","Rajneesh"],
#         "SEX":["MALE","MALE","MALE","MALE","MALE","MALE","MALE","MALE","MALE","MALE","MALE","MALE"]
#     }
# )
# print(df.head(1))
# print(df.tail(9))


# Reading a csv file
studentscorelist=pd.read_csv("studentlist.csv")
print(studentscorelist.head())
print(studentscorelist[["AGE","SCORE"]].describe())
studentscorelist.plot.scatter(x="AGE",y="SCORE")
# plt.xlabel("AGE")
# plt.ylabel("SCORE")
# plt.title("SCORECARD")
# plt.show()