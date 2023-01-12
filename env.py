import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "14202110").strip()
API_HASH = os.getenv("API_HASH", "45f3a3ac8effd88e42aeabe3cfe4f520").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5409377598:AAEc2gVjT7hUuza9uPqqFaRvB2kX13kJEAI").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5537497510").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://ctypgtthtsituv:07f8cb5550bed652b0ecb0a7a16bc80f8aeb10c3d522b3be28a6f7bf8ea40370@ec2-54-155-14-129.eu-west-1.compute.amazonaws.com:5432/d5063872tcnfm1").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "VENOM_OFFICIAL_FAMILY")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
