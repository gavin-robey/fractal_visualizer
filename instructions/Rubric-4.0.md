# CS 1440 Assignment 4.0 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 25 pts | Software Development Plan is comprehensive and well-written<br/>DuckieCorp project conventions are followed
| 5  pts | Signature is filled out properly
| 10 pts | Code smells are cataloged in `doc/Smells.md`<br/>Each piece of required information is included: location, code snippet, explanation and fix description
| 5 pts  | A User's Manual explains the program's user interface<br/>Is written for a non-technical audience using simple terms<br/>Avoids describing internal details about how the program works
| 15 pts | A UML class diagram describes your design<br/>Class diagram adheres to UML standards as far as these were explained in class<br/>All modules/classes are represented, behaviors and data members are accounted for, and relationships between modules are described
| 15 pts | Increase coverage of unit tests to seven (7) tests<br/>All unit tests pass<br/>No trivial unit tests are present
| 10 pts | Implementation: the original user interface functionality is preserved<br/>No new features or capabilities are added to the refactored program
| 20 pts | Implementation: Program requirements are met<br/>The new code is cleaner than the original starter code<br/>No code smells from the starter code are in the final product, nor are any other notable code smells added
| 5 pts  | All five (5) Git tags are present and appropriately applied <br/>`A4.0-analyzed` <br/>`A4.0-designed` <br/>`A4.0-implemented` <br/>`A4.0-tested` <br/>`A4.0-deployed`

**Total points: 110**


## Penalties

*Please read the "How To Submit Assignments" page of Canvas (found under the DuckieCorp Employee Handbook Module) for more information on these penalties and what we expect.*

***Penalties for this assignment***:

0.  **110 point penalty** if your program imports any modules **except**:
    *   `unittest`
    *   `sys`
    *   `time`
    *   `math`
    *   `tkinter`
    *   modules that are provided by the starter code
    *   modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.
1.  **10 point penalty** The last commit of this assignment does not bear the tag `A4.0-deployed`.
2.  **15 point penalty**  if your UML diagram is unreadable.  Watch out for a transparent background (on Diagrams.net, click File -> Export as -> PNG..., then make sure that the option "Transparent background" is left unchecked).  Make sure that the background isn't black, as this obscures the lines connecting classes to each other.  Make sure that the file size is large enough to make the text legible, and that the colors of the diagram stand out in sharp contrast to the background.
3.  **10 point penalty** for each  _trivial_ unit test (i.e. a unit test which unconditionally passes without meaningfully testing some functionality)

***Penalties for all assignments***:

#### Project Layout
0. **10 point penalty** if the repository does not follow the Git Repository Naming Convention
1. **10 point penalty** if the submitted project is not a clone of the starter code repository.
2. **10 point penalty** if there is an omission of required files and directories (missing, renamed, or moved from their expected location)
3. **10 point penalty** if there are forbidden files and directories in the submission
4. **10 point penalty** if there is no `.gitignore` file (whether it is missing or corrupted)
5. **Late Penalty**:
    *   \<24hrs late = -25% total points
    *   \>=24hrs & <48hrs = -50% total points
    *   \>=48hours = -100% total points


#### Modules and Functions
0. **10 point penalty** if a module fails to import due to misspelling or incorrect capitalization.
1. **10 point penalty** if the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
2. **10 point penalty** `eval()` or a similar function is used by your program; use type constructor functions such as `int()` and `float()` instead
3. **\<Varies\> point penalty** A library which the grader doesn't happen to have installed is imported; The resulting `ModuleNotFoundError` is treated as a crash and penalized accordingly
4. **20 point penalty** A library not permitted by the instructions is used, but doesn't result in a crash

#### Files and Paths
0. **10 point penalty** if the program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
1. **10 point penalty** if one or more data files are not closed after being processed in *ordinary* situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they will automatically be closed as your program exits.
2. **100% point penalty** if external programs are called upon to do the work.  Our customer has hired you to create a pure-Python solution, not a shell script that relies on external programs.
    - Do not use `os.system()`, `subprocess`, `pipes` or similar functions and libraries
    - Write a pure Python solution, not a script that leverages external programs

#### All Else
0. **Crashing Code Penalty**:
    * *Reminder: it is your responsibility to test and ensure that your program works on your grader's computer*
    *   Code that crashes and cannot be quickly & easily fixed by the grader will receive 0 points on the implementation portions of the rubric
    *   Code that crashes and CAN be quickly & easily fixed by the grader (or crashes only part of the time) will receive, at most, half-credit on the implementation portion of the rubric
