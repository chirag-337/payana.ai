from typing import Any
import logging
from app.config import settings

logger = logging.getLogger("PayanaDB")

# Lazy Supabase client initialization
_supabase_client = None

def get_supabase_client():
    global _supabase_client
    if _supabase_client is None:
        try:
            from supabase import create_client
            _supabase_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
        except Exception as e:
            logger.warning(f"Supabase client initialization deferred: {e}")
            _supabase_client = None
    return _supabase_client
