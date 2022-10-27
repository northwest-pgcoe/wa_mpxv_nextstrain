# wa_mpxv
WA-focused config files for mpxv nextstrain

# Setup
First, install the [monkeypox nextstrain pipeline](https://github.com/nextstrain/monkeypox) and clone the monkeypox repository using `git clone https://github.com/nextstrain/monkeypox.git` or `gh repo clone nextstrain/monkeypox`.

Next, clone this repository in the `monkeypox/config` folder. You can do this in the command-line terminal by navigating to the `monkeypox` repository using `cd monkeypox/config` and then cloning the repository using `git clone https://github.com/DOH-SML1303/wa_mpxv.git` or `gh repo clone DOH-SML1303/wa_mpxv`.

# Retrieving sequencing and metadata files for the monkeypox nextstrain
The monkeypox sequencing data is maintained by the Nextstrain team and can be retrieved using `wget`. To retrieve the sequencing and metadata files, navigate to the `monkeypox/data` folder. While in the `data` folder in the terminal window, run the command `wget https://data.nextstrain.org/files/workflows/monkeypox/sequences.fasta.xz` to download the sequencing data and `wget https://data.nextstrain.org/files/workflows/monkeypox/metadata.tsv.gz` to download the metadata.

# Updating the metadata to include metadata for WA cases
The python script [wa-mpxv-metadata-update.py](https://github.com/DOH-SML1303/wa_mpxv/blob/main/wa-mpxv-metadata-update.py) will allow you to update the metadata in the nextstrain `metadata.tsv.gz` file with data from a separate spreadsheet containing the metadata for the WA cases. You may need to update the file path for the WA metadata on line 12. You can update the script as necessary (especially if the variables are different) in order to get the script to run.

To run the python script, use the command `python3 ~/monkeypox/config/wa_mpxv/wa-mpxv-metadata-update.py`. The `metadata.tsv.gz` will automatically replace the old metadata file.

Next, you will need to subset the hMPXV-1 cases in the master metadata file.* To run the python script, use the command `python3 ~/monkeypox/config/wa_mpxv/select-hMPXV-1-nextstrain.py`. This will automatically replace the `metadata.tsv.gz` file. *Please note that this step has been included as the filter step in the `wa_config_hmpxv1.yaml` on line 25 `filters: "--exclude-where outbreak!=hMPXV-1"` has been replaced with the filter step `filters: "--include-where 'division=Washington'"` to include all Washington state sequences.

# Running the WA-focused monkeypox build in nextstrain
Go through the proper steps of activating the `nextstrain` environment in the terminal window using `conda activate nextstrain` and then navigate to the monkeypox repository using `cd monkeypox`. Run the command `nextstrain build --docker --cpus 6 . --configfile config/wa_mpxv/wa_config_hmpxv1.yaml` to run the pipeline.
