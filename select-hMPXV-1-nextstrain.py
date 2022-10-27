# this script is to subset hMPXV-1 metadata from
# the nextstrain metadata file
# Author: Steph M. Lunn
# Date: 221011

# import pandas
import pandas as pd

# read file
nextstrain = pd.read_csv('~/monkeypox/data/metadata.tsv.gz',
    sep='\t',
    index_col=['genbank_accession_rev'],
    compression='gzip',
    parse_dates=['date'])

hMPXV = nextstrain[nextstrain['outbreak'] == 'hMPXV-1']

hMPXV.to_csv('~/monkeypox/data/metadata.tsv.gz', sep='\t', compression='gzip')