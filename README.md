# CN_Project

# Here in this project, I tried to Optimise the Traffic at the Data Center using Machine Learning. For This I have used K-Mean Clustering, Random forest Regression, A method of Reinforcement Learning i.e., Thompson Sampling/.

# First, we have searched for the dataset for a datacenter and finally got one, which describes the following:
#•	It is a routing table from one PARTICULAR IP to another IP via data center having 10 routers.
#•	It has the 10,000 packet routing history of that particular transaction.

#Now, We have given a priority for each packet and sorted them based on the priority by using a Priority Queue. We
#sent the resulting dataset to our Central System that decides
#whether it is a small data flow or large data flow on it size of packet. Here, we used sorting technique to do so namely merge sort. Sorted it in ascending order and given the preference to shorter data flow.
#This is all done in background and made in the form of CSV files and used in the code.

# With This we have achieved the efficiency of 25% for long flows, and nearly 69% to the short Data Flows.

# Future work of turning this machine learning model into deep learning model is in progress.
