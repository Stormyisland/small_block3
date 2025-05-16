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
    
  def create_genesis_block(self):
    gwenesis_block = Block(0, [], time.time(), "0")
    self.chain.append(genesis_block)

  def last_block(self):
    return self.chain[-1]

  def add_transaction(self,transaction):
    self.unconfirmed_transactions.append(transaction)

  def mine(self, miner_address):
    if not self.unconfirmed_transactions.append(transactions)
       return False
    # Add reward for miner 
reward_tx = {
  'from' : 'network'
  'to': miner_address,
  'amount': self.reward,
  'signature':''
}
self.unconfirmed_tranactions.append(reward_tx)

last_block = self.last_block()
new_block = Block(insex=last_block.hash)

     while not new_block.hash.startswith('0' * Blockchain.difficulty):
       new_block.nonce += 1
       new_block.hash = new_block.compute_hash()

      self.chain.append(new_block)
      sefl.uncomfirme_transactions = []
      return new_block 

class wallet:
  def __init__(self):
    (self.public_key, self.privat_key) = rsa.newkeys(512)

  def sign_transaction(self.transaction): 
   
  
  
    
    












  
