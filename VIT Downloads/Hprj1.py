{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f6d5c05d",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: scikit-learn in c:\\programdata\\anaconda3\\lib\\site-packages (1.0.2)\n",
      "Requirement already satisfied: numpy>=1.14.6 in c:\\users\\91738\\appdata\\roaming\\python\\python39\\site-packages (from scikit-learn) (1.23.5)\n",
      "Requirement already satisfied: scipy>=1.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from scikit-learn) (1.9.1)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from scikit-learn) (2.2.0)\n",
      "Requirement already satisfied: joblib>=0.11 in c:\\programdata\\anaconda3\\lib\\site-packages (from scikit-learn) (1.1.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3d9b1550",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.neighbors import NearestNeighbors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2dcc8da4",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('donor_data1.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b08ae2bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "interaction_matrix = pd.pivot_table(data, index='donor_id', columns='donor_name', values='previous_donations', fill_value=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "994e787f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "NearestNeighbors(algorithm='brute', metric='cosine')"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn_model = NearestNeighbors(metric='cosine', algorithm='brute')\n",
    "knn_model.fit(interaction_matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5232ae7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recommend_donors(donor_id, n_recommendations=3):\n",
    "    donor_index = interaction_matrix.index.get_loc(donor_id)\n",
    "    distances, indices = knn_model.kneighbors(interaction_matrix.iloc[donor_index].values.reshape(1, -1), n_neighbors=n_recommendations + 1)\n",
    "    recommended_indices = indices.flatten()[1:]\n",
    "    return interaction_matrix.index[recommended_indices].tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "867b669b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda3\\lib\\site-packages\\sklearn\\base.py:450: UserWarning: X does not have valid feature names, but NearestNeighbors was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "recommended = recommend_donors(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fae2ac8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recommended donors for Restaurant A: [62, 63, 65]\n"
     ]
    }
   ],
   "source": [
    "print(f\"Recommended donors for Restaurant A: {recommended}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76097cd6",
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
