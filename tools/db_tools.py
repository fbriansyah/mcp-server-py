from models.user import User
from server import mcp
from utils.database import get_db
from typing import List, Optional

@mcp.tool()
def list_users() -> str:
    """
    List all users in the database.
    
    Returns:
        A string containing user information.
    """
    db = get_db()
    users = db.query(User).all()
    
    if not users:
        return "No users found in the database."
    
    result = "Users in database:\n"
    for user in users:
        result += f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Signup: {user.signup_date}\n"
    
    return result

@mcp.tool()
def add_user(name: str, email: str) -> str:
    """
    Add a new user to the database.
    
    Args:
        name: The user's name
        email: The user's email address
        
    Returns:
        A confirmation message.
    """
    db = get_db()
    
    # Check if user with this email already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return f"User with email {email} already exists."
    
    # Create new user
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return f"User added successfully with ID: {new_user.id}"

@mcp.tool()
def import_users_from_csv(filename: str = "sample.csv") -> str:
    """
    Import users from a CSV file into the database.
    
    Args:
        filename: Name of the CSV file in the /data directory (default: sample.csv)
        
    Returns:
        A confirmation message.
    """
    import pandas as pd
    from pathlib import Path
    from utils.file_reader import DATA_DIR
    
    file_path = DATA_DIR / filename
    
    if not file_path.exists():
        return f"File {filename} not found in data directory."
    
    try:
        df = pd.read_csv(file_path)
        
        # Check if required columns exist
        required_columns = ['name', 'email']
        if not all(col in df.columns for col in required_columns):
            return f"CSV file must contain columns: {', '.join(required_columns)}"
        
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
        return f"Successfully imported {count} users from {filename}."
    
    except Exception as e:
        return f"Error importing users: {str(e)}"
