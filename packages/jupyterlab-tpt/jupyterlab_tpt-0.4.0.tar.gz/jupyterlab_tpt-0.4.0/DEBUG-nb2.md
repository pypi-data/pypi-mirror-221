# helpers

juytext dev released; notebook 7 released

# v0 - just notebook and jupytext

```bash
conda deactivate ; conda env remove -n nb7-text
conda create -y -n nb7-text python=3.11; conda activate nb7-text
pip install notebook; pip install --pre jupytext
pip freeze | egrep 'notebook|jupyte'
```

```bash
pip freeze | egrep 'notebook|jupyte'
jupyter-events==0.6.3
jupyter-lsp==2.2.0
jupyter_client==8.3.0
jupyter_core==5.3.1
jupyter_server==2.7.0
jupyter_server_terminals==0.4.4
jupyterlab==4.0.3
jupyterlab-pygments==0.2.2
jupyterlab_server==2.23.0
jupytext==1.15.0.dev1
notebook==7.0.0
notebook_shim==0.2.3
```

## in notebook mode:
* ipynb: OK ![OK](jupytext-notebook-OK-ipynb.png)
* jupytext: KO ![KO](jupytext-notebook-KO-py.png)

investigating the jupytext issue

* warnings in the console ![warnings](jupytext-notebook-KO-py-console-warnings.png)
* errors in the console: 1 out of 3 may be of interest
  ![errors](jupytext-notebook-KO-py-console-errors.png)
  ![source](jupytext-notebook-KO-py-console-errors-source.png)

## in jlab mode:

* ipynb: OK
* jupytext: KO
* ![KO](jupytext-lab.png)

investigating

* the warnings in the console are similar to the ones in notebook mode
  ![warnings](jupytext-lab-console-warnings.png)