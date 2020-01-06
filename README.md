# random_name.py
Assembles Lists of Names to Json and Does Random Picks

It's simple enough. Look at the `get_random()` func for options, which I'll eventually put into argparse options.

```python
                                              
                                              # 
def get_random(times=1,                       # output iterations
               names=read_json(),             # custom list for
               first=True,                    # False for only Family
               last=True,                     # False for only First
               typical=random.randint(0, 1),  # 0 True, 1 False
               sex=random.randint(0, 1)):     # 0 Male, 1 Female
    ```
    
For now, just run it with `python3 -i random_names.py`
    
And at the `>>>` python shell, `get_random(20)` with options as keyargs or default require no arguments. This will print 20 names to stdout.
