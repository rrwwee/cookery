---
name: cook
description: Use the kitchen camera script during hands-free cooking.
---

1. Open QuickTime's **New Movie Recording** and select the **top-down kitchen view**.
2. Create a temporary folder for this session and run [scripts/camera.sh](scripts/camera.sh) with that folder's path. It saves a picture every five seconds.
3. Open the folder's `latest.jpg`, check its modification time and confirm the top-down view. Tell the user you're ready and ask what they'd like to cook.
4. Help them cook: make the current recipe step clear, display large reference images when useful, and proactively check fresh captures at relevant moments during the conversation.
5. When they're finished, stop the script. Confirm cleanup with the user, then delete the session's capture folder and quit QuickTime.
