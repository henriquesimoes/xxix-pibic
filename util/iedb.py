from os import path

import pandas as pd


class Normalizer:
    def __init__(self, df):
        self.df = df.copy()

    def columns(self, column_mapper):
        self.df = self.df.rename(columns=column_mapper)[column_mapper.values()]
        return self

    def chains(self, chain1_col, chain1_type, chain2_col, chain2_type):
        self.df = self.df.loc[(self.df[chain1_col] == chain1_type) & (self.df[chain2_col] == chain2_type)]
        return self

    def keep(self, columns):
        self.df = self.df[columns]
        return self

    def filter(self, column, pattern):
        self.df = self.df.loc[self.df[column].str.contains(pattern)]
        return self

    def drop_nan(self):
        self.df.dropna(inplace=True)
        return self

    def drop_duplicates(self):
        self.df.drop_duplicates(inplace=True)
        return self

    def trim(self, columns):
        self.df[columns] = self.df[columns].apply(lambda x: x.str.strip())
        return self

    def finish(self):
        return self.df


class IEDBDataset:
    def __init__(self, dir, file, norm=True):
        self.file = file
        self.dir = dir
        self.raw = self._load()
        self.data = self._normalize(self.raw) if norm else self.raw

    def _load(self):
        file_path = path.join(self.dir, self.file)
        return pd.read_csv(file_path)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return '{name} (from: {file}, rows: {len})'.format(
            name=type(self).__name__,
            file=self.file,
            len=len(self),
        )

    @staticmethod
    def _normalize(csv):
        df = Normalizer(csv) \
            .columns({
                'Description': 'epitope',
                'Chain 1 Type': 'chain1_type',
                'Chain 2 Type': 'chain2_type',
                'Chain 1 CDR3 Calculated': 'cdrh3',
                'Chain 2 CDR3 Calculated': 'cdrl3',
            }) \
            .trim(['chain1_type', 'chain2_type']) \
            .chains(chain1_col='chain1_type', chain1_type='heavy', chain2_col='chain2_type', chain2_type='light') \
            .keep(['epitope', 'cdrl3', 'cdrh3']) \
            .trim(['epitope', 'cdrl3', 'cdrh3']) \
            .filter(column='epitope', pattern=r'^[A-Z]+$') \
            .drop_nan().drop_duplicates().finish()

        return df.set_index('epitope')
