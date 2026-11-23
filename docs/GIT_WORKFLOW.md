# GitHub workflow: personal laptop ↔ GitHub ↔ lab PC

Repository: https://github.com/chbsankar2003-hue/Navel-Project

## 1. Personal laptop: first-time setup
Install Git if needed, then open a terminal in the folder where you keep projects:
```bash
git --version
git clone https://github.com/chbsankar2003-hue/Navel-Project.git
cd Navel-Project
```
If the repository is private, GitHub will prompt you to authenticate. Use GitHub's browser/device login or a Personal Access Token when requested; never paste a token into a Python file or commit it.

Copy the reviewed project files into this cloned folder. Then:
```bash
git status
git add .
git commit -m "Add initial Navel project structure"
git push -u origin main
```
If Git says the default branch is not `main`, check with `git branch --show-current` and use the branch name it reports.

## 2. Lab PC: first-time setup
Open a terminal on the lab PC:
```bash
cd ~/control-studio/scripts/room_navigator
```
If `Navel-Project` does not exist there:
```bash
git clone https://github.com/chbsankar2003-hue/Navel-Project.git
```
If it already exists and is a Git clone:
```bash
cd Navel-Project
git status
git pull
```

## 3. Existing project folder warning
Your previous lab work is in:
`~/control-studio/scripts/room_navigator/navel_room_navigator`

Do **not** run `git clone` over that folder and do not delete it. First inspect it:
```bash
cd ~/control-studio/scripts/room_navigator/navel_room_navigator
ls -la
git status
```
If it is not already a Git repository, clone the new repo into a sibling folder named `Navel-Project` instead. Keep the old folder until all old scripts and CSV results have been backed up and compared.

## 4. Every future update
Laptop:
```bash
git pull
# edit/create files
git status
git add scripts docs README.md
git commit -m "Describe the change"
git push
```
Lab PC:
```bash
cd ~/control-studio/scripts/room_navigator/Navel-Project
git pull
```

## 5. If both computers changed files
Do not blindly overwrite. Run:
```bash
git status
git pull
```
If Git reports a conflict, stop and resolve it before running experiments. Do not use `git reset --hard` or delete files to "fix" it.

## 6. Private repository
A private repository is recommended if it contains unpublished university project work. Check GitHub repository Settings → General → Danger Zone / Change repository visibility. Never publish robot credentials, personal data, or sensitive lab information.
