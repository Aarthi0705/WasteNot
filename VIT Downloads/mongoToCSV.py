{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6f99c0e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c74a343c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting pymongo\n",
      "  Downloading pymongo-4.11-cp39-cp39-win_amd64.whl (731 kB)\n",
      "     -------------------------------------- 731.2/731.2 kB 1.3 MB/s eta 0:00:00\n",
      "Collecting dnspython<3.0.0,>=1.16.0\n",
      "  Downloading dnspython-2.7.0-py3-none-any.whl (313 kB)\n",
      "     -------------------------------------- 313.6/313.6 kB 1.2 MB/s eta 0:00:00\n",
      "Installing collected packages: dnspython, pymongo\n",
      "Successfully installed dnspython-2.7.0 pymongo-4.11\n"
     ]
    }
   ],
   "source": [
    "!pip install pymongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "50050284",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pymongo import MongoClient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c0073e06",
   "metadata": {},
   "outputs": [],
   "source": [
    "client = MongoClient(\"mongodb://localhost:27017/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4486d7b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "db = client[\"test_db\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4fa631d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "collection = db[\"users\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d6586fc0",
   "metadata": {},
   "outputs": [
    {
     "ename": "ServerSelectionTimeoutError",
     "evalue": "localhost:27017: [WinError 10061] No connection could be made because the target machine actively refused it (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms), Timeout: 30s, Topology Description: <TopologyDescription id: 67a3e2bd98bac325441d95d9, topology_type: Unknown, servers: [<ServerDescription ('localhost', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('localhost:27017: [WinError 10061] No connection could be made because the target machine actively refused it (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms)')>]>",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mServerSelectionTimeoutError\u001b[0m               Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_32716\\93046618.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcollection\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m\"_id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\cursor.py\u001b[0m in \u001b[0;36m__next__\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1279\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1280\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__next__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[0m_DocumentType\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1281\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1282\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1283\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__iter__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m->\u001b[0m \u001b[0mCursor\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0m_DocumentType\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\cursor.py\u001b[0m in \u001b[0;36mnext\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1255\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_empty\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1256\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mStopIteration\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1257\u001b[1;33m         \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_refresh\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1258\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpopleft\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1259\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\cursor.py\u001b[0m in \u001b[0;36m_refresh\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1203\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_exhaust\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1204\u001b[0m             )\n\u001b[1;32m-> 1205\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_message\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mq\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1206\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_id\u001b[0m\u001b[1;33m:\u001b[0m  \u001b[1;31m# Get More\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1207\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_limit\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\cursor.py\u001b[0m in \u001b[0;36m_send_message\u001b[1;34m(self, operation)\u001b[0m\n\u001b[0;32m   1098\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1099\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1100\u001b[1;33m             response = client._run_operation(\n\u001b[0m\u001b[0;32m   1101\u001b[0m                 \u001b[0moperation\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_unpack_response\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maddress\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_address\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1102\u001b[0m             )\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\_csot.py\u001b[0m in \u001b[0;36mcsot_wrapper\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    117\u001b[0m                     \u001b[1;32mwith\u001b[0m \u001b[0m_TimeoutContext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    118\u001b[0m                         \u001b[1;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 119\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    120\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    121\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mcast\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mF\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcsot_wrapper\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\mongo_client.py\u001b[0m in \u001b[0;36m_run_operation\u001b[1;34m(self, operation, unpack_res, address)\u001b[0m\n\u001b[0;32m   1750\u001b[0m             )\n\u001b[0;32m   1751\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1752\u001b[1;33m         return self._retryable_read(\n\u001b[0m\u001b[0;32m   1753\u001b[0m             \u001b[0m_cmd\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1754\u001b[0m             \u001b[0moperation\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_preference\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\mongo_client.py\u001b[0m in \u001b[0;36m_retryable_read\u001b[1;34m(self, func, read_pref, session, operation, address, retryable, operation_id)\u001b[0m\n\u001b[0;32m   1859\u001b[0m             \u001b[0mretryable\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mretry_reads\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0msession\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0min_transaction\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1860\u001b[0m         )\n\u001b[1;32m-> 1861\u001b[1;33m         return self._retry_internal(\n\u001b[0m\u001b[0;32m   1862\u001b[0m             \u001b[0mfunc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1863\u001b[0m             \u001b[0msession\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\_csot.py\u001b[0m in \u001b[0;36mcsot_wrapper\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    117\u001b[0m                     \u001b[1;32mwith\u001b[0m \u001b[0m_TimeoutContext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    118\u001b[0m                         \u001b[1;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 119\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    120\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    121\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mcast\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mF\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcsot_wrapper\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\mongo_client.py\u001b[0m in \u001b[0;36m_retry_internal\u001b[1;34m(self, func, session, bulk, operation, is_read, address, read_pref, retryable, operation_id)\u001b[0m\n\u001b[0;32m   1815\u001b[0m         \u001b[1;33m:\u001b[0m\u001b[1;32mreturn\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mOutput\u001b[0m \u001b[0mof\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mcalling\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1816\u001b[0m         \"\"\"\n\u001b[1;32m-> 1817\u001b[1;33m         return _ClientConnectionRetryable(\n\u001b[0m\u001b[0;32m   1818\u001b[0m             \u001b[0mmongo_client\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1819\u001b[0m             \u001b[0mfunc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfunc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\mongo_client.py\u001b[0m in \u001b[0;36mrun\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   2563\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_check_last_error\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcheck_csot\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2564\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2565\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_read\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_is_read\u001b[0m \u001b[1;32melse\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_write\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2566\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mServerSelectionTimeoutError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2567\u001b[0m                 \u001b[1;31m# The application may think the write was never attempted\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\mongo_client.py\u001b[0m in \u001b[0;36m_read\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   2698\u001b[0m         \u001b[1;33m:\u001b[0m\u001b[1;32mreturn\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mOutput\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[0;31m'\u001b[0m\u001b[0ms\u001b[0m \u001b[0mcall\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2699\u001b[0m         \"\"\"\n\u001b[1;32m-> 2700\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_server\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_server\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2701\u001b[0m         \u001b[1;32massert\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_read_pref\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Read Preference required on read calls\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2702\u001b[0m         with self._client._conn_from_server(self._read_pref, self._server, self._session) as (\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\mongo_client.py\u001b[0m in \u001b[0;36m_get_server\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   2654\u001b[0m         \u001b[1;33m:\u001b[0m\u001b[1;32mreturn\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mAbstraction\u001b[0m \u001b[0mto\u001b[0m \u001b[0mconnect\u001b[0m \u001b[0mto\u001b[0m \u001b[0mserver\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2655\u001b[0m         \"\"\"\n\u001b[1;32m-> 2656\u001b[1;33m         return self._client._select_server(\n\u001b[0m\u001b[0;32m   2657\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_server_selector\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2658\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_session\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\mongo_client.py\u001b[0m in \u001b[0;36m_select_server\u001b[1;34m(self, server_selector, session, operation, address, deprioritized_servers, operation_id)\u001b[0m\n\u001b[0;32m   1645\u001b[0m                     \u001b[1;32mraise\u001b[0m \u001b[0mAutoReconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"server %s:%s no longer available\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0maddress\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# noqa: UP031\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1646\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1647\u001b[1;33m                 server = topology.select_server(\n\u001b[0m\u001b[0;32m   1648\u001b[0m                     \u001b[0mserver_selector\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1649\u001b[0m                     \u001b[0moperation\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\topology.py\u001b[0m in \u001b[0;36mselect_server\u001b[1;34m(self, selector, operation, server_selection_timeout, address, deprioritized_servers, operation_id)\u001b[0m\n\u001b[0;32m    400\u001b[0m     ) -> Server:\n\u001b[0;32m    401\u001b[0m         \u001b[1;34m\"\"\"Like select_servers, but choose a random server if several match.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 402\u001b[1;33m         server = self._select_server(\n\u001b[0m\u001b[0;32m    403\u001b[0m             \u001b[0mselector\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    404\u001b[0m             \u001b[0moperation\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\topology.py\u001b[0m in \u001b[0;36m_select_server\u001b[1;34m(self, selector, operation, server_selection_timeout, address, deprioritized_servers, operation_id)\u001b[0m\n\u001b[0;32m    378\u001b[0m         \u001b[0moperation_id\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mOptional\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    379\u001b[0m     ) -> Server:\n\u001b[1;32m--> 380\u001b[1;33m         servers = self.select_servers(\n\u001b[0m\u001b[0;32m    381\u001b[0m             \u001b[0mselector\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moperation\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mserver_selection_timeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maddress\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moperation_id\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    382\u001b[0m         )\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\topology.py\u001b[0m in \u001b[0;36mselect_servers\u001b[1;34m(self, selector, operation, server_selection_timeout, address, operation_id)\u001b[0m\n\u001b[0;32m    285\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    286\u001b[0m         \u001b[1;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_lock\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 287\u001b[1;33m             server_descriptions = self._select_servers_loop(\n\u001b[0m\u001b[0;32m    288\u001b[0m                 \u001b[0mselector\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mserver_timeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moperation\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moperation_id\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maddress\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    289\u001b[0m             )\n",
      "\u001b[1;32m~\\AppData\\Roaming\\Python\\Python39\\site-packages\\pymongo\\synchronous\\topology.py\u001b[0m in \u001b[0;36m_select_servers_loop\u001b[1;34m(self, selector, timeout, operation, operation_id, address)\u001b[0m\n\u001b[0;32m    335\u001b[0m                         \u001b[0mfailure\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_error_message\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mselector\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    336\u001b[0m                     )\n\u001b[1;32m--> 337\u001b[1;33m                 raise ServerSelectionTimeoutError(\n\u001b[0m\u001b[0;32m    338\u001b[0m                     \u001b[1;34mf\"{self._error_message(selector)}, Timeout: {timeout}s, Topology Description: {self.description!r}\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    339\u001b[0m                 )\n",
      "\u001b[1;31mServerSelectionTimeoutError\u001b[0m: localhost:27017: [WinError 10061] No connection could be made because the target machine actively refused it (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms), Timeout: 30s, Topology Description: <TopologyDescription id: 67a3e2bd98bac325441d95d9, topology_type: Unknown, servers: [<ServerDescription ('localhost', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('localhost:27017: [WinError 10061] No connection could be made because the target machine actively refused it (configured timeouts: socketTimeoutMS: 20000.0ms, connectTimeoutMS: 20000.0ms)')>]>"
     ]
    }
   ],
   "source": [
    "data = list(collection.find({}, {\"_id\": 0}))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5207228f",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_32716\\1923510999.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "df = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ec199281",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_32716\\100344739.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mto_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"output.csv\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mindex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "df.to_csv(\"donor_data.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "539b63c3",
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
