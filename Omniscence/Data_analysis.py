import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.mixture import BayesianGaussianMixture as BGM

class OmniAnalyzer:
    def __init__(self,file_dir,task,input_size,target):
        self.__file_dir__ = file_dir
        self.__task__ = task
        self.__input_size__ = input_size
        self.__target__ = target
        self.__data__ = pd.DataFrame()
        self.__data_numeric__ = pd.DataFrame()
        self.__numeric_features__ = []
        self.__categorical_features__ = []
        self.__categorical_dict__ = {}
        self.__stats__ = pd.DataFrame()

        
    def load(self):
        self.__data__ = pd.read_csv(self.__file_dir__)
        self.__numeric_features__ = [key for key in dict(self.__data__.dtypes) if dict(self.__data__.dtypes)[key]
                in ['float64','float32','int32','int64']]
        self.__categorical_features__ = [key for key in dict(self.__data__.dtypes)
                     if dict(self.__data__.dtypes)[key] in ['object'] ]
        for feature in self.__categorical_features__:
            uniques = self.__data__[feature].unique()
            count = 0 
            for unique in uniques:
                self.__categorical_dict__.update({unique:count})
                count += 1
        for feature in self.__data__:
            if feature in self.__numeric_features__:
                self.__data_numeric__[feature] = self.__data__[feature]
            else:
                self.__data_numeric__['enum_'+feature]=self.__data__[feature].map(self.__categorical_dict__)
        self.__stats__ = self.__data__.describe()
    
    def report(self):
        try:
            return self.__data_numeric__.describe()
        except:
            try:
                return self.__data__.describe()
            except:
                pass
            pass
    
    def normalize(self,method):
        if method == 'minmax':
            self.__normalization__ = 'minmax'
            for feature in self.__stats__:
                _min_ = self.__stats__[feature]['min']
                _max_ = self.__stats__[feature]['max']
                _range_ = _max_ - _min_
                self.__data_numeric__[feature]= (self.__data_numeric__[feature] - _min_) / (_range_)
        elif method == 'meanstd':
            self.__normalization__ = 'meanstd'
            for feature in self.__stats__:
                _mean_ = self.__stats__[feature]['mean']
                _std_ = self.__stats__[feature]['std']
                self.__data_numeric__[feature]= (self.__data_numeric__[feature] - _mean_) / (_std_)
        else:
            raise ValueError('minmax or meanstd are the normalization types')
            
    def denormalize(self,new_data):
        if self.__normalization__ == 'minmax' :
            for feature in self.__stats__:
                _min_ = self.__stats__[feature]['min']
                _max_ = self.__stats__[feature]['max']
                _range_ = _max_ - _min_
                new_data[feature]= (new_data[feature] * (_range_)) + _min_
        elif self.__normalization__ == 'meanstd' :
            for feature in self.__stats__:
                _mean_ = self.__stats__[feature]['mean']
                _std_ = self.__stats__[feature]['std']
                new_data[feature]= (new_data[feature] * (_std_)) + _mean_

    def analyze(self):
        sns.pairplot(data=self.__data__, diag_kind="kde",hue=self.__target__, palette="husl")
    
    def heatmap(self):
        corr = self.__data_numeric__.corr()
        fig, ax = plt.subplots(figsize=(10, 10))
        colormap = sns.diverging_palette(220, 10, as_cmap=True)
        dropSelf = np.zeros_like(corr)
        dropSelf[np.triu_indices_from(dropSelf)] = True
        colormap = sns.diverging_palette(220, 10, as_cmap=True)
        sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f", mask=dropSelf)
        plt.xticks(range(len(corr.columns)), corr.columns);
        plt.yticks(range(len(corr.columns)), corr.columns)
        plt.show()
        
        
    def unsupervised_classification(self):
        self.__labels__ = self.__data_numeric__.pop('enum_'+str(self.__target__))

        n_components = np.arange(1, len(self.__labels__.unique())+2)
        models = [BGM(n, covariance_type='full', random_state=1453).fit(self.__data_numeric__.values)
          for n in n_components]
        bics=[]
        for model in models:
            bic = (-2 * model.score(self.__data_numeric__.values) * self.__data_numeric__.values.shape[0] + model.n_components * np.log(self.__data_numeric__.values.shape[0]))
            bics.append(bic)
        plt.figure()
        plt.plot(n_components, bics)
        plt.xlabel('n_components')
        plt.ylabel('BIC Score')
        plt.show()
        plt.close()
        self.__best_n__ = n_components[np.argmin(bics)]
        print('Convergence complete!')
        estimator = BGM(n_components=self.__best_n__)
        estimator.fit(self.__data_numeric__.values)
        self.__data_numeric__['cluster'] = estimator.predict(self.__data_numeric__)
        sns.pairplot(self.__data_numeric__, diag_kind="kde", hue='cluster', vars=[index for index in self.__data_numeric__ if index != 'cluster'],palette="husl")
        self.__data_numeric__['labels'] = self.__labels__



