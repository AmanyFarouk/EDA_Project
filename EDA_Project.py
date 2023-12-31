import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
# read the file in csv format or excel
def load_DataSet(file):
    if file.endswith('.csv'):
        data = pd.read_csv(file)
        return data
    elif file.endswith('.xlsx'):
        data = pd.read_excel(file)
        return data
    else:
        print("error , the file path invalid")
        return 0
    
    
def feature_selection(file):
  pass
# Dimensionality reduction with PCA
def dimensionality_reduction(file):
    pca = PCA()
    reduced_data = pca.fit_transform(file)
    return pd.DataFrame(reduced_data)    

#Handling missing values 
def HandlingMissingValues(file):
    #drop the null values 
    file.dropna(inplace=True)
    return file
#Encoding Categorical Features with get_dummies or one hot encoding
def Encoding(file):
    encoding_file=file.copy()
    categorical_columns=encoding_file.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        encoding_col=pd.get_dummies(encoding_file[col],prefix=col,drop_first=True)
        encoding_file=encoding_file.drop(col,axis=1)
        encoding_file=pd.concat([encoding_file,encoding_col],axis=1)
    return encoding_file

def Scaling(file):
    scaled_file=file.copy()
    numerical_columns=scaled_file.select_dtypes(include=['float','int']).columns
    for col in numerical_columns:
        minVal=scaled_file[col].min()
        maxVal=scaled_file[col].max()
        scaled_file[col]=(scaled_file[col]-minVal/maxVal-minVal)
    return scaled_file
#pre-process the data
def preProcess(file):
    df=HandlingMissingValues(file)
    df=Encoding(df)
    df=Scaling(df)
    return df
#visualization
def visualization(file):
  # to visualize numerical data :(hist , pie)
  # to visualize categorical data : (pie, bar)
   for col in file.columns:
        col2 = str(col)
        if file[col2].dtype == 'object':
            counts = file[col].value_counts()
            plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
            plt.title(f"Pie chart of column '{col2}'")
            plt.show()
        else :
            #numberical features
            plt.hist(file[col])
            plt.title(f"Histogram of column '{col2}'")
            plt.show()
    
       
        
file=input("enter the file : ")
df=load_DataSet(file)
df=preProcess(df)
df=dimensionality_reduction(df)
df=visualization(df)
