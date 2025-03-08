# Collation area

The collation work is not done here. The software used is the Standalone Collation Editor from
The Institute for Textual Scholarship and Electronic Editing (ITSEE).

https://itsee-wce.birmingham.ac.uk/

It is run on a local machine and the working data resides elsewhere.

regularizations.txt is a file to be incorporated with the json files of
transcriptions. It is no longer needed. I do the regularizations in the Standalone Collation Editor. The file will be deleted eventually.

The json files have been created by using David Flood's "criticus"

https://github.com/d-flood/criticus

Python 3.13 will not work. When I backed down to Python 3.12 the problem
with "lib2to3" disappeared. Others have run into the same problem with
other software.

David Flood has since updated Criticus with a new graphical
interface and support for Python 3.11+. I have not moved up to Python 3.13 again.
It works with 3.12 and I am not ready to risk anything.

