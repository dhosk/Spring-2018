# Final Project

The final project is an opportunity to use the ideas from this course for exploring interesting data science problems.
You will work on the project in a group of four. 

## Logistics

__Project group__: Please work in a group of four. If you cannot find a group of four, I will help in merging smaller groups to make groups of four. If have reasons for prefering a different group structure, please talk to me.

__Progress report (Due May 28 at 10 pm)__: A one page outline naming your group members, proposed data set, and project outline.

__Report (Due June 14 at 10 pm)__: You need to provide a Jupyter notebook report of your project. You may use multiple notebooks to separate material into parts (also, in order to avoid any large notebook issues). If your project is not accepted by GauchoSpace due to space limitation (100 MB), prepare a shared zip-archive of complete set of files needed to run your project on Box: https://ucsb.account.box.com/login. Everyone at UCSB has an unlimited storage using this service. Indicate the URL location of your shared zip-archive on your Jupyter notebooks on GauchoSpace, and indicate the shared link on your notebook. Note that any file that needs to be downloaded using API keys, etc, need to be pickled into a separate file(s) and made available in the zipped-archive.

__Sections Friday (June 1)__: Upcoming sections this Friday will be used to help you work on your projects. Discuss with your group to ask questions. I will post sign-up form to make better use of times.

__Presentation__: Your group will make a 20-minute presentation on one of these dates:
- June 4 (lecture time): 2-3 groups
- June 6 (lecture time): 2-3 groups
- June 8 (discussion times): 3-4 groups = up to 2 groups x 2 sections
- June 14 (Final exam time: 12-3 pm): up to 6 groups

## Possible Project Ideas

### Basketball

NBA website provides many different types of data. Some project ideas are:

Exploring feature engineering for basketball data:   
NBA website [glossary](http://stats.nba.com/help/glossary/) offers many engineered features. For example, search for `DEFRTG`. Are these useful for discrimination or prediction?
What features seem to discriminate a class label? e.g., wins vs. losses, home game vs. away game, defensive player vs. offensive player, etc.
Can you design your useful features? Can you show that your features are useful qualitatively? quantitatively?
You also build classification models using your new features
  
### Portfolio Optimization

Minimum variance portfolio selection problem was discussed in a naive setting to illustrate the theory. 
Using the theory in practice, however, requires a more sophisticated approach. 
For example, since real financial market is not stationary, portfolio weights needs to be recomputed periodically (called rebalancing).
Costs associated with trades need to be included in the calculation: borrowing cost, transaction cost, etc.
For reference, you can refer to Appendix J in [this paper](https://arxiv.org/abs/1307.5381) for details. 
A pre-built package that powers a quantitative trading strategy site is [Quantopian](https://www.quantopian.com/home).
They release a package that powers [their site](http://www.zipline.io/). The package takes care of the details. 
Refer to some examples [here](http://www.zipline.io/beginner-tutorial.html).  
A project idea is to tackle minimum variance portfolio investment strategy with Zipline.

### Health data 

[NHANES dataset](https://www.cdc.gov/nchs/nhanes/nhanes_questionnaires.htm) is a vast resource of open health datasets.
You can extend the health data module for your project. Many papers have been published using NHANES dataset, so web search will give you some ideas. You can extend the ideas from health module in ways you think are interesting.

### Yelp 

In later part of the course, we will use Yelp reviews to work with text data. 
You can consider doing a project using text data. Python has a wealth of packages for working with text data. 
Even with simple tools, one can do a lot with text. Here is the link to a good [online resource](https://ucsb-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=01UCSB_ALMA51279011670003776&context=L&vid=UCSB&search_scope=default_scope&tab=default_tab&lang=en_US).

### Your project

You can work on your a project of your choosing. Please discuss your idea with me, so that I can help you get started and make sure the scope is reasonable.

### Presentation Schedule

|                                | Group 1                                              | Group 2                                                        | Group 3                                                         | Group 4                                            | Group 5 | Group 6 |
|--------------------------------|------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------|---------|---------|
| Wednesday, June 6, 11-12:15 pm | Josh Bang, Ashley Radford, Emeric Szaboky, Lash Tan  | Ben Ku, Xining Li, Mi Yu, Zhipu Zhou                           | Maria Carmen, Jesus Fernandez, Tyler Nicholson, Rebecca Samouha |                                                    |         |         |
| Friday, June 8, 9-9:50 am      | Sam ONeill, Aaron Plesset, Xiaoxiong Xu, Xiaoyue Zhu | Junli Chen, Mingxi Chen, Zhaoming Hua, Syen Yang Lu            |                                                                 |                                                    |         |         |
| Friday, June 8, 12-12:50 pm    | Guoqiang Chen, Fay Wu, Qi Wang                       | Andy Vu Hoang, Shon Inouye, J Steven Raquel, Andrew Zhang      |                                                                 |                                                    |         |         |
| Thursday, June 14, 12-3 pm     | Benjamin Fox, Meet Gala, Alex Gordee                 | Kendall Brown, Lauren Gripenstraw, Rahul Narula, Jory Oberlies | Amy Huynh, Eri Martinez, Brian Ordonez, Don Zheng               | Wenlu Gou, Nhan Huynh,  Zach Terner, Laura Urbisci | David Hoskins | (empty) |
