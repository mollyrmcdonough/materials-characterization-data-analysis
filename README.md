# Materials Characterization Data Analysis (MCDA)
Python modules to analyze charecterization data.

In order to start using this package in it's current state, you first need to edit the .env file to set the path correctly in order to use the package pre-release. If you don't have a .env file, just make one within vscode.

You must change the .env file to contain `PYTHONPATH=/;src/;${PYTHONPATH}` for Windows. If you use Linux or MacOS, you need to change it to `PYTHONPATH=/:src/:${PYTHONPATH}` (replacing `;` with `:`). If the PATH is not properly set, you'll see linting errors and you won't be able to use this package. When the package is actually released, you will not need to do this.
