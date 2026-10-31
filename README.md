# [Aerokicks Cinema Hall](https://aungmarma201-dev.github.io/aerokicks-cinema-hall/)

A small browser-based cinema ticket counter inspired by the simple interactive layout of the Morse Code WebApp example. Visitors can use the ticket calculator directly on the website, while the original command-line Python version is available to download.
🌐 **Live Website:** [Open Aerokicks Cinema Hall](https://aungmarma201-dev.github.io/aerokicks-cinema-hall/)
## Features

- Buy between 1 and 10 tickets at $10 each
- Automatically apply a 10% discount when buying more than 5 tickets
- Add popcorn ($5), soda ($3), and candy ($2)
- Add multiple snacks and remove individual snacks
- View a live price breakdown and generate a final bill
- Download and run the Python command-line version

## Run locally

Open `index.html` in a web browser. No installation or external libraries are required.

To run the Python version, install Python 3 and run:

```bash
python movie_ticket_counter.py
```

## Publish with GitHub Pages

1. Upload `index.html`, `movie_ticket_counter.py`, and this `README.md` to the root of your GitHub repository.
2. Open the repository's **Settings** tab.
3. Select **Pages** in the sidebar.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch `main` and folder `/ (root)`, then save.
6. After GitHub Pages publishes the site, open the URL shown in the Pages settings.

The website runs in the visitor's browser using JavaScript. GitHub Pages does not execute the Python file; the Python file is provided as a download for visitors who want to run it locally.
