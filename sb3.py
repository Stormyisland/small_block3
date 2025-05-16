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
  def compute_hash(self):
      block_string = json.dumps(sel.__dict__, sort_keys=True)
      return hashlib.sha256(block_string.encode()).hexdigest()
class Blockchain:
  difficuty = 2
  reward = 10
  def __int__(self):
    self.unconfermed_transactions = []
    self.chain =[]
    self.create_genesis_block()
  def 
