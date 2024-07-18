## How to execute specific test

- -n Argument is for number of parallel process
- --flake-runs is for same test needs to be executed how many times

### Python file with classes

```
pytest -n 15 test_unbox.py --flake-finder --flake-runs=15 -k 'test_demo_netcore' --html=report.html --self-contained-html