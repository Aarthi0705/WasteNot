{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "85c6f524",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split, cross_val_score\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.pipeline import Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "78fdf0a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(r\"C:\\Users\\91738\\Downloads\\VIT Downloads\\donor_data2.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "a82e823c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.fillna(0, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "02ddb884",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data[['previous_donations', 'business_type', 'location']]\n",
    "y = data['donated']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "313eec65",
   "metadata": {},
   "outputs": [],
   "source": [
    "preprocessor = ColumnTransformer(\n",
    "    transformers=[\n",
    "        ('cat', OneHotEncoder(), ['business_type', 'location'])\n",
    "    ],\n",
    "    remainder='passthrough'  # Leave other columns unchanged\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "856a4467",
   "metadata": {},
   "outputs": [],
   "source": [
    "model_pipeline = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor),\n",
    "    ('classifier', LogisticRegression())\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "49194af2",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "324c7da8",
   "metadata": {},
   "outputs": [],
   "source": [
    "cross_val_scores = cross_val_score(model_pipeline, X_train, y_train, cv=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "744473ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cross-validation scores: [0.81818182 0.63636364 0.63636364 0.81818182 0.81818182]\n"
     ]
    }
   ],
   "source": [
    "print(f\"Cross-validation scores: {cross_val_scores}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "1ac5744f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pipeline(steps=[('preprocessor',\n",
       "                 ColumnTransformer(remainder='passthrough',\n",
       "                                   transformers=[('cat', OneHotEncoder(),\n",
       "                                                  ['business_type',\n",
       "                                                   'location'])])),\n",
       "                ('classifier', LogisticRegression())])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model_pipeline.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0544a282",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_data = pd.DataFrame({\n",
    "    'previous_donations': [5],\n",
    "    'business_type': ['Restaurant'],\n",
    "    'location': ['Downtown']\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "33dab8f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = model_pipeline.predict(new_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "69a812f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted donation status: [1]\n"
     ]
    }
   ],
   "source": [
    "print(f\"Predicted donation status: {predictions}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c30ea28a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prediction probabilities: [[0.28405348 0.71594652]]\n"
     ]
    }
   ],
   "source": [
    "probabilities = model_pipeline.predict_proba(new_data)\n",
    "print(f\"Prediction probabilities: {probabilities}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcb2bfce",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
