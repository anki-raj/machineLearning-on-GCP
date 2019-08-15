# Machine Learning with TensorFlow on Google Cloud Platform

### Table of Contents
1. How Google does Machine Learning
2. Launching into Machine Learning
3. Intro to TensorFlow
4. Feature Engineering
5. Art and Science of Machine Learning

## How Google does Machine Learning

- ML is extensively used in Google photos, youtube and many other apps
- PreTrained model: using speech API or dialogflow to get the work done.
- Building custom model APIs
- personalization of maps is possible with ML:
    -Use of A* algorithm to reach to a destination.
    -recommendation articles of the places you visited.
- Approach to an ML problem
    -Manual data analysis, collecting and analysis of data
- Create an app to read customer emails and determine which department should handle it.
- ML effort Allocation
    - Data collection
    - Infrastructure building
- Path to ML
    - Individual contribution
    - Delegation
    - Digitization
    - Big Data and analytics
    - Machine learning
    
- Making ML inclusive
    - Biases in ML can lead to tilt the direction of learning
    - Evaluation metric - confusion matrix (false positives and false negatives)
    - False negative can be less dangerous in span detection
    - Equatily of opportunity
    - Finding errors in dataset using facets

- Python notebooks in the cloud
    - dataLab
    - VM instances
    - Mutiple zones for apps

- Process earthquake data
    - Create an instance
    - SSH into it and install git
    - clone the earthquake data repo
    - run scripts to visualize the csv file and process it
    - share it to the google storage bucket and to public

- BigQuery
    - work with the entire dataset and not a sample
    - BigQuery to process data at scale and bring it back to in memory structure like pandas.
    - Analyse large airline dataset using BigQuery and cloud Datalab
        - Launch Cloud Datalab
        - Invoke a BigQuery query
        - Create graphs in Datalab
        - commit and push the notebook to git
- ML APIs
    - Vision API -
        . giphy: extract text from image to improve search results
        . Label detection
        . Logo detection
    - Video Intelligence API
        . regionazation
        . label detection
        . shot change detection
    - Speech API
        . Transript voice to text
    - Natural language API
        . Extract entities
        . detect sentiments
        . analyze syntax
        . classify content
- working with labs
    - commands
        . gcloud compute zones list        
        . datalab create <NAME> --zone <ZONENAME>

    





