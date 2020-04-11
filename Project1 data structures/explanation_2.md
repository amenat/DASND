Problem 2: File search

Directories are best modelled by a tree and finding all items means doing a treversal and filtering out items. This process in inherently recursive in nature hence recursive solution is fairly simple to implement.

Pseudocode:

```create a list to store found files

    for all child items:
        if file: check if it meets criteria, add to list of found files
        if directory: recurse and merge result with parent call
```

Since this is basically treversal of a tree runtime complexity is O(n) where n is total number of folders and files.

Worst case space complexity is O(n) since most modern file systems limit file names, in worst case when all files match the filter we will be storing n filenames in the list which will amount to O(n) space.