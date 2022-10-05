# this script is to take the mpxv nextstrain metadata and
# join with WA mpxv metadata to show the metadata in the
# mpxv nextstrain build
# Author: Stephanie Lunn
# Date: 221005

# import pandas
import pandas as pd

# read in csv files
nextstrain = pd.read_csv('~/monkeypox/data/metadata.tsv', sep='\t', parse_dates=['date'])
wa = pd.read_csv('~/monkeypox/data/doh_metadata_2022-08-18_linkedWDRS.csv', parse_dates=['collect_date'])
print(type(wa['collect_date']))

# print column headers
print(list(nextstrain.columns))
print(list(wa.columns))

# rename columns in wa metadata to match nextstrain
wa = wa.rename(columns={
    'collect_date': 'date',
    'genbank': 'genbank_accession_rev',
    'PATIENT__AGE': 'age',
    'PATIENT__ADMINISTRATIVE__SEX': 'sex',
    'PATIENT__ADDRESS__CORRECTED__COUNTY': 'county'})

# set index
nextstrain = nextstrain.set_index('genbank_accession_rev', drop=False)
wa = wa.set_index('genbank_accession_rev', drop=False)

# convert collect_date to YYYY-MM-DD
wa['date'] = pd.to_datetime(wa['date']).dt.strftime('%Y-%m-%d')
print(wa['date'].head(10))

# replace wa collection dates
nextstrain_dates = pd.DataFrame(nextstrain.loc[:, 'date'])
wa_dates = pd.DataFrame(wa.loc[:, 'date'])
new_dates = wa_dates.append(nextstrain_dates)
# drop duplicates
new_dates = new_dates.drop_duplicates('date')
new_dates = pd.DataFrame(new_dates)
# replace nextstrain metadata dates with updated dates
new_df = pd.DataFrame(nextstrain.replace(to_replace=nextstrain['date'], value=new_dates['date'], inplace=False))

# add age, sex, and county columns
new_df[['age', 'sex', 'county']] = wa[['age', 'sex', 'county']]

# write out to gzip compressed tsv file
new_df.to_csv('metadata.tsv.gz', sep='\t', compression='gzip')



