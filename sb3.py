transactiond
import hashlib
import json
import time
import rsa

class Block:
  def __int__(self, index, transactions, timestamp, gps, altitude, previous_hash, nonce=0):
        self.index =index
        self.transactions = transactions
        self.timestamp = timestamp
        self.gps = gps
        self.altitude = altitude 
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()
