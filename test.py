import pandas as pd
print(pd.__version__)
df = pd.read_excel('test.xls')
print(len(df.values))

def highlight_max(x):
    return ['background-color: yellow' if ('Total' in x.values) else ''
                for v in x]

df.style.apply(highlight_max,axis=1).to_excel("styled.xlsx", engine="openpyxl",index=None)

# for c in df.values:
#     if ('Total' in c):
#         c[2] = "吃饭"
#         print(c)
