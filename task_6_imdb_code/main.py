import pandas as pd
pd.set_option('display.max_columns', 60)
pd.set_option('display.max_rows', 30)

url_path = 'https://datasets.imdbws.com/'
file_name = 'name.basics.tsv.gz'


def imdb_find_alive_primary_producers():
    print('Starting IMDb process...')

    imdb_df = pd.read_csv(f'{url_path}{file_name}', compression='gzip', header=0, sep='\t', quotechar='"')
    # Dataset column names: ['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']

    print('Data imported, beginning filters')

    # filter the data where there is no death year, using escape character
    imdb_is_alive_df = imdb_df[imdb_df.deathYear == r'\N']

    # search the data for where the primary profession contains producer as interim step (to reduce dataset size)
    imdb_is_alive_producer_df = imdb_is_alive_df[imdb_is_alive_df['primaryProfession'].str.contains("producer", na=False)]

    # split primary profession column to more easily identify the first value
    imdb_is_alive_producer_df[['primaryProfession1', 'primaryProfession2', 'primaryProfession3']] = \
        imdb_is_alive_producer_df['primaryProfession'].str.split(',', expand=True)

    # first of 3 primary professions are producer
    imdb_is_alive_primary_producer_df = imdb_is_alive_producer_df[imdb_is_alive_producer_df.primaryProfession1 == 'producer']

    # print answer to user
    print(f'The number of primary profession 1 producers who are alive in the IMDb dataset: {len(imdb_is_alive_primary_producer_df)}')


if __name__ == '__main__':
    imdb_find_alive_primary_producers()

