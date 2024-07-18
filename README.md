## How to execute specific test

- -n Argument is for number of parallel process
- --flake-runs is for same test needs to be executed how many times

### Python file with classes

```
pytest -n 5 test_unbox.py --flake-finder --flake-runs=10 -k 'test_demo_netcore' --html=report.html --self-contained-html