# Git & GitHub Version Control Assignment

## Overview

This assignment demonstrates Git and GitHub version control concepts including:

* SSH Authentication
* Repository Creation
* Cloning via SSH
* Branch Creation and Management
* Commits and Push Operations
* Branch Merging
* Merge Conflict Resolution
* Git Reset
* Git Rebase

---

# Prerequisites

Install the following software:

* Git
* Python
* Flask
* MongoDB Atlas Account
* GitHub Account

Verify Git installation:

```bash
git --version
```

---

# PART 1: Create Repository, Clone Using SSH, Create Branch, Commit and Merge

## Step 1: Create GitHub Repository

1. Log in to GitHub.
2. Click **New Repository**.
3. Repository Name:

```text
flask-assignment
```

4. Choose Public or Private.
5. Click **Create Repository**.

---

## Step 2: Generate SSH Key

Check whether an SSH key already exists:

```bash
ls ~/.ssh
```

Generate a new SSH key if required:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press **Enter** for all prompts.

### Why SSH?

SSH allows secure authentication with GitHub without entering your username and password each time.

---

## Step 3: Start SSH Agent

```bash
eval "$(ssh-agent -s)"
```

Add the SSH key:

```bash
ssh-add ~/.ssh/id_ed25519
```

---

## Step 4: Copy Public Key

Display the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output.

Example:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExampleKey your_email@example.com
```

---

## Step 5: Add SSH Key to GitHub

Navigate to:

```text
GitHub → Settings → SSH and GPG Keys → New SSH Key
```

Paste the copied public key and click:

```text
Add SSH Key
```

---

## Step 6: Test SSH Connection

```bash
ssh -T git@github.com
```

Expected output:

```text
Hi username! You've successfully authenticated.
```

---

## Step 7: Clone Repository Using SSH

Copy the SSH URL from GitHub.

Example:

```bash
git clone git@github.com:Gyani06/flask-assignment.git
```

Move into the repository:

```bash
cd flask-assignment
```

---

## Step 8: Create Branch Named After Username

Example:

```bash
git checkout -b GitHub_Course
```

### Explanation

```text
git checkout -b
```

Creates and immediately switches to a new branch.

---

## Step 9: Add Flask Project Files

Example files:

```text
app.py
data.json
requirements.txt
README.md
```

Copy all files into the repository folder.

---

## Step 10: Check Repository Status

```bash
git status
```

---

## Step 11: Add Files to Staging Area

```bash
git add .
```

### Explanation

Stages all modified and new files for commit.

---

## Step 12: Commit Files

```bash
git commit -m "Added Flask project"
```

---

## Step 13: Push Branch

```bash
git push origin GitHub_Course
```

---

## Step 14: Merge Into Main Branch

Switch to main:

```bash
git checkout main
```

Pull latest changes:

```bash
git pull origin main
```

Merge branch:

```bash
git merge GitHub_Course
```

Push changes:

```bash
git push origin main
```

---

# PART 2: Create New Branch and Resolve Merge Conflict

## Step 1: Create Branch

```bash
git checkout -b GitHub_Course_new
```

---

## Step 2: Modify JSON File

### Before

```json
[
  {
    "id": 1,
    "name": "Gyani",
    "course": "Python"
  },
  {
    "id": 2,
    "name": "Ganesh",
    "course": "Flask"
  }
]
```

### After

```json
[
  {
    "id": 1,
    "name": "Gyani",
    "course": "Python"
  },
  {
    "id": 2,
    "name": "Ganesh",
    "course": "Flask"
  },
  {
    "id": 3,
    "name": "Amit",
    "course": "MongoDB"
  }
]
```

---

## Step 3: Commit Changes

```bash
git add data.json
git commit -m "Updated JSON data"
```

---

## Step 4: Push Branch

```bash
git push origin GitHub_Course_new
```

---

## Step 5: Merge Into Main

```bash
git checkout main
git merge GitHub_Course_new
```

---

## Merge Conflict Resolution

If Git displays:

```text
CONFLICT (content)
```

You may see:

```text
<<<<<<< HEAD
Old Content
=======
New Content
>>>>>>> GitHub_Course_new
```

Remove the conflict markers and keep the required content.

Example:

```json
[
  {
    "name": "Amit"
  }
]
```

Stage and commit:

```bash
git add data.json
git commit -m "Resolved merge conflict using GitHub_Course_new changes"
git push origin main
```

---

# PART 3: Create master_1 and master_2 Branches

## Step 1: Create master_1

```bash
git checkout main
git checkout -b master_1
```

---

## Step 2: Create To-Do Form

```html
<form method="POST">
    <input type="text" name="itemName" placeholder="Item Name">

    <textarea name="itemDescription"
    placeholder="Item Description"></textarea>

    <button type="submit">
        Submit
    </button>
</form>
```

---

## Step 3: Commit Changes

```bash
git add .
git commit -m "Added ToDo page frontend"
git push origin master_1
```

---

## Step 4: Create master_2

```bash
git checkout main
git checkout -b master_2
```

---

## Step 5: Create Backend Route

```python
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return "Saved"
```

---

## Step 6: Commit Changes

```bash
git add .
git commit -m "Added submittodoitem API"
git push origin master_2
```

---

## Step 7: Merge Both Branches

```bash
git checkout main

git merge master_1
git merge master_2

git push origin main
```

---

# PART 4: Sequential Commits, Reset and Rebase

## Switch to master_1

```bash
git checkout master_1
```

---

## First Commit – Add Item ID

```html
<input type="text"
       name="itemId"
       placeholder="Item ID">
```

```bash
git add .
git commit -m "Added Item ID field"
```

---

## Second Commit – Add Item UUID

```html
<input type="text"
       name="itemUUID"
       placeholder="Item UUID">
```

```bash
git add .
git commit -m "Added Item UUID field"
```

---

## Third Commit – Add Item Hash

```html
<input type="text"
       name="itemHash"
       placeholder="Item Hash">
```

```bash
git add .
git commit -m "Added Item Hash field"
```

---

## View Commit History

```bash
git log --oneline
```

Example:

```text
abc111 Added Item Hash field
abc222 Added Item UUID field
abc333 Added Item ID field
```

---

## Merge master_1 Into Main

```bash
git checkout main
git merge master_1
git push origin main
```

---

## Git Reset to Item ID Commit

Locate commit:

```bash
git log --oneline
```

Reset:

```bash
git reset --soft abc333
```

### Explanation

```text
--soft
```

* Moves HEAD to selected commit.
* Keeps changes staged.
* Does not remove files.

---

## Create New Commit

```bash
git commit -m "Rollback to Item ID version"
```

Push (if permitted):

```bash
git push origin main --force
```

---

## Rebase Main Into master_1

Switch branch:

```bash
git checkout master_1
```

Run rebase:

```bash
git rebase main
```

or

```bash
git rebase main master_1
```

### Explanation

Rebase reapplies master_1 commits on top of the latest main branch history while preserving individual commits.

---

## If Rebase Conflict Occurs

Resolve conflicts manually.

Stage changes:

```bash
git add .
```

Continue rebase:

```bash
git rebase --continue
```

Repeat until completed.

---

## Verify Commit History

```bash
git log --oneline --graph --all
```

Expected commits:

```text
Added Item ID field
Added Item UUID field
Added Item Hash field
Rollback to Item ID version
```

---

# Git Commands Summary

```bash
git clone <ssh-url>

git checkout -b GitHub_Course
git add .
git commit -m "Added Flask project"
git push origin GitHub_Course

git checkout main
git merge GitHub_Course

git checkout -b GitHub_Course_new
git add .
git commit -m "Updated JSON file"

git checkout main
git merge GitHub_Course_new

git checkout -b master_1
git checkout -b master_2

git merge master_1
git merge master_2

git reset --soft <commit-id>

git rebase main

git log --oneline --graph --all
```

---

# Learning Outcomes

By completing this assignment, you will gain hands-on experience with:

* GitHub SSH Authentication
* Repository Management
* Branching Strategies
* Commits and Push Operations
* Merge Operations
* Conflict Resolution
* Git Reset
* Git Rebase
* Commit History Management

---

# Author

**Gyaneshwar Sharma**
