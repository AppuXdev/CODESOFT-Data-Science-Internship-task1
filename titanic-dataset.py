{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f3245730",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import numpy as np\n",
    "df=pd.read_csv(\"Titanic-Dataset.csv\")\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2d3c9082",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 12 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  891 non-null    int64  \n",
      " 1   Survived     891 non-null    int64  \n",
      " 2   Pclass       891 non-null    int64  \n",
      " 3   Name         891 non-null    object \n",
      " 4   Sex          891 non-null    object \n",
      " 5   Age          714 non-null    float64\n",
      " 6   SibSp        891 non-null    int64  \n",
      " 7   Parch        891 non-null    int64  \n",
      " 8   Ticket       891 non-null    object \n",
      " 9   Fare         891 non-null    float64\n",
      " 10  Cabin        204 non-null    object \n",
      " 11  Embarked     889 non-null    object \n",
      "dtypes: float64(2), int64(5), object(5)\n",
      "memory usage: 83.7+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "dcac83be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      0\n",
       "Survived         0\n",
       "Pclass           0\n",
       "Name             0\n",
       "Sex              0\n",
       "Age            177\n",
       "SibSp            0\n",
       "Parch            0\n",
       "Ticket           0\n",
       "Fare             0\n",
       "Cabin          687\n",
       "Embarked         2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c52a2757",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.3838383838383838"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Survived'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f7724054",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Survived</th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sex</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>female</th>\n",
       "      <td>81</td>\n",
       "      <td>233</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>male</th>\n",
       "      <td>468</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Survived    0    1\n",
       "Sex               \n",
       "female     81  233\n",
       "male      468  109"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(df['Sex'],df['Survived'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "da95b6d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "First 5 rows:\n",
      "   PassengerId  Survived  Pclass  \\\n",
      "0            1         0       3   \n",
      "1            2         1       1   \n",
      "2            3         1       3   \n",
      "3            4         1       1   \n",
      "4            5         0       3   \n",
      "\n",
      "                                                Name     Sex   Age  SibSp  \\\n",
      "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
      "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
      "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
      "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
      "4                           Allen, Mr. William Henry    male  35.0      0   \n",
      "\n",
      "   Parch            Ticket     Fare Cabin Embarked  \n",
      "0      0         A/5 21171   7.2500   NaN        S  \n",
      "1      0          PC 17599  71.2833   C85        C  \n",
      "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
      "3      0            113803  53.1000  C123        S  \n",
      "4      0            373450   8.0500   NaN        S  \n",
      "\n",
      "Info about coulmns:\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 12 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  891 non-null    int64  \n",
      " 1   Survived     891 non-null    int64  \n",
      " 2   Pclass       891 non-null    int64  \n",
      " 3   Name         891 non-null    object \n",
      " 4   Sex          891 non-null    object \n",
      " 5   Age          714 non-null    float64\n",
      " 6   SibSp        891 non-null    int64  \n",
      " 7   Parch        891 non-null    int64  \n",
      " 8   Ticket       891 non-null    object \n",
      " 9   Fare         891 non-null    float64\n",
      " 10  Cabin        204 non-null    object \n",
      " 11  Embarked     889 non-null    object \n",
      "dtypes: float64(2), int64(5), object(5)\n",
      "memory usage: 83.7+ KB\n",
      "None\n",
      "\n",
      "Missing values in each column:\n",
      "PassengerId      0\n",
      "Survived         0\n",
      "Pclass           0\n",
      "Name             0\n",
      "Sex              0\n",
      "Age            177\n",
      "SibSp            0\n",
      "Parch            0\n",
      "Ticket           0\n",
      "Fare             0\n",
      "Cabin          687\n",
      "Embarked         2\n",
      "dtype: int64\n",
      "\n",
      "Overall survival rate\n",
      "0.3838383838383838\n"
     ]
    }
   ],
   "source": [
    "# loading data\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "df=pd.read_csv(\"Titanic-dataset.csv\")\n",
    "print(\"\\nFirst 5 rows:\")\n",
    "print(df.head())\n",
    "print(\"\\nInfo about coulmns:\")\n",
    "print(df.info())\n",
    "print(\"\\nMissing values in each column:\")\n",
    "print(df.isnull().sum())\n",
    "print(\"\\nOverall survival rate\")\n",
    "print(df['Survived'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "71a1a343",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing values after cleaning:\n",
      "Survived      0\n",
      "Pclass        0\n",
      "Sex           0\n",
      "Age           0\n",
      "SibSp         0\n",
      "Parch         0\n",
      "Fare          0\n",
      "Embarked      0\n",
      "FamilySize    0\n",
      "IsAlone       0\n",
      "Title         0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#cleaning data\n",
    "df_clean=df.copy()\n",
    "df_clean['Age']=df_clean.groupby(['Pclass','Sex'])['Age'].transform(lambda x:x.fillna(x.median()))\n",
    "df_clean['Embarked'].fillna(df_clean['Embarked'].mode()[0],inplace=True)\n",
    "df_clean['FamilySize']=df_clean['SibSp']+df_clean['Parch']+1\n",
    "df_clean['IsAlone']=np.where(df_clean['FamilySize']==1,1,0)\n",
    "df_clean['Title']=df['Name'].str.extract('([A-Za-z]+)\\.',expand=False)\n",
    "df_clean['Title']=df_clean['Title'].replace(['Lady','Countness','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona'],'Rare')\n",
    "df_clean['Title']=df_clean['Title'].replace('Mlle','Miss')\n",
    "df_clean['Title']=df_clean['Title'].replace('Ms','Miss')\n",
    "df_clean['Title']=df_clean['Title'].replace('Mme','Mrs')\n",
    "df_clean.drop(['Cabin','Ticket','PassengerId','Name'],axis=1,inplace=True)\n",
    "print(\"Missing values after cleaning:\")\n",
    "print(df_clean.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "fd828cb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'IsAlone', 'Embarked_Q', 'Embarked_S', 'Title_Master', 'Title_Miss', 'Title_Mr', 'Title_Mrs', 'Title_Rare']\n",
      "   Survived  Pclass  Sex   Age  SibSp  Parch  Fare  FamilySize  IsAlone  \\\n",
      "0         0       3  NaN  22.0      1      0  7.25           2        0   \n",
      "\n",
      "   Embarked_Q  Embarked_S  Title_Master  Title_Miss  Title_Mr  Title_Mrs  \\\n",
      "0           0           1             0           0         1          0   \n",
      "\n",
      "   Title_Rare  \n",
      "0           0  \n"
     ]
    }
   ],
   "source": [
    "print(df_clean.columns.tolist())\n",
    "print(df_clean.head(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "19f40590",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)]\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(sys.version)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ea6a7a29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sys\n",
    "import subprocess\n",
    "subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn==1.0.2'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e191fed4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "First 5 rows:\n",
      "   PassengerId  Survived  Pclass  \\\n",
      "0            1         0       3   \n",
      "1            2         1       1   \n",
      "2            3         1       3   \n",
      "3            4         1       1   \n",
      "4            5         0       3   \n",
      "\n",
      "                                                Name     Sex   Age  SibSp  \\\n",
      "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
      "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
      "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
      "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
      "4                           Allen, Mr. William Henry    male  35.0      0   \n",
      "\n",
      "   Parch            Ticket     Fare Cabin Embarked  \n",
      "0      0         A/5 21171   7.2500   NaN        S  \n",
      "1      0          PC 17599  71.2833   C85        C  \n",
      "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
      "3      0            113803  53.1000  C123        S  \n",
      "4      0            373450   8.0500   NaN        S  \n",
      "\n",
      "Info about coulmns:\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 12 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   PassengerId  891 non-null    int64  \n",
      " 1   Survived     891 non-null    int64  \n",
      " 2   Pclass       891 non-null    int64  \n",
      " 3   Name         891 non-null    object \n",
      " 4   Sex          891 non-null    object \n",
      " 5   Age          714 non-null    float64\n",
      " 6   SibSp        891 non-null    int64  \n",
      " 7   Parch        891 non-null    int64  \n",
      " 8   Ticket       891 non-null    object \n",
      " 9   Fare         891 non-null    float64\n",
      " 10  Cabin        204 non-null    object \n",
      " 11  Embarked     889 non-null    object \n",
      "dtypes: float64(2), int64(5), object(5)\n",
      "memory usage: 83.7+ KB\n",
      "None\n",
      "\n",
      "Missing values in each column:\n",
      "PassengerId      0\n",
      "Survived         0\n",
      "Pclass           0\n",
      "Name             0\n",
      "Sex              0\n",
      "Age            177\n",
      "SibSp            0\n",
      "Parch            0\n",
      "Ticket           0\n",
      "Fare             0\n",
      "Cabin          687\n",
      "Embarked         2\n",
      "dtype: int64\n",
      "\n",
      "Overall survival rate\n",
      "0.3838383838383838\n",
      "Missing values after cleaning:\n",
      "Survived      0\n",
      "Pclass        0\n",
      "Sex           0\n",
      "Age           0\n",
      "SibSp         0\n",
      "Parch         0\n",
      "Fare          0\n",
      "Embarked      0\n",
      "FamilySize    0\n",
      "IsAlone       0\n",
      "Title         0\n",
      "dtype: int64\n",
      "Model Accuracy: 0.8212290502793296\n",
      "\n",
      "Detailed Report:\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.85      0.85      0.85       105\n",
      "           1       0.78      0.78      0.78        74\n",
      "\n",
      "    accuracy                           0.82       179\n",
      "   macro avg       0.82      0.82      0.82       179\n",
      "weighted avg       0.82      0.82      0.82       179\n",
      "\n",
      "\n",
      "Confusion Matrix:\n",
      "[[89 16]\n",
      " [16 58]]\n"
     ]
    }
   ],
   "source": [
    "# loading data\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "df=pd.read_csv(\"Titanic-dataset.csv\")\n",
    "print(\"\\nFirst 5 rows:\")\n",
    "print(df.head())\n",
    "print(\"\\nInfo about coulmns:\")\n",
    "print(df.info())\n",
    "print(\"\\nMissing values in each column:\")\n",
    "print(df.isnull().sum())\n",
    "print(\"\\nOverall survival rate\")\n",
    "print(df['Survived'].mean())\n",
    "#cleaning data\n",
    "df_clean=df.copy()\n",
    "df_clean['Age']=df_clean.groupby(['Pclass','Sex'])['Age'].transform(lambda x:x.fillna(x.median()))\n",
    "df_clean['Embarked'].fillna(df_clean['Embarked'].mode()[0],inplace=True)\n",
    "df_clean['FamilySize']=df_clean['SibSp']+df_clean['Parch']+1\n",
    "df_clean['IsAlone']=np.where(df_clean['FamilySize']==1,1,0)\n",
    "df_clean['Title']=df['Name'].str.extract('([A-Za-z]+)\\.',expand=False)\n",
    "df_clean['Title']=df_clean['Title'].replace(['Lady','Countness','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona'],'Rare')\n",
    "df_clean['Title']=df_clean['Title'].replace('Mlle','Miss')\n",
    "df_clean['Title']=df_clean['Title'].replace('Ms','Miss')\n",
    "df_clean['Title']=df_clean['Title'].replace('Mme','Mrs')\n",
    "df_clean.drop(['Cabin','Ticket','PassengerId','Name'],axis=1,inplace=True)\n",
    "print(\"Missing values after cleaning:\")\n",
    "print(df_clean.isnull().sum())\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score,classification_report,confusion_matrix\n",
    "df_clean['Sex']=df_clean['Sex'].map({'male':0,'female':1})\n",
    "df_clean=pd.get_dummies(df_clean,columns=['Embarked','Title'],drop_first=True)\n",
    "y=df_clean['Survived']\n",
    "X=df_clean.drop('Survived',axis=1)\n",
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\n",
    "model=LogisticRegression(max_iter=1000)\n",
    "model.fit(X_train,y_train)\n",
    "predictions=model.predict(X_test)\n",
    "print(\"Model Accuracy:\",accuracy_score(y_test,predictions))\n",
    "print(\"\\nDetailed Report:\")\n",
    "print(classification_report(y_test,predictions))\n",
    "print(\"\\nConfusion Matrix:\")\n",
    "print(confusion_matrix(y_test,predictions))\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
