import os
import sys

TOKEN = os.getenv("TOKEN")

print("DEBUG_TOKEN_VALUE:", repr(8244461517:AAGhYk4hXRy4lRgrvppImjY2ZYpaeb6wo_Q), flush=True)

if not TOKEN:
    print("FATAL: TOKEN env var is missing", flush=True)
    sys.exit(1)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
