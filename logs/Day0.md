Looking into this kaggle sample competition to get an image dataset: https://www.kaggle.com/c/plant-seedlings-classification/data

Generate Kaggle key at https://www.kaggle.com/nikitavr/account and download the `kaggle.json` file with the key inside

then from my personal computer to copy over to paperspace: 

`scp kaggle.json paperspace@paperspaceMachineIP:~/.kaggle/kaggle.json` 

Then on Paperspace inside `~/.kaggle/` run

```
chmod 600 /home/paperspace/.kaggle/kaggle.json
```

That ensures other users cannot read your api key file.

Then ran `kaggle competitions download -c plant-seedlings-classification` to get the data for this sample competition: https://www.kaggle.com/c/plant-seedlings-classification/data

The default storage location is `~/.kaggle/` so the files for this competition are in `~/.kaggle/competitions/plant-seedlings-classification`

cd into that directory then run

```
unzip sample_submission.csv.zip
```

```
unzip train.zip
```

```
unzip test.zip
```
