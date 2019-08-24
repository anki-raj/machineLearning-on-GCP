### What will be discussed
    - Create ML models in Tensorflow
    - Core Tensorflow: Numeric programming library
    - Tendorflow library to solve numeric problems
    - Estimator API for training, evaluating, serving ML models
    - Deploy the model on Google cloud engine

### Core Tensorflow (Lazy evaluation programs, graphs, sessions, variables, visualize graph, debugging)
    - TensorFlow is an open source, high performance, library for numerical computation.
        . Eg To solve partial differential equations
    - Directed Acyclic graph: Connects each node which represent mathematical operation
    - Tensor is an N-dimentional array of data
    - DAC is important for it's portability nature
        . Program is written in python and executed to Tensorflow execution engine (written in c++)
    - Train the model on a powerful device and take the trained model and put in to a device.
        . Using Tensorflow lite to get the trained models to the phone, raspberry etc.
    - TensorFlow API Hierarchy
        . tf.estimator (high level)
        . tf.layers, tf.metrics, tf.losses (to build custom NN models)
        . Core TF (python)
        . Core TF (C++)
        . CPU, GPU, TPU..
    - Lazy evalution
        . Build the DAG and then evalute it using Sessions
        . You need to run the graph to get the results
    - Eager mode to evalute the result immediately
    - Visualize the graph
        . tf.summary.FileWriter
    - tensors, variables
        . A variable is a tensor whose value is initialized and then the value gets changed as a program runs.
        . Placeholder is a container which feeds in a value to the graph at runtime.
    - LAB (Build a graph, run, feed values, finding area of triangle using TF)

### Estimator API
    - Learn how to
        . Create Production ready ML models
        . Train on large Datasets that do not fit in memory
        . Monitor tarining metrics in tensorboard
    - High level API for production ready ML models
        . Quick model
        . checkpointing
        . out-of-memory datasets
        . train, eval, monitor
        . distributed learning
    - Syntax
        - tf.estimator.Estimator.
            (Pre-made estimator)
            LinearRegression
            DNNRegressor ...
        - tf.feature_column (shape that the model can understand)
        - model.train(input,steps=100)
        - model.predict(predict_input_func)
    - Checkpoints
        . To save the trained model in a folder which can be used later
        . tf.estimator.LinearRegression(featcols, './model_trained')
    - Lab Estimator API
        . Read .csv data into a Pandas dataframe
        . Implement a Linear Regression model in TensorFlow
        . Train the model
        . Evaluate the model
        . Predict with the model
        . Repeat with a Deep Neural Network model in TensorFlow
    - Dataset API
        . They generate input functions for Estimators.
        . tf.data.Dataset 
            - textLineDataset   
            - TFRecordDataset
            - FixedlengthRecordDataset
        . TF creates a graph after creating a model. Dataset is useful to use batches at a time to prevent saturation of the memory.
        . input fuunctions return TF nodes and not data
    
        
