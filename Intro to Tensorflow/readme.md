What will be discussed
    - Create ML models in Tensorflow
    - Core Tensorflow: Numeric programming library
    - Tendorflow library to solve numeric problems
    - Estimator API for training, evaluating, serving ML models
    - Deploy the model on Google cloud engine

Core Tensorflow (Lazy evaluation programs, graphs, sessions, variables, visualize graph, debugging)
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
