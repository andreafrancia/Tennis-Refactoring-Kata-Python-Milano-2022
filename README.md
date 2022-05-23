Tennis-Refactoring-Kata
=======================

  * https://github.com/emilybache/Tennis-Refactoring-Kata
  * curated by Emily Bache
  * Legacy project
  * Used for refactoring workshops
  * Available in many programming languages

Setup
=====
python3 -mvenv venv
source venv/bin/activate
pip install pytest

echo "venv/bin/pytest" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

How to refactor:
================

* A commit for each refactoring
* make evident and then remove duplication
* improve names
* remove non-needed complexity
* improve tests

Simple Design
=============
The code is simple when:
1. passes all tests
2. contains no duplicated logic
3. express all programmer intents
4. small

https://www.manning.com/books/the-mikado-method

https://cumulative-hypotheses.org/2011/08/30/tdd-as-if-you-meant-it/




Names:
======
draw -> pareggio
players_have_tied_score

DRY -vs- DAMP
=============
DRY: Don't Repeat Yourself
DAMP: Descriptive and Meaningful Names

Rule of thumb:
 * production code -> More DRY than DAMP
 * test code -> More DAMP that DRY
