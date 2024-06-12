import os


OPENAI_API_KEY = 'OPENAI_API_KEY'

# Get the absolute path of the current script
script_dir = os.path.dirname(__file__)

# Get the absolute path of the project root
PROJECT_ROOT = os.path.abspath(os.path.join(script_dir, '..'))
