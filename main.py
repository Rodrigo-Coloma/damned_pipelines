#imports
from dotenv import 

def main():

# Inputs

API_TOKEN = #API TOKEN (REMEMBER: do not push these to your repo)
USERNAME = #USERNAME
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ih-datapt-mad/'
REPO = #LAB_REPOSITORY
SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open' 

if __name__ == '__main__':
    main()