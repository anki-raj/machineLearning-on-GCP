### Launching into Machine learning
- Things to cconsider
    . creating datasets
    . Optimization
    . Generalization and sampling
- Learn how to
    . Differentiate between major categories of ML problems
    . Identify why DL is currently popular

- Supervised learning : Give the model labelled examples of what is should learn
    . Two types of problems:
        - Regression - continous value -> predicting the tip amount
            . Logistic is not under classification because it estimates the probabilities of the outcome
            . Reduce the loss -> mean squared value
        - Classification - descrete value -> predicting the gender of the person who tips
            . Reduce the loss -> cross entropy
- History of ML
    . Perceptron
        - computational model of a neuron
    . Neural network
        - Multi-layered
        - activation function -> sigmoid, tanh, relu
    . Decision trees
        - Used for both classification and regression
        - makes a tree with each node having linear classifier of each feature
    . Kernel methods ( Support vector machine)
        - Maximises the margin between 2 classes
        -  Therefore, SVM classifiers aim to maximize the margin between the two support vectors using a hinge loss function compared to logistic regression's minimization of cross-entropy.
        - kernel transformation for non linear models
    . Random Forests
        - Strong learner from many weak learners
        - It is reminiscent of k-fold validation using random holdouts.
        - Instead of taking your entire training set and using that to build one decision tree, you could have a group of decision trees that each get a random subsample of the training data.
    . Modern NN
        - dropout layers
        - reLu
        - CNN
        - Lots of data, generalization, experimenting
- Optimization
    . loss functions, gradients, performance matrix
    . Defining an ML model
        - Parameter-> Changed during model training
            . linear - bias and weight
        - Hyperparameter-> Set before training
    . loss function
        - for regression: Root mean square error
        - for classification: Cross entropy -> Log loss
    . Gradient descent
        - Take a loss functiona and turn it into a search stratergy
        - Learning rate (step size)
        - loss curve
        - hyperparameter tuning - learning rate, batch size
        - loss surface with more than one minima
    . TensorFlow playground
        - input features, hidden layers, batch size, learning rate
    . Performance metrics
        - accuracy, presision, recall

- Generalization and sampling
    . When is the most accurate ML model not the right one to pick?
    . Should perform good in unseen data
    . Assess if the model is overfitting
    . Use the validation set to know if the model has the right fit
    . cross validation for small dataset
    . Sampling/splitting data based on hash
    
    - Creating Repeatable Dataset Splits in BigQuery
        - https://googlecoursera.qwiklabs.com/focuses/35214
        - Comparing the spilt with rand() fnction and a hash function
    - Steps for an ML projet
        - explore a dataset using BigQuery and Datalab
        - sample the dataset and create training, validation, and testing datasets for local development of TensorFlow models
        - create a benchmark to evaluate the performance of ML against
    













