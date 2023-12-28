from mojang import Client
import os
import subprocess

client = Client(os.environ.get("MC_EMAIL"), os.environ.get("MC_PW"))

# Get the account's profile information
profile = client.get_profile()

if os.name == 'nt':
    subprocess.run([".\\gradlew.bat", "runClient", '-Puuid=' + profile.id, '-PaccessToken='+client.bearer_token, '-Pusername='+profile.name, '-PuserType=mojang'])