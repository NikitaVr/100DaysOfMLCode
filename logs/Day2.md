Mostly was going through more of the fast ai lessons, finished lesson 2 and starting lesson 3.

Tried to improve Seedling classifier.

Tried using resnext50 architecture, but found it was not initially setup in the  fast ai repo.

Found I had to get it using `wget http://files.fast.ai/models/weights.tgz`

Then `tar zxvf weights.tgz` to unpack it in a `weights` dir in the current directory

You can also run `tar zxvf weights.tgz -C /path/to/different/dir` to specify where you want it unpacked to.

Ended up running out of memory, need to look more into that as I think I have sufficient resources. Different batch sizes did not seem to help but need to look more into that and other possible fixes.

Read a little bit about openai gym and want to experiment with that too but still make progres on fast ai too.
