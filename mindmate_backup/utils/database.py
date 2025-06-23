import sqlite3
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent.parent / "data" / "mindmate.db"

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        logger.error(f"Failed to connect to database: {str(e)}")
        raise

def get_journal_stats(user_id: str = "default_user") -> dict:
    """Get journal statistics including total entries and average mood"""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Get total entries
            cursor.execute("""
                SELECT COUNT(*) as total_entries, 
                       AVG(mood_score) as avg_mood
                FROM journal_entries
                WHERE user_id = ?
            """, (user_id,))
            
            result = cursor.fetchone()
            return {
                "total_entries": result["total_entries"] or 0,
                "avg_mood": result["avg_mood"] or 0
            }
    except Exception as e:
        logger.error(f"Failed to get journal stats: {str(e)}")
        return {"total_entries": 0, "avg_mood": 0}

def get_meditation_stats(user_id: str = "default_user") -> dict:
    """Get meditation statistics including total minutes"""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Get total minutes
            cursor.execute("""
                SELECT SUM(minutes) as total_minutes
                FROM meditation_sessions
                WHERE user_id = ?
            """, (user_id,))
            
            result = cursor.fetchone()
            return {
                "total_minutes": result["total_minutes"] or 0
            }
    except Exception as e:
        logger.error(f"Failed to get meditation stats: {str(e)}")
        return {"total_minutes": 0}

def init_db():
    """Initialize the database with required tables"""
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Create journal entries table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS journal_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    timestamp DATETIME NOT NULL,
                    entry_type TEXT NOT NULL,
                    content TEXT NOT NULL,
                    mood_score REAL NOT NULL,
                    keywords TEXT
                )
            """)
            
            # Create meditation sessions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS meditation_sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    timestamp DATETIME NOT NULL,
                    session_type TEXT NOT NULL,
                    minutes INTEGER NOT NULL,
                    notes TEXT
                )
            """)
            
            conn.commit()
            
    except Exception as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        raise
