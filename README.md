# tinkoffhack

### to start the service:
`# make a venv before launch`

`pip install -r requirements.txt`

`python -m uvicorn api:app --reload`

### paths:
GET `/` - ui & docs

POST `/api/partners` - new partners

GET `/api/partners/{id}` - get partner info

PUT `/api/partners/{id}/cashback` - new cashback

