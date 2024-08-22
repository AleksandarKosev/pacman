import http.server
import socketserver
import os
import logging
import signal
# """
# A simple python script that hosts a old-time favorite game. 
# !!!THE LEGENDARY PACMAN!!!WAKA WAKA!!
# ⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣅⢀⣽⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
# ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠁⠀⠀⣴⣶⡄⠀⣶⣶⡄⠀⣴⣶⡄
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠙⠋⠁⠀⠉⠋⠁⠀⠙⠋⠀
# ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# Overview
# This script runs a simple HTTP server to serve files from the 'pacman' directory. 
# The server listens on port 8080 and includes basic security features, logging and gracefully fails. 
# Tested on:
#     Microsoft Edge

# In the future we might actually plan switching to flask or django to host it, or maybe even containerize it in docker,
# so everyone can feel nostalgic, even boomers. 
# """

def shutdown_server(signum, frame):
    httpd.shutdown()
    print("Server shutting down...")

# We can choose any port.
PORT = 8080

#Logging activity
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Check if folder exists actually
WEB_DIR = os.path.abspath("pacman")
if not os.path.exists(WEB_DIR):
    raise FileNotFoundError(f"Directory {WEB_DIR} does not exist")
os.chdir(WEB_DIR)

#Hosting the game on the most simplest way, logging the activity and gracefully catching if something goes wrong.
Handler = http.server.SimpleHTTPRequestHandler
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving website on http://localhost:{PORT}")
        logger.info(f"Serving website on http://localhost:{PORT}")
        httpd.serve_forever()
except Exception as e:
    print(f"Server failed to start: {e}")
    logger.info(f"Server failed to start: {e}")

#Cleaning up.
signal.signal(signal.SIGINT, shutdown_server)
signal.signal(signal.SIGTERM, shutdown_server)