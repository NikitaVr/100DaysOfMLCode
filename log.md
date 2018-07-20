# 100 Days Of ML Code - Log

## Use this as a base template. Create your own repository on GitHub and start logging your work daily!

### Day 0: 17 July, 2018
##### (delete me or comment me out)

**Today's Progress**: Setting up PaperSpace with Kaggle tool and getting dataset ready

**Thoughts:** Create a more detailed log with more steps. Keep a location for useful scripts, also keep track of lessons learned.

**Link to work:** [More Detailed Log](https://github.com/NikitaVr/100DaysOfMLCode/blob/master/logs/Day0.md)

### Day 1: 18 July, 2018

**Today's Progress**: Looked through the first 2 lessons of course.fast.ao again. Trained fast ai image classifier with unfrozen layers in the net on https://www.kaggle.com/c/plant-seedlings-classification . Got about 93.3% accuracy. 

**Thoughts:** Can probably tune it more and use different sizes to further improve accuracy. This library definitely makes it easy to get good results very fast.

**Link to work:** [Commit](https://github.com/NikitaVr/100DaysOfMLCode/commit/a5458822952a475c1503d3345ab65f3031bf901e), [Commit of Readable Python Code](https://github.com/NikitaVr/100DaysOfMLCode/commit/db206e77ae9ade436ab23f84efc69b7b02f95db9), maybe a good idea to also commit the trained saved model.

### Day 1: 18 July, 2018

**Today's Progress**: Finished fast ai lesson 2 video and went on to lesson 3. Tried improving model and using resnext50 architecture but ran out of memory. Trying different batch sizes did not seem to help but need to look more into that.

**Thoughts:** Look into how to make better memory usage. I think I should be able to run resnext50 on my tier of paperspace, as there should be sufficient RAM and GPU Memory, but need to look into it more. Also thinking about how image recognition could be applied in manufacturing to find deffective parts. It may need to notice quite small subtle changes, may need to have more training of the very early levels of the model for Image Net instead of the usual approach of mostly modifying the final layers.

**Link to work:** [Detailed Log](https://github.com/NikitaVr/100DaysOfMLCode/blob/master/logs/Day2.md)
