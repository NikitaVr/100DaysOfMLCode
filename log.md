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

### Day 2: 19 July, 2018

**Today's Progress**: Finished fast ai lesson 2 video and went on to lesson 3. Tried improving model and using resnext50 architecture but ran out of memory. Trying different batch sizes did not seem to help but need to look more into that.

**Thoughts:** Look into how to make better memory usage. I think I should be able to run resnext50 on my tier of paperspace, as there should be sufficient RAM and GPU Memory, but need to look into it more. Also thinking about how image recognition could be applied in manufacturing to find deffective parts. It may need to notice quite small subtle changes, may need to have more training of the very early levels of the model for Image Net instead of the usual approach of mostly modifying the final layers.

**Link to work:** [Detailed Log](https://github.com/NikitaVr/100DaysOfMLCode/blob/master/logs/Day2.md)

### Day 3: 20 July, 2018

**Today's Progress**: Slower day today. Mostly studied but also began setting up open ai gym. Got the basic gym working but hard to install the Atari packages on windows, and to setup gym-retro.

**Thoughts:** Thinking of switching to Linux based system. Seems a lot of this stuff is made with Linux in mind first.

**Link to work:** [Commit](https://github.com/NikitaVr/100DaysOfMLCode/commit/ea3909e415f3bfc8bf4ffa1fa04d4a356abc86b9)

### Day 4: 21 July, 2018

**Today's Progress**: Going through Lesson 3 of course.fast.ai . Important Note: When setting precompute=True to slightly speed up the training, the data augmentation will not work ( since it uses certain precomputed values). So if you want to use data augmentation, then DO NOT set precompute=True. Also when working with images similar to ImageNet, note the learn.bn_freeze(True)

**Thoughts:** Try out the quick image classifications for many different applications.

**Link to work:** [Lesson](http://course.fast.ai/lessons/lesson3.html), [Quick To Write Classification With Great Results](https://github.com/NikitaVr/100DaysOfMLCode/blob/master/fastai/StateOfTheArtImageClassification.JPG)

### Day 5: 22 July, 2018

**Today's Progress**: Going through more of fast.ai on Lesson 3. Found this interesting proof that a neural network can compute any function: http://neuralnetworksanddeeplearning.com/chap4.html

**Thoughts:** Need to search for a database of camouflage vs no camouflage. Interested in making an image classifier that can detect camo.

**Link to work:** [Reading](http://neuralnetworksanddeeplearning.com/chap4.html)

### Day 6: 23 July, 2018

**Today's Progress**: Finishing up lesson 3 of course.fast.ai . Important Note: Generally do not unfreeze righ away, as the last layer begins randomly initialized, but previous layers are not random and are already trained using ImageNet, which is ussually better than random. So first train the last layers only, for a bit, to get them better than random, then you can unfreeze and train the whole model with differential learning rates.

**Thoughts:** Need to look for sources of multi class labeled data to try these methods out more, there is the kaggle planet dataset https://www.kaggle.com/c/planet-understanding-the-amazon-from-space but would be nice to find more.

**Link to work:** [Fast AI Lesson 3](http://course.fast.ai/lessons/lesson3.html)

### Day 7: 24 July, 2018

**Today's Progress**: Slower day today but at least went through more of the fast ai content. Going through lesson 4 now.

**Thoughts:** Try and apply the structured data knowledge to some of the kaggle competitions.

**Link to work:** [Fast AI Lesson 4](http://course.fast.ai/lessons/lesson4.html)

### Day 8: 25 July, 2018

**Today's Progress**: Continuing with course.fast.ai lesson 4. Tip: use `Dropout` in convolutional networks to decrease overfitting. ex. p=0.5 will mean we throw out each activation with a 50% chance.

sometimes you may want to treat things like Year as Categorical rather than continuous

Categorical Data has to be treated as Categorical in the model

but Continuous Data can be treated as Continuous or Categorical on the model depending on what you think better models the relationship

**Thoughts:** Put together a document of really useful tips

**Link to work:** [Fast AI Lesson 4](http://course.fast.ai/lessons/lesson4.html)

### Day 9: 26 July, 2018

**Today's Progress**: More Progress with course.fast.ai lesson 4. Also went over Siraj Raval's video on Loss Functions https://www.youtube.com/watch?v=IVVVjBSk9N0

**Thoughts:** Much Tired, can't think

**Link to work:** [Fast AI Lesson 4](http://course.fast.ai/lessons/lesson4.html), [Loss Functions Video](https://www.youtube.com/watch?v=IVVVjBSk9N0)






