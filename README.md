# Codewars Solutions

this repository is a personal archive of my solutions to [Codewars](https://www.codewars.com/) katas, written in python.

## Purpose

im using codewars to build programming confidence working through problems of increasing difficulty. this repo exists to:

- track my progress over time and see how my approach to problems evolves
- keep a searchable record of problems ive solved in case i want to revisit them
- build a public portfolio of consistent practice
- force a bit of accountability, if it's tracked, im more likely to keep at it

## Structure

each solved kata gets its own folder, organized by difficulty (kyu rank):

```
/6kyu/kata-slug/
    README.md       # link to the problem + brief notes
    solution.py     # my solution
/7kyu/another-kata/
    README.md
    solution.py
```

each kata has a `README.md` file which contains a link back to the original problem on Codewars and a short paraphrase for context. solution files includes comments as well as a `if __name__ == "__main__":` guard to check if the file is being run directly or is being imported as a module.

if the file was being run directly it will fire the code block inside the if statement. if it was imported, the block gets skipped.

## Notes

- solutions here reflect my thinking at the time i solved them, not necessarily the "optimal" solution. some may get revisited and refactored later.
