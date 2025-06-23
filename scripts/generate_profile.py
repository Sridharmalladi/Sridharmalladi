#!/usr/bin/env python3
"""
Dynamic Profile README Generator
Generates personalized content for GitHub profile README
"""

import requests
import json
from datetime import datetime
import os

def get_github_stats(username):
    """Fetch GitHub statistics using GitHub API"""
    try:
        # Note: This would require a GitHub token for authenticated requests
        # For now, we'll use the public API endpoints
        api_url = f"https://api.github.com/users/{username}"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
        return None

def generate_quote():
    """Generate a motivational quote"""
    quotes = [
        "The best way to predict the future is to invent it. - Alan Kay",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Data is the new oil. - Clive Humby",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Technology is best when it brings people together. - Matt Mullenweg"
    ]
    import random
    return random.choice(quotes)

def create_profile_content():
    """Generate dynamic profile content"""
    content = f"""
# 🎯 Today's Focus

**Quote of the Day:** {generate_quote()}

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

## 🚀 Current Status
- 🔥 **Working on:** AI-powered analytics solutions
- 📚 **Learning:** Advanced LLM architectures
- 🎯 **Goal:** Building scalable ML pipelines
- 🌟 **Available for:** Exciting collaborations

## 📊 Quick Stats
- **Experience:** 4+ years in Data & AI
- **Projects Delivered:** 15+
- **Technologies Mastered:** 20+
- **Industries Served:** 5+

---
"""
    return content

if __name__ == "__main__":
    # Create the output directory
    os.makedirs("output", exist_ok=True)
    
    # Generate profile content
    profile_content = create_profile_content()
    
    # Write to file
    with open("output/profile_stats.md", "w") as f:
        f.write(profile_content)
    
    print("✅ Profile content generated successfully!")
    print("📁 Check output/profile_stats.md for the generated content") 