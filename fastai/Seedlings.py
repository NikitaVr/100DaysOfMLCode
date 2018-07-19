
# coding: utf-8

# In[3]:


# Put these at the top of every notebook, to get automatic reloading and inline plotting
get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


# This file contains all the main external libs we'll use
from fastai.imports import *


# In[5]:


from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *


# In[20]:


import  os  as  os
from os  import  *
import  random


# In[8]:


PATH = "/home/paperspace/.kaggle/competitions/plant-seedlings-classification/"
sz=224


# In[9]:


get_ipython().system('ls {PATH}')


# In[10]:


torch.cuda.is_available()


# In[11]:


torch.backends.cudnn.enabled


# In[12]:


os.listdir(PATH)


# In[13]:


os.listdir(f'{PATH}train/')


# In[14]:


files = os.listdir(f'{PATH}train/Cleavers')[:5]
files


# In[15]:


img = plt.imread(f'{PATH}train/Cleavers/{files[0]}')
plt.imshow(img);


# In[16]:


img.shape


# In[26]:


def copy_to_valid(chosen_files,class_dir):
    for i in range (len(chosen_files)):
        get_ipython().system('mv "{PATH}/train/{class_dir}/{chosen_files[i]}" "{PATH}/valid/{class_dir}"')


# In[27]:


classes = get_ipython().getoutput('ls {PATH}/train')


# In[28]:


for classname in classes:
    os.makedirs(f'{PATH}/valid/{classname}', exist_ok=True)
    list_of_files = get_ipython().getoutput('ls "{PATH}/train/{classname}"')
    random.shuffle(list_of_files)
    n_files_moved=int(len(list_of_files)*0.2)
    selected_files = [list_of_files[m] for m in range(n_files_moved)]
    copy_to_valid(selected_files,classname)


# In[24]:


#img[:4,:4]


# In[33]:


arch=resnet34
data = ImageClassifierData.from_paths(PATH, tfms=tfms_from_model(arch, sz))
learn = ConvLearner.pretrained(arch, data, precompute=True)
learn.fit(0.01, 2)


# In[34]:


# This is the label for a val data
data.val_y


# In[35]:


# from here we know that 'cats' is label 0 and 'dogs' is label 1.
data.classes


# In[36]:


# this gives prediction for validation set. Predictions are in log scale
log_preds = learn.predict()
log_preds.shape


# In[32]:


log_preds[:10]


# In[37]:


learn = ConvLearner.pretrained(arch, data, precompute=True)


# In[38]:


lrf=learn.lr_find()


# In[39]:


learn.sched.plot_lr()


# In[40]:


learn.sched.plot()


# In[43]:


# Using transforms_top_down here as photos are taken from above
tfms = tfms_from_model(resnet34, sz, aug_tfms=transforms_top_down, max_zoom=1.1)


# In[42]:


def get_augs():
    data = ImageClassifierData.from_paths(PATH, bs=2, tfms=tfms, num_workers=1)
    x,_ = next(iter(data.aug_dl))
    return data.trn_ds.denorm(x)[1]


# In[44]:


ims = np.stack([get_augs() for i in range(6)])


# In[45]:


plots(ims, rows=2)


# In[46]:


data = ImageClassifierData.from_paths(PATH, tfms=tfms)
learn = ConvLearner.pretrained(arch, data, precompute=True)


# In[47]:


learn.fit(1e-2, 1)


# In[48]:


learn.precompute=False


# In[50]:


learn.fit(1e-2, 6, cycle_len=1)


# In[51]:


learn.save('224_lastlayer')


# In[52]:


learn.load('224_lastlayer')


# In[53]:




learn.unfreeze()


# In[54]:


lr=np.array([1e-4,1e-3,1e-2])


# In[56]:


learn.fit(lr, 3, cycle_len=1, cycle_mult=2)


# In[57]:


learn.save('224_all')


# In[58]:


learn.load('224_all')


# In[60]:


log_preds,y = learn.TTA()
probs = np.mean(np.exp(log_preds),0)


# In[61]:


# Confusion Matrix
preds = np.argmax(probs, axis=1)
probs = probs[:,1]


# In[62]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y, preds)


# In[64]:


plot_confusion_matrix(cm, data.classes)

