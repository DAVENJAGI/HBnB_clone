                                AirBnB_clone
====================================================================================
This is a repository that contains air bnb clone website, built using python. It's a full web app built using Python programming language, mostly, integrated with other languages. It's built sequentially, while adding and integrating other programming languages and frameworks. It ontains a python command interpreter for managing the project

DIRECTORIES:

*The repository contains various directories  with different files in them, that add different fratures to it.
*The various directories include AUTHORS, CONSOLE.PY, MODELS, and finally TESTS.

            ******AUTHORS******
*The AUTHORS is a file found in the root of the repository. It contais the details of the various contributors of the project, namely, DAVENJAGI, and KEITH NYIRENDA.

            ******README.md******
*This is a file in the root of the repository basically giving a brief description of what the repository contains.

            ******calculator.py******
 *This is a file containing pycodestyle compliant code that does simple math calculations.

            ******console.py******
*This is a file in the root of the repository that contains the code for commandline interpreter for the python project, basically a shell like interpreter used to manage the whole project during the development and during the mintenance of the code.

            ******MODELS******
*This is a DIRECTORY containing the python files for the project, it contains the files __init__.py, base_model.py, users.py, and a directory ENGINES.

                #----------base_model.py------------------
    * This file contains code for a class BaseModel that defines all common methods or attributes for other classes.
    * The class BaseModel contains public instance attributes namely;
            - id: string, assigns with an UUID when an instance us created. We use the uuid.uuid4() function to generate the unique id, an dit should  be converted to a string. We should have a unique id for each BaseModel
            - created_at: we use the datetime module to assign with the current datetime when an instance is created.
            - updated_at: we use the datetime module here too to assign the current datetime when an instance is created and updated everytime you change your object.
    * We use the __str__ to print strings for [<class name]> (self.id) <self.__dict__>
    * We have the method save that updates public instance updated_at with the current datetime
    * to_dict method returns a dictionary that contains all keys/values of __dict__ of the instance. By using self.__dict only instance attributes set will be returned
    * We use the ISO time format for the created_at and updated_at.

            ******ENGINE*****
This is a directory that cotains file used to store the objests in the json format

            ******tests******
*This is a repository containing the test files.
*This project uses the unittest module available in python

