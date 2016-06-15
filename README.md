# python-pandas
data-ing all the data

## Build & Run instructions

1.	Make sure you have python. (FWIW I am using 2.7.11.)
	```
	python --version
	```
2.	Clone dis repo, enter the directory.
	```
	git clone https://github.com/tesslins/python-pandas.git
    cd python-pandas
	```
3. Download Miniconda binary from here: http://conda.pydata.org/miniconda.html.
   (Make sure to get the version appropriate to your Python version!)

4. Follow instructions here: http://conda.pydata.org/docs/install/quick.html#os-x-miniconda-install.
    (There are also non-Mac instructions.)

5. Create environment.
    ```
    conda create -n <name_of_environment> python
    ```

6.	Activate environment.
	```
	source activate <name_of_environment>
	```

7.	Install pandas & recommended pandas dependencies.
	```
	conda install pandas
    conda install numexpr
    conda install bottleneck
    conda install matplotlib
	```
