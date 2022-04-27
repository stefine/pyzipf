import pandas as pd
# Recall that Zipf’s Law states the second most common word in a body of text appears half
# as often as the most common, the third most common appears a third as often, and so on.
# Mathematically, this might be written as “word frequency is proportional to 1/rank.”
# 意思是: 第二名出现次数是第一名出现次数的1/2，第三名的是第一名的1/3, 以此类推...
# 换句话就是: 它们的比分别是: 1:0.5:0.33:0.25...

input_csv = 'results/jane_eyre.csv'
df = pd.read_csv(input_csv, header=None,
                 names=('word', 'word_frequency'))
df['rank'] = df['word_frequency'].rank(ascending=False,
                                       method='max')
df['inverse_rank'] = 1 / df['rank']
scatplot = df.plot.scatter(x='word_frequency',
                           y='inverse_rank', figsize=[12, 6],
                           grid=True)
fig = scatplot.get_figure()
fig.savefig('results/jane_eyre.png')