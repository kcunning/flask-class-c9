import os
from app import app

# Host and port are unique to Cloud 9. You don't need these on your local,
# or if using other services
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True)