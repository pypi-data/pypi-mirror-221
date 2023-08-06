import time
import glob
from distutils.core import setup

setup(
  name = 'buckets',
  packages = ['buckets'],
  version = time.strftime('%Y%m%d'),
  description = 'Highly available key, value store - with GET/PUT operations over HTTPS.',
  long_description = 'Uses Paxos for replication and SQLite for storage. Leaderless and highly available.',
  author = 'Bhupendra Singh',
  author_email = 'bhsingh@gmail.com',
  url = 'https://github.com/magicray/buckets',
  keywords = ['paxos', 'kv', 'key', 'value', 'sqlite', 'consistent']
)
