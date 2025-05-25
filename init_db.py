from utils.database import init_db, User, get_db
import pandas as pd
from pathlib import Path
from utils.file_reader import DATA_DIR
from utils.config import get_config

def main():
    print("Initializing database...")
    print(f"Using database: {get_config('DB_NAME', 'mix_server')}")
    init_db()
    
    # Import users from sample.csv
    file_path = DATA_DIR / "sample.csv"
    
    if file_path.exists():
        print(f"Importing users from {file_path}...")
        df = pd.read_csv(file_path)
        
        db = get_db()
        count = 0
        
        for _, row in df.iterrows():
            # Check if user already exists
            existing_user = db.query(User).filter(User.email == row['email']).first()
            if not existing_user:
                # Create new user
                new_user = User(
                    name=row['name'],
                    email=row['email'],
                    signup_date=row.get('signup_date') if 'signup_date' in row else None
                )
                db.add(new_user)
                count += 1
        
        db.commit()
        print(f"Successfully imported {count} users.")
    else:
        print(f"Sample data file not found: {file_path}")
    
    print("Database initialization complete.")

if __name__ == "__main__":
    main()
