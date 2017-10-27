import pandas as pd
import os.path

files = [
    "cats.csv",
    "near.csv",
    "quest.csv",
    "where.csv"
]

JOIN_COL = ['cat1','cat2']


def t(x):
    return os.path.splitext(x)[0]


def run():

    tables = [
        pd.read_csv(name, index_col=None)
        for name in files
    ]

    for i, table_one in enumerate(tables[:-1]):
        for j, table_two in enumerate(tables[i + 1:]):
            name1 = t(files[i])
            name2 = t(files[i + j + 1])
            out_name = "%s_%s.csv" % (name1, name2)

            join = pd.merge(table_one, table_two, on=JOIN_COL)
            col1 = join.columns[-2]
            col2 = join.columns[-1]
            col_name1 = "precent_" + name1
            col_name2 = "precent_" + name2

            join["precent_" + name1] = join[col1]
            join["precent_" + name2] = join[col2]

            del join[col1]
            del join[col2]

            join['ratio1'] = join[col_name1]/join[col_name2]
            join['ratio2'] = join[col_name2]/join[col_name1]
            # save

            join.to_csv(out_name)

    # point3 = df.dropna(thresh=10)
    # clean = point3.fillna(0)
    # test = clean.groupby(['cat1', 'cat2'])['cpercentage'].mean()


if __name__ == "__main__":
    run()
