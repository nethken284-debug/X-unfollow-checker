# X Unfollow Checker

Find accounts you follow on X (Twitter) that don't follow you back.

Runs entirely on your own computer using your X data archive.
No login, no API key, no scraping.

## How to use

1. On X, go to **Settings → Your account → Download an archive of your data** and wait for the archive.
2. Unzip it and find `following.js` and `follower.js` (inside the `data` folder).
3. Create a `data` folder next to `unfollow_checker.py` and put both files in it.
4. Run:

```bash
   python3 unfollow_checker.py
```

5. The script prints the account ID and profile link of everyone who doesn't follow you back.

## Requirements

- Python 3 (standard library only)
- Tested on macOS

## License

MIT
