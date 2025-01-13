# Customizing Git - [Git Configuration](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Configuration)

Read [Git Documentation](https://git-scm.com/docs) for more informations.

Pass `--system`, `--global` and `--local` flag to set configuration system-wide, globally or locally (specific to that git project).

```
git config --global user.name "Dhiraj Bhattarai"
git config --global user.email "dhiraj@example.com"
```

Set VSCode as a default/core code editor.
<!-- Default Code Editor -->
```
git config --global core.editor code
```
<!-- Pass `-w` flat to wait until the code editor is closed -->
```
git config --global core.editor "code -w"
```
<!-- Add commit message template -->
<!-- First create a file at /home/dyroz/.gitmessage.txt -->
```
git config --global commit.template ~/.gitmessage.txt
```