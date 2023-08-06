import time
import glob
from distutils.core import setup

setup(
  name = 'binlogs',
  packages = ['binlogs'],
  version = time.strftime('%Y%m%d'),
  description = 'Highly available logger - with APPEND/TAIL operations over HTTPS.',
  long_description = 'Uses Paxos for replication and filesystem for storage. Leaderless and highly available.',
  author = 'Bhupendra Singh',
  author_email = 'bhsingh@gmail.com',
  url = 'https://github.com/magicray/binlogs',
  keywords = ['paxos', 'stream', 'pubsub', 'pub', 'sub', 'queue', 'consistent']
)
