## NON-ESSENTIAL OR POSSIBLE FUTURE CHANGES

* Make the menu button stay on the screen at every scroll position

## Bugs

* Pressing nav buttons on mobile "eats" buttons and messes up the navbar until refreshed/reset

<br/><br/><br/>
---

### Modified from Cobyism/gh-pages-deploy.md gist (https://gist.github.com/cobyism/4730490#file-gh-pages-deploy-md) on deploying a website in a subfolder to gh-pages

Reference for management of my current working structure for my gh-pages deployment

---

# Deploying a subfolder to GitHub Pages

Sometimes you want to have a subdirectory on the `main` branch be the root directory of a repository’s `gh-pages` branch.

For the sake of this example, let’s pretend the subfolder containing your site is named `dist`.

### Step 1

Remove the `dist` directory from the project’s `.gitignore` file (if it’s ignored).

### Step 2

Make sure git knows about your subtree (the subfolder with your site).

```sh
git add dist && git commit -m "Initial dist subtree commit"
```

### Step 3

Use subtree push to send it to the `gh-pages` branch on GitHub.

```sh
git subtree push --prefix dist origin gh-pages
```

Boom. If your folder isn’t called `dist`, then you’ll need to change that in each of the commands above.

---