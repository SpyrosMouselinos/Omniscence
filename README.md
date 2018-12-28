# Omniscence

Omniscence is a multipurpose library for Data Analysis and Preprocessing, focused mainly on assisting the data input pipeline of Machine Learning Projects.

# Alpha Version 0.1 is here!
Features:
  - Import csv files into Dataframes
  - Create Raw Data Distribution Reports
  - Perform In-Place Normalization and Filtering
  - Perform Data Correlation Heatmap Analysis
  - Use Bayesian Gaussian Mixture Model for Unsupervised Classification and Data Grouping.

### Installation

Omniscence requires python3,numpy,pandas,seaborn,matplotlib and sklearn to run.

Install all the dependencies from the requirements file in the project.

```sh
$ cd Omniscence
$ pip3 install -r requirements.txt
```
### Usage
```sh
import Omniscence as oms
# Initialization
omni_analyzer = oms(file_dir = The csv file to load, 
                    task = 'classification' / 'regression',
                    input_size = No. of features without the target,
                    target = 'the name of the target feature')
# Load data.
omni_analyzer.load()

# Normalize data (optional).
omni_analyzer.normalize('minmax'/'meanstd')

# Report Data.
omni_analyzer.report()

# Create Kernel Density Estimators and plot data distributions.
omni_analyzer.analyze()

# Plot the inter-correlating feature scores in a heatmap
omni_analyzer.heatmap()

# Perform a BIC score search on the best No. of Clusters and then fit a Bayesian Gaussian Mixture Model on the Data performing Unsupervised Classification.
omni_analyzer.unsupervised_classification()

# Denormalize a dataset based on the normalization metrics of the preprocessed dataset
omni_analyzer.denormalize(dataset_to_denormalize)
```








License
----

Spyros Mouselinos 2018 -MIT
