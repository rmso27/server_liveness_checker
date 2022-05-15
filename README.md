# Server Liveness Checker

A Python tool to check the liveness status of a given list of servers

## Instructions

1. Edit the host.json file and add the hosts like this:

``
[<br />
	{<br />
		"host": "127.0.0.1",<br />
		"description": "Localhost"<br />
    	},<br />
	{<br />
		"host": "google.com",<br />
		"description": "Google Website"<br />
	},<br />
]
``

2. Pip install the necessary modules:

``
pip install -r requirements.txt
``

3. Execute the script:

``
python server_liveness_checker.py
``

## Output

